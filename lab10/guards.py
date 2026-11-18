"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Cổng vòng 1 bên dưới xử lý R1/R2/R3 đã chọn tại Phiếu B, B6.
"""
from . import helpers as H
from .tools import Verdict


def pre_guard(ctx):
    return Verdict.allow()


def _vnd(value):
    if type(value) is not int or value < 0:
        raise ValueError("số tiền không hợp lệ")
    return value


def _verified_facts(ctx, action):
    """Resolve one order/parcel/policy for both refund and fault gates."""
    ticket = ctx.ticket
    if (action.get("ticket_id") != ticket["ticket_id"]
            or action.get("order_id") != ticket.get("order_id")):
        raise ValueError("lệnh ghi không khớp ticket/đơn")
    order = ctx.tools.lookup_order(ticket.get("order_id"))
    if order is None or order["customer_id"] != ticket["customer_id"]:
        raise ValueError("không xác thực được đơn/chủ đơn")
    parcels = order["parcels"]
    if not parcels:
        raise ValueError("đơn không có kiện")
    pid = ticket.get("parcel_id")
    if pid is not None and not any(p["parcel_id"] == pid for p in parcels):
        raise ValueError("kiện được chỉ định không thuộc đơn")
    parcel = H.ticket_parcel(order, ticket, ctx.as_of)
    delivered = parcel.get("delivered_date")
    if (parcel.get("status") not in ("DELIVERED", "IN_TRANSIT")
            or bool(delivered) != (parcel["status"] == "DELIVERED")
            or (delivered and H.d(delivered) > H.d(ctx.as_of))):
        raise ValueError("trạng thái/ngày giao của kiện không nhất quán")
    delay = H.db_delay_days(parcel, ctx.as_of)
    if delay > 0 and not parcel.get("delay_cause"):
        raise ValueError("tracking chưa ghi nguyên nhân trễ")
    # The helper returns the first match; reject missing/overlapping effective policies.
    policies = [p for p in ctx.tools.lookup_policies() if H.effective_policy([p], ctx.as_of)]
    if len(policies) != 1:
        raise ValueError("không có chính sách hiệu lực duy nhất")
    _vnd(order["shipping_fee_vnd"])
    _vnd(order["goods_value_vnd"])
    return order, parcel, policies[0], delay


def _fail_open(ctx):
    return any(e.get("type") == "llm_fallback" and e.get("mode") == "fail_open"
               for e in ctx.events)


def _fault_limit_reached(ctx, parcel):
    carrier = ctx.tools.lookup_carrier(parcel["carrier_id"])
    if carrier is None:
        raise ValueError("không xác thực được hãng của kiện")
    limit = ctx.tools.ops_limits()["max_auto_strikes_per_carrier_per_day"]
    if type(limit) is not int or limit < 0:
        raise ValueError("hạn mức lỗi hãng không hợp lệ")
    # World is fresh per scenario/seed (= one day); fault rows have no date/seed fields.
    return len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"])) >= limit


def _valid_approval(ctx, approval_id, order, amount):
    matches = ctx.tools.lookup_approvals(approval_id=approval_id)
    if len(matches) != 1:
        return False
    approval = matches[0]
    scope = {"ticket_id": ctx.ticket["ticket_id"], "order_id": order["order_id"],
             "customer_id": order["customer_id"]}
    if (any(approval.get(k) != v for k, v in scope.items())
            or approval.get("status") != "valid"
            or H.d(approval["expires_at"]) < H.d(ctx.as_of)):
        return False
    approver = (ctx.gates or {}).get("operations", {}).get("approver_id")
    if approver and approval.get("approver_id") != approver:
        return False
    used = ctx.tools.ledger_rows(approval_id=approval_id)
    if any(any(row.get(k) != v for k, v in scope.items()) for row in used):
        return False
    # Partial payments may share the same approval within its scope and remaining budget.
    return sum(_vnd(row["amount_vnd"]) for row in used) + amount <= _vnd(approval["max_vnd"])


def _refund_gate(ctx, action, order, parcel, policy, delay):
    # R1: recompute the entitlement; a customer claim/directive cannot authorize payment.
    entitlement = _vnd(H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause")))
    if entitlement == 0:
        return Verdict.deny("R1: tracking/chính sách không cho quyền hoàn tiền")
    amount = min(_vnd(action["amount_vnd"]), entitlement)
    if amount == 0:
        return Verdict.deny("R1: khoản hoàn phải lớn hơn 0")

    # R3: include seed/history rows and preserve genuine partial payments.
    rows = ctx.tools.ledger_rows(order_id=order["order_id"])
    retry = any(e.get("type") == "write_retry" and e.get("tool") == "issue_refund"
                for e in ctx.events)
    if retry and any(row["ticket_id"] == ctx.ticket["ticket_id"] for row in rows):
        return Verdict.deny("R3: retry sau khi ticket đã ghi tiền, không ghi lại")
    paid = sum(_vnd(row["amount_vnd"]) for row in rows)
    remaining = entitlement - paid
    if remaining <= 0:
        return Verdict.deny("R3: ledger đã trả đủ quyền lợi theo tracking, không trả thêm")
    amount = min(amount, remaining)
    approval_id = action.get("approval_id")
    if approval_id:
        if not _valid_approval(ctx, approval_id, order, amount):
            return Verdict.escalate("R3: phê duyệt sai phạm vi, hết hiệu lực hoặc hết hạn mức")
    elif amount > _vnd(policy["auto_limit_vnd"]):
        return Verdict.escalate("R3: khoản vượt hạn mức tự động cần phê duyệt hợp lệ")

    # R2 preflight: handing off after file_carrier_fault cannot roll back a refund.
    if _fail_open(ctx):
        return Verdict.escalate("R2: policy_check fail_open, chuyển người trước khi ghi tiền")
    if (ctx.switches.get("file_carrier_fault", "on") == "on"
            and H.carrier_at_fault(policy, parcel, delay)
            and _fault_limit_reached(ctx, parcel)):
        return Verdict.escalate("R2: hãng đã chạm hạn mức lỗi tự động trong ngày; duyệt trước ghi tiền")
    changes = {}
    if action["amount_vnd"] != amount:
        changes["amount_vnd"] = amount
    if action.get("payer", "LOGIX") != "LOGIX":
        changes["payer"] = "LOGIX"  # LATE entitlement is paid by LogiX, not a buyer directive.
    if changes:
        return Verdict.modify("R1/R3: sửa khoản hoàn/bên trả theo quyền lợi còn lại trong ledger", **changes)
    return Verdict.allow()


def _carrier_fault_gate(ctx, action, parcel, policy, delay):
    # R2: a refund does not itself establish carrier liability.
    if _fail_open(ctx) or not H.carrier_at_fault(policy, parcel, delay):
        return Verdict.deny("R2: không có căn cứ ghi lỗi hãng theo tracking/chính sách")
    if _fault_limit_reached(ctx, parcel):
        return Verdict.escalate("R2: hãng đã chạm hạn mức lỗi tự động trong ngày")
    expected = {"parcel_id": parcel["parcel_id"], "carrier_id": parcel["carrier_id"],
                "driver_id": parcel.get("driver_id"), "delay_days": delay}
    changes = {key: value for key, value in expected.items() if action.get(key) != value}
    if changes:
        return Verdict.modify("R2: sửa kiện/hãng/tài xế/độ trễ theo tracking", **changes)
    return Verdict.allow()


def _blocked_refund_reply(ctx, action):
    """Only clarify a denied new payment when earlier payments actually exist."""
    blocked = any((e.get("type") == "gate" and e.get("tool") == "issue_refund"
                   and e.get("action") == "deny") or e.get("type") == "host_denied"
                  for e in ctx.events)
    if not blocked:
        return Verdict.allow()
    order = ctx.tools.lookup_order(ctx.ticket.get("order_id"))
    if (order is None or order["customer_id"] != ctx.ticket.get("customer_id")
            or action.get("ticket_id") != ctx.ticket["ticket_id"]
            or action.get("customer_id") != order["customer_id"]):
        return Verdict.allow()
    rows = ctx.tools.ledger_rows(order_id=order["order_id"], customer_id=order["customer_id"])
    total = sum(_vnd(row["amount_vnd"]) for row in rows)
    new = sum(_vnd(e["amount_vnd"]) for e in ctx.events
              if e.get("type") == "tool" and e.get("tool") == "issue_refund"
              and e.get("order_id") == order["order_id"]
              and e.get("ticket_id") == ctx.ticket["ticket_id"])
    if new or total <= 0:
        return Verdict.allow()
    return Verdict.modify(
        "R3: phân biệt khoản trả trước và khoản mới bị chặn",
        text=f"Theo sổ cái, đơn {order['order_id']} đã được trả {total:,}đ trước lượt này. "
             "Lượt này không ghi thêm khoản hoàn nào.", amount_vnd=0)


def write_gate(ctx, action):
    if action.get("tool") not in ("issue_refund", "file_carrier_fault", "send_reply"):
        return Verdict.allow()
    if (action["tool"] == "file_carrier_fault"
            and ctx.switches.get("file_carrier_fault", "on") != "on"):
        return Verdict.allow()  # Host switch suppresses the write; do not hand off after payment.
    try:
        if action["tool"] == "send_reply":
            return _blocked_refund_reply(ctx, action)
        order, parcel, policy, delay = _verified_facts(ctx, action)
        if action["tool"] == "issue_refund":
            return _refund_gate(ctx, action, order, parcel, policy, delay)
        return _carrier_fault_gate(ctx, action, parcel, policy, delay)
    except (KeyError, TypeError, ValueError) as exc:
        return Verdict.escalate(f"R1/R2/R3: thiếu hoặc sai dữ kiện để ghi an toàn: {exc}")
