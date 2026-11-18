"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""
from .world import DATA, load_json


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def worst_warehouse_cost_per_ticket_vnd(trials):
    """C8 proxy: max warehouse mean of machine, review and suspected repeat cost.

    Rechecks use the agreed with-note estimate, not actual queue review units.
    Repeated refunds are observed within (seed, day), including within a ticket.
    Missing day/seed only permits detection within that individual trial.
    No labels, pass/fail, historical ledger seeds or incident metadata are read.
    """
    facts = load_json(DATA / "world.json")["ops_facts"]
    review_cost = facts["review_cost_per_ticket_vnd"]
    recheck_cost = review_cost * facts["recheck_with_note_units"]
    totals, counts, seen_orders = {}, {}, {}
    for index, trial in enumerate(trials):
        warehouse = trial.get("warehouse")
        if not warehouse or warehouse == "?":
            continue
        cost = trial.get("cost_vnd", 0)
        if trial.get("review_kind") == "escalated":
            cost += review_cost
        elif trial.get("review_kind") == "recheck":
            cost += recheck_cost

        seed, day = trial.get("seed"), trial.get("day")
        context = (seed, day) if seed is not None and day is not None else ("unscoped", index)
        seen = seen_orders.setdefault(context, set())
        for row in trial.get("ledger", []):
            order_id = row.get("order_id")
            if not order_id:
                continue
            if order_id in seen:
                cost += row.get("amount_vnd", 0)
            seen.add(order_id)
        totals[warehouse] = totals.get(warehouse, 0) + cost
        counts[warehouse] = counts.get(warehouse, 0) + 1
    return max((total / counts[w] for w, total in totals.items()), default=0)


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "worst_warehouse_cost_per_ticket_vnd": worst_warehouse_cost_per_ticket_vnd,
}
STARTER_MONITORS = ("escalation_rate",)
