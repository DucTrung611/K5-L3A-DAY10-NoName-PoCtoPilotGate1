# Kế hoạch và chia việc · LAB 10 · Bàn NoName

Repo: `K5-L3A-DAY10-NoName-PoCtoPilotGate1` (giá trị `team` trong tiêu chí và `submission.json` phải ghi **y hệt** tên này).

Đề đầy đủ: [README.md](README.md), [problem-set.md](problem-set.md), [RUBRIC.md](RUBRIC.md). File này chỉ để bàn biết **ai làm gì, lúc nào**.

## 1. Bốn người, bốn phần việc

| Người | Phụ trách | Công việc cụ thể | Sản phẩm bàn giao | Câu của đề |
|---|---|---|---|---|
| **TV1 · Kỹ sư cổng: xây biện pháp bảo vệ** | Logic phòng ngừa | Đọc `helpers.py`, `agent.py`; viết `pre_guard`, `write_gate`; kiểm điều kiện trước hoàn tiền, ghi lỗi hãng, gửi thông tin; sửa theo nguyên nhân sự cố | `lab10/guards.py`; giải thích từng cổng chặn gì, dựa vào dữ liệu nào (B7.1, phần code của C7) | 1.3, 2.6, 2.7, 3.5 (code) |
| **TV2 · Kỹ sư cổng: đánh giá và giám sát** | Bằng chứng kỹ thuật, **giữ máy chạy lệnh chính** | Chạy `eval`, `gate`, `grade`, public tests; ký, chốt, push; thiết kế hai ca `--adhoc`; phân tích lỗi; viết specification, fault tree, monitor | `lab10/monitors.py`; mã lần chạy (B0, C0), bảng trước/sau, ca kiểm thử và phân tích lỗi (B1, B2, B7.3, C2, C5 câu 3.2, C6, C8, C9) | 2.1, 2.2, 2.8, 3.1, 3.2, 3.4, 3.6, 3.7 (cây) |
| **TV3 · Kinh doanh** | Tiêu chí, chi phí, ROI, phạm vi pilot | Chuẩn bị tiêu chí trước khi đo; tính đủ chi phí; đọc kết quả theo kho/hãng; đề xuất ngân sách, phạm vi; lập luận quyết định v1/v2 | Phiếu A (trừ 1.2, 1.3, 1.4); `config/acceptance_criteria.json`; các số `business` kèm lý do (B7.4); bản đồ dữ liệu (B3); quyết định B8, C12 | 1.1, 1.6, 2.3, 2.9, 3.5 (business), v1, v2 |
| **TV4 · Pháp lý, rủi ro và vận hành** | HAZOP, checklist, trách nhiệm, xử lý sự cố | Chủ trì HAZOP; gom checklist 9 nhóm; kiểm dữ liệu cá nhân và quyền ghi; xác định người duyệt, cảnh báo, điều kiện dừng, runbook | HAZOP hai vòng (B4, C4); checklist có PIC (B5, C11); runbook (B7.5, B7.6, C11); config `operations`/`legal`; risk register (C10); `submission/submission.json` | 1.2, 1.4, 2.4, 2.10, 3.0, 3.3, 3.5 (ops/legal), 3.7 |

**Cả bàn cùng làm:** câu 1.5, 2.5 (pre-mortem), quyết định v1 và v2. Fault tree (3.4, 3.7) do TV2 cầm bút, cả bàn góp nhánh: TV3 góp nhánh kinh doanh, TV4 góp nhánh con người và pháp lý.

Hai kỹ sư chia theo **công việc**, không chia theo hàm: TV1 viết cổng trong lúc TV2 chuẩn bị ca kiểm thử, đọc trace và xây monitor, nên ít khi cùng sửa một file.

## 2. Luật làm việc trên một repo

1. **Máy chính là máy TV2.** Chỉ máy TV2 chạy `lab10.criteria sign`, `lab10.eval`, `lab10.gate`, `lab10.checkpoint`, `lab10.grade`, `lab10.check_submission`. Lý do: `eval` và `grade` ghi vào `runs/journal.jsonl` (thư mục `runs/` không lên git), team chấm dùng file này để kiểm "ký trước khi đo". Nhật ký phải nằm trọn ở một máy.
2. **TV1 tự thử cổng trên máy mình** bằng `python -m lab10.trace …` và `python -m unittest discover -s tests` (hai lệnh này không ghi nhật ký). Khi cổng ổn: commit + push `lab10/guards.py` → báo TV2 → TV2 `git pull` rồi mới chạy `eval`.
3. **Config chung một file:** TV3 sửa `business`, TV4 sửa `operations` và `legal` trong cùng `config/operating_gates.json`. Báo nhau trước khi lưu; pull trước khi sửa, push ngay sau khi sửa.
4. **Phiếu:** mỗi người viết phần mình, pull trước khi push. Nếu xung đột, giữ cả hai phần rồi báo người kia.
5. **Không ai mở rồi lưu** `config/acceptance_criteria.json` sau khi ký.
6. Mọi lần chạy chỉ đổi MỘT thứ, ghi rõ trong `--note`.

## 3. Số liệu dùng chung (từ `data/world.json`)

| Nhóm | Số |
|---|---|
| `ops_facts` | Ca 480 phút · 1 người duyệt 6 ca/giờ (10 phút/ca; kiểm lại có ghi chú chỉ 4 phút) · làm tay 10.000đ/ticket · 1 ca chuyển người 10.000đ · phí giữ chỗ người trực thêm 30.000đ/ca |
| `ops_limits` | Ngân sách hoàn tự động 2.000.000đ/ngày · tối đa 300.000đ/khách/ngày · tối đa 2 lỗi tự động/hãng/ngày · người duyệt nhận ca trong 60 phút · tiền LLM ≤ 1.500đ/ticket |
| `staff` | `NV-HANH` Trần Thị Hạnh (trưởng ca CSKH, duyệt vượt hạn mức) · `NV-TUNG` Lê Thanh Tùng (giám sát vận hành, giữ công tắc tắt) · `NV-OANH` Phạm Kiều Oanh (kế toán đối soát) |
| `policies` | `as_of` = 2026-11-16, đang hiệu lực **REFUND-v3** (hoàn phí từ trễ 3 ngày, thưởng từ 7 ngày, hạn mức tự động 200.000đ). **REFUND-v4 hiệu lực từ 2026-12-01** (trễ 2 ngày, hạn mức 100.000đ, bất khả kháng không ghi lỗi hãng) |
| Hãng | GHSH phạt 150.000đ/lỗi, treo sau 3 lỗi/7 ngày · VNX 100.000đ, sau 10 · MKD 120.000đ, sau 5 · DNB 80.000đ, sau 3 · LGX nội bộ |
| Kho | HN · HCM · DN · CT · HCM-B2B (đơn sỉ ≥ 2 triệu) |

Mọi ngưỡng, con số, quyết định là **của bàn**: phần "gợi ý" dưới đây chỉ chỉ chỗ có dữ liệu; bàn tự chọn và phải giải thích được lúc demo. **Không chép ngưỡng từ `acceptance_criteria.example.json`** (bị trừ điểm).

## 4. Lịch tổng (ai làm gì theo từng khối)

| Phút | TV1 · Bảo vệ | TV2 · Đánh giá, giám sát | TV3 · Kinh doanh | TV4 · Pháp lý, vận hành |
|---|---|---|---|---|
| 0–15 | Clone, test OK | Clone, test OK; trưởng nhóm điền `TEAM.md` | Chọn eval card + PRD v1.1 | Clone, test OK |
| 15–35 | Đọc `agent.py`, `helpers.py`; **1.3** offline metric (A2) | Đọc `world.json`, `tickets.jsonl`; giúp TV1 tìm sự kiện trace cho 1.3 | **1.1** (A1); nháp ngưỡng | **1.2** (A1); **1.4** telemetry (A2) |
| 35–40 | **1.5** cả bàn (A3) | | | |
| 40–60 | Soát `decision_rule` đo được bằng report | Soát 4 câu hỏi (A4 bước 2) | **1.6**, điền `acceptance_criteria.json` | Nháp `stop_condition` |
| 60–65 | | ⛔ **Ký** + commit + push | Điền A5 | |
| 65–75 | Nháp cổng (chưa sửa file) từ danh sách điểm yếu | **2.1** base + gate (B0, B1); **2.2** trace T-002@55 (B2) | **2.3** bản đồ dữ liệu + drift (B3) | **2.4** HAZOP vòng 1 (B4) + checklist (B5) |
| 75–85 | **2.5** pre-mortem cả bàn (B6), chọn 2–3 lý do thành cổng | | | |
| 85–105 | **2.6** code 2–3 cổng (B7.1); **2.7** (B7.2) | **2.8** hai ca `--adhoc` (B7.3); chạy `eval --stage after` mỗi khi TV1 push | **2.9** `business` (B7.4) | **2.10** `operations`, `legal`; runbook 1–3 + giờ cao điểm (B7.5, B7.6) |
| 105–115 | | ⛔ **Checkpoint** → prepared → gate → push | **Quyết định v1** (B8) | Kiểm checklist khớp số mới |
| 125–135 | | ⛔ Kéo thẻ → `grade` trước khi sửa (C0) | Ghi `Thẻ đã bốc:` | **3.0** C1 (mở lại pre-mortem) |
| 135–150 | Đọc thẻ, trace cùng TV2 để tìm nguyên nhân kỹ thuật | **3.1** trace ≥ 2 ticket, soát lỗi (C2) | Đọc kho/hãng, chi phí của thẻ | C3 phần riêng; C4 HAZOP thẻ; **3.3** (C5) |
| 145–155 | | **3.2** specification (C5); **3.4** fault tree trước (C6), cả bàn góp | góp nhánh kinh doanh | góp nhánh con người, pháp lý |
| 155–180 | **3.5** sửa `guards.py` (C7 phần code) | **3.6** monitor (C8); chạy eval Sx, eval base, grade | Sửa `business` nếu cần (C7) | Sửa `operations`/`legal` nếu cần (C7) |
| 180–190 | | **3.7** fault tree sau (C9) | | **3.7** C10, C11 (checklist, runbook 4–5) |
| 185–200 | | Lệnh 7, push | **Quyết định v2** (C12) + ba dòng | `submission.json`; sửa `[THIẾU]` |
| 200–240 | Demo: giải thích cổng | Demo: chiếu ba mốc, chạy ca hiểm | Demo: quyết định v2 | Demo: người, quy trình; nhắc trả số về v2 |

---

## 5. Quy trình chi tiết từng người

Cách đọc: mỗi bước ghi **Phút · Làm gì · File / lệnh · Ghi vào ô nào · Xong khi**. Đánh `[x]` khi xong. ⛔ = điểm chặn, cả bàn chờ. 🤝 = làm chung.

### TV1 · Kỹ sư cổng: xây biện pháp bảo vệ

**Bước 1 · Cài đặt (phút 0–15)**
- [ ] Clone repo, `git remote add upstream https://github.com/VinUni-AI20k/K5_L3_Day10_PoC-to-Pilot_Gate1_student.git`
- [ ] `git config user.name "<MSSV trưởng nhóm>"`, `git config user.email "<MSSV>@example.com"`
- [ ] `python -m unittest discover -s tests` → `Ran 13 tests … OK`

**Bước 2 · Đọc code (phút 15–20)**
- [ ] Đọc `lab10/agent.py` hàm `run_ticket` (đọc ticket → tra đơn → chọn chính sách → tính tiền → phê duyệt → ghi), `lab10/helpers.py`, đầu file `lab10/guards.py`, [guide Phụ lục C](docs/guide.md#phu-luc-c)
- [ ] Lập danh sách chỗ agent tin thứ không phải nguồn sự thật, gửi TV4 (HAZOP) và cả bàn (pre-mortem). Gợi ý chỗ xem: số ngày trễ khách tự khai (`model_override`); nguyên nhân trễ trống bị coi là lỗi hãng; ghi chú lúc đặt hàng (`checkout_note`) được model đọc như lệnh; LLM lỗi thì "fail_open"; không chắc đã ghi thì ghi lại (`write_retry`); lỗi hãng luôn gán cho kiện đầu tiên; chính sách lấy theo cờ `index_active`; cờ `refund_status` chỉ cập nhật ban đêm; payload gửi hãng có chữ khách tự gõ và (đơn quà) tên, số điện thoại người nhận

**Bước 3 · Câu 1.3, offline metric (phút 20–35) → Phiếu A, A2 cột "Offline"**
- [ ] Chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng), khác bước của ví dụ mẫu
- [ ] Điền 5 ô: bước, thước đo (có đơn vị), dữ liệu (sự kiện nào trong `runs/<mã>/traces/`, 22 ticket × 5 seed, ai gán nhãn), cách tính (mẫu số, ca thiếu dữ liệu), điểm mù

**Bước 4 · Câu 1.5 🤝 (phút 35–40) → A3**

**Bước 5 · Soát tiêu chí với TV3 (phút 50–60)**: mỗi dòng `decision_rule` phải đọc được từ output `lab10.gate`

**Bước 6 · Nháp cổng (phút 65–75)**: viết ra giấy 3–5 cổng ứng viên (hàm nào, tool nào, so với nguồn sự thật nào). Chưa sửa file

**Bước 7 · Pre-mortem 🤝 (phút 75–85) → B6**: cầm lăng kính Kỹ thuật; cùng bàn chọn 2–3 lý do thành cổng

**Bước 8 · Câu 2.6, code 2–3 cổng (phút 85–101) → `lab10/guards.py`, B7.1**
- [ ] Mỗi cổng ứng với 1 dòng B6 hoặc B4; viết trước dòng `return Verdict.allow()` cuối hàm
- [ ] `pre_guard(ctx)` chạy trước khi agent đọc ticket; `write_gate(ctx, action)` chạy trước `issue_refund`, `file_carrier_fault`, `notify_carrier`, `send_reply`. Lưu ý agent ghi tiền **trước**, ghi lỗi hãng **sau**
- [ ] Chỉ dựa vào nguồn sự thật: `ctx.tools.lookup_order`, `H.db_delay_days`, `H.ticket_parcel`, `H.effective_policy`, `H.entitlement_vnd`, `H.carrier_at_fault`, `ctx.tools.ops_limits()`, `ctx.tools.fault_rows(...)`, `ctx.tools.ledger_rows(...)`, `ctx.tools.lookup_approvals(...)`
- [ ] **Không** so khớp mã ticket, mã đơn hay câu chữ cụ thể (test ẩn sẽ bắt)
- [ ] Ưu tiên `modify` / `deny` khi tính lại được từ nguồn sự thật; chỉ `escalate` khi thật sự cần người (mỗi ca chuyển người tốn 10.000đ và làm dài hàng chờ)
- [ ] Thử trên máy mình: `python -m lab10.trace --suite base --ticket <ID> --seed <11|22|33|44|55> --stage after` + `python -m unittest discover -s tests`
- [ ] Cổng ổn → commit + push `lab10/guards.py` → báo TV2 chạy `eval --stage after`; đọc kết quả, không ca nào trước đúng mà giờ sai
- [ ] Điền B7.1: hàm + nhánh, dòng B6/B4, chặn gì + nguồn sự thật, mã lần chạy (TV2 gửi), "ca bị hỏng: không"

**Bước 9 · Câu 2.7 (phút 101–105) → B7.2**: 2 bước tránh "chỉnh trên chính bộ dùng để chấm" (gắn với bộ nền, gói sự cố, test ẩn)

**Bước 10 · ⛔ Trước phút 105**: `guards.py` bản cuối vòng 1 đã push, TV2 đã pull. Sau checkpoint không sửa `lab10/guards_round1.py`

**Bước 11 · Phân tích thẻ (phút 135–155)**: 🤝 đọc trace cùng TV2, chỉ ra nguyên nhân kỹ thuật và cổng vòng 1 đã/không đỡ; góp nhánh kỹ thuật cho fault tree

**Bước 12 · Câu 3.5, sửa cổng (phút 155–180) → `guards.py`, C7**
- [ ] Giữ cổng vòng 1, thêm nhánh mới cho nguyên nhân kỹ thuật; mỗi lần đổi MỘT thứ
- [ ] Thử bằng `python -m lab10.trace --suite Sx --ticket <ID> --seed 11 --stage after` → push → TV2 chạy eval Sx, eval base, grade
- [ ] Điền các dòng code của C7: nhánh, nguyên nhân, chỗ sửa (hàm + nhánh), tầng, giảm hay ngăn và vì sao, mã lần chạy

**Bước 13 · Demo + nộp (phút 200–240)**: giải thích từng cổng chặn gì, dựa vào dữ liệu nào; viết mục cá nhân + exit ticket trong `TEAM.md`; nộp link LMS

---

### TV2 · Kỹ sư cổng: đánh giá và giám sát (máy chính)

**Bước 1 · Cài đặt (phút 0–15)**
- [ ] Repo Private; mời team chấm (Read) và TV1, TV3, TV4 (nếu TV2 là chủ repo; nếu không thì nhờ chủ repo)
- [ ] Clone, gắn `upstream`, đặt `user.name`/`user.email` (MSSV trưởng nhóm, email giả), test OK
- [ ] Trưởng nhóm điền bảng thành viên `TEAM.md`, push

**Bước 2 · Đọc dữ liệu (phút 15–35)**
- [ ] Đọc `data/world.json` (`orders[].parcels`, `policies`, `approvals`), `data/tickets.jsonl`, `lab10/agent.py`
- [ ] 🤝 Giúp TV1 câu 1.3: tìm sự kiện trong trace làm dữ liệu cho thước đo

**Bước 3 · Câu 1.5 🤝 (phút 35–40) → A3**

**Bước 4 · Soát tiêu chí (phút 40–60) → A4 bước 2**: điền bảng 4 câu soát (mọi bên? ai thiệt? ngày 1? ngày 1.000?) cho bản nháp TV3

**Bước 5 · ⛔ Ký (phút 60–65)**
- [ ] Pull bản tiêu chí TV3 đã điền; `python -m lab10.criteria sign` → `ĐÃ KÝ.`
- [ ] Chạy đúng dòng git máy in (add + commit `Sign acceptance criteria` + push). VS Code báo lỗi mạng thì chạy lại trong terminal
- [ ] Gửi mã commit cho TV3 điền A5
- Xong khi: commit ký có trên GitHub. **Trước bước này không ai chạy `lab10.eval`.**

**Bước 6 · Câu 2.1, mốc base (phút 65–71) → B0 dòng 1, B1**
- [ ] `python -m lab10.eval --suite base --stage base --note "baseline"` → ghi mã lần chạy
- [ ] `python -m lab10.gate --run runs/<mã>/report.json`
- [ ] Ghi ngưỡng `[CHƯA]`, dòng đáng lo ở khối "kinh doanh và vận hành", kho/hãng xấu nhất
- [ ] Bảng lý lẽ tự chặn vs người duyệt, khoanh khuyến nghị
- [ ] Gửi khối kinh doanh + theo kho/hãng cho TV3, khối hàng chờ cho TV4

**Bước 7 · Câu 2.2, soát lỗi `T-002@55` (phút 71–75) → B2**
- [ ] `python -m lab10.trace --suite base --ticket T-002 --seed 55`
- [ ] Phần 1: ≥ 2 lỗi bằng dòng trace, ai chịu, mức hệ trọng, loại lỗi (giới hạn / ngữ cảnh / chìm)
- [ ] Phần 2: đánh dấu nguồn. Phần 3: hướng xử lý + tên metric sẽ theo dõi
- [ ] Gửi kết luận cho TV1 và TV4

**Bước 8 · Pre-mortem 🤝 (phút 75–85) → B6**: thư ký, ghi bảng B6 cho cả bàn

**Bước 9 · Câu 2.8, behavioral test (phút 85–100) → B7.3**
- [ ] Viết 1 tính chất (một câu, dạng "dù ticket nói gì, …")
- [ ] Viết 2 ticket hiểm **mới** (cách viết khác bộ nền), `--order`/`--customer` có thật trong `world.json` (khách là chủ đơn)
- [ ] Sau khi pull cổng của TV1: `python -m lab10.trace --suite base --stage after --adhoc "…" --order O-10xx --customer C-xx`
- [ ] Dán dòng `SỔ CÁI` / `LỖI HÃNG` / `GỬI HÃNG`; ghi tính chất có giữ được. Giữ 2 ca cho demo

**Bước 10 · Đo cổng vòng 1 (phút 85–105, mỗi khi TV1 push)**
- [ ] `git pull` → `python -m lab10.eval --suite base --stage after --note "cổng vòng 1: <tên cổng>"` + unittest
- [ ] So từng ticket với base: báo TV1 nếu có ca hỏng mới; gửi mã lần chạy cho TV1 điền B7.1; ghi B0

**Bước 11 · ⛔ Chốt vòng 1 (phút 105–110)** — chỉ chạy khi TV1, TV3, TV4 đã push bản cuối `guards.py`, `operating_gates.json`
- [ ] `git pull` → `python -m lab10.checkpoint` → `ĐÃ CHỐT cổng vòng 1 … 8 ký tự đầu: …`
- [ ] `python -m lab10.eval --suite base --stage prepared` → `python -m lab10.gate --run runs/<mã>/report.json`
- [ ] Gửi mã lần chạy + output gate cho TV3 viết v1; điền B0 dòng 2–3

**Bước 12 · Push v1 (phút 110–115)**: pull phiếu B của TV3, chạy lệnh git cuối B8

**Bước 13 · Nháp monitor (phút 115–125, giờ nghỉ, tuỳ chọn)**: đọc `lab10/monitors.py`; trial có `events`, `ledger`, `faults`, `outbound`, `cost_vnd`, `queue_wait_min`, `warehouse`, `review_kind`…

**Bước 14 · ⛔ Nhận thẻ (phút 125–135) → C0**
- [ ] `git pull --no-rebase --no-edit --allow-unrelated-histories -X ours upstream main`; có `incidents/S1…S8`, `incident-cards.md` (nếu file phiếu không đổi theo repo đề, đó là đúng: `-X ours` giữ bài của bàn)
- [ ] `python -m lab10.grade --incident Sx` **trước khi sửa gì** → `1 integrity | ✅`; ghi mã lần chạy vào C0 dòng 1, gửi cả bàn
- [ ] Push để TV1, TV3, TV4 có thẻ

**Bước 15 · Câu 3.1, soát lỗi thẻ (phút 135–150) → C2**
- [ ] `python -m lab10.trace --suite Sx --ticket <ID> --seed 11` cho ≥ 2 ticket hỏng **khác kiểu**
- [ ] Ghi tác hại (cho ai, đo bằng gì, bao nhiêu ở base); ≥ 3 lỗi, ≥ 2 nguồn khác nhau, ≥ 1 lỗi chìm; đủ 3 phần

**Bước 16 · Câu 3.2 + 3.4 (phút 145–155) → C5, C6**
- [ ] Specification: một câu "phần mềm phải …" mà vi phạm thì gây tác hại trên thẻ; kiểm bằng hàm trong `guards.py` hoặc dòng report
- [ ] 🤝 Fault tree trước: sự kiện đỉnh là tác hại; ≥ 2 nhánh ở 2 tầng khác nhau (nhận nhánh kinh doanh từ TV3, nhánh con người/pháp lý từ TV4); mỗi lá có `ticket@seed` hoặc dòng report; bảng spec / giả định cho từng lá

**Bước 17 · Câu 3.6, chỉ số theo dõi (phút 155–180) → `lab10/monitors.py`, C8**
- [ ] Thêm một hàm phía trên dict `MONITORS`, nhận `trials` (không nhãn), trả về một số; đăng ký `"tên_chỉ_số": tên_hàm`
- [ ] Giá trị phải **khác nhau** giữa bộ nền và gói sự cố; `escalation_rate` có sẵn không tính
- [ ] Điền C8: tên, bước đo, thước đo, dữ liệu, cách tính, ngưỡng báo động, điểm mù, giá trị nền · thẻ

**Bước 18 · Đo sau khi sửa (phút 155–185, mỗi khi có người push)**
- [ ] `git pull` → `python -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: …"`
- [ ] `python -m lab10.eval --suite base --stage after --note "kiểm lại bộ nền sau khi sửa"`
- [ ] `python -m lab10.grade --incident Sx` → cần `visible ✅`, `regression ✅`, `monitor ✅`; ghi C0 dòng 2–4, gửi mã cho người sửa điền C7

**Bước 19 · Câu 3.7, fault tree sau (phút 180–185) → C9**: thêm nút `VÀ [gate … hỏng]`, ghi tầng, giảm hay ngăn, nhánh còn hở

**Bước 20 · Gom bài (phút 190–200)**
- [ ] Pull mọi phiếu và `submission.json`; `python -m lab10.check_submission --collect`; cùng TV4 sửa `[THIẾU]` tới `ĐỦ THÀNH PHẦN`
- [ ] Push theo README mục 6

**Bước 21 · Demo + nộp (phút 200–240)**: chiếu ba cột base · prepared · after; chạy ca hiểm khi bàn kia phản biện; sau demo trả số về v2, chạy lại `grade` + lệnh 7, push lần cuối; mục cá nhân `TEAM.md`; nộp link LMS

---

### TV3 · Kinh doanh

**Bước 1 · Chuẩn bị (phút 0–15)**: clone, test OK; chọn eval card + PRD v1.1 (Lab 9) làm bản chung; mở `world.json` mục `ops_facts`, `ops_limits`, `policies`

**Bước 2 · Câu 1.1 (phút 15–20) → A1**: một mục tiêu cấp hệ thống (khác "model trả lời đúng"), dựa PRD §3

**Bước 3 · Nháp ngưỡng (phút 20–35)**
- [ ] Tính đủ chi phí một ticket: tiền máy (LLM + nền tảng) + công người khi chuyển duyệt/kiểm lại + phí người trực, so với làm tay 10.000đ
- [ ] Liệt kê từng khoá và số tham chiếu: `cost_per_ticket_vnd_max` · `roi_min` · `queue_stuck_max` (SLA 60 phút) · `escalation_rate_max` · `pass_rate_min`, `pass_k_min` · ba chỉ số an toàn (đề gợi ý để 0)

**Bước 4 · Câu 1.5 🤝 (phút 35–40) → A3**

**Bước 5 · Câu 1.6, Bản tiêu chí (phút 40–58) → A4**
- [ ] Mỗi chỉ số bắt buộc một câu "Nếu {chỉ số} của {trợ lý, trên bộ nào} {tụt dưới / vượt} {ngưỡng} thì chúng tôi sẽ {hành động}"; chỉ số tranh luận nhiều nhất viết 2 phiên bản
- [ ] Hai câu ranh giới đầu ra: một hành động bị cấm, một ngưỡng chuyển người duyệt
- [ ] Bước 2: nhận bảng soát từ TV2. Bước 3: điền `business_ops`, ngày xem lại + ai dự
- [ ] Điền `config/acceptance_criteria.json`: `team` = `K5-L3A-DAY10-NoName-PoCtoPilotGate1`, `signed_by`, `required` (5), `nice_to_have`, `business_ops` (3), `stop_condition` (nhận nháp từ TV4), `decision_rule` (4 dòng, mỗi dòng nêu chỉ số nào đạt/chưa thì chọn quyết định đó)
- [ ] 🤝 Soát với TV1 rằng mỗi điều kiện đọc được từ output `lab10.gate`

**Bước 6 · ⛔ Push file tiêu chí cho TV2 ký (phút 60)**; điền A5 (giờ ký, mã commit, đã push). **Từ đây không mở file tiêu chí.**

**Bước 7 · Câu 2.3, bản đồ dữ liệu (phút 65–75) → B3**
- [ ] Điền 9 dòng bảng và đoạn "Tóm lại"
- [ ] Trường then chốt nên xem: `parcels[].promised_date`, `delivered_date`, `delay_cause`, `policies[].index_active` / `effective_from`, `refund_status`
- [ ] Ví dụ drift: REFUND-v4 hiệu lực 2026-12-01 (cái gì đổi, ngày nào, trường nào thấy, con số tiêu chí nào bị ảnh hưởng, đầu vào đổi hay quan hệ vào–ra đổi, chỉ số nào phát hiện)

**Bước 8 · Pre-mortem 🤝 (phút 75–85) → B6**: cầm lăng kính Kinh doanh (chi phí mỗi ticket so với làm tay, trần hoàn mỗi ngày, nhóm ticket không thể có lời, ví dụ kho sỉ HCM-B2B)

**Bước 9 · Câu 2.9, cổng kinh doanh (phút 85–100) → `operating_gates.json` mục `business`, B7.4**
- [ ] Đọc khối "theo kho và hãng" của mốc base (TV2 gửi) để chọn phạm vi
- [ ] `daily_refund_cap_vnd` (tham chiếu ngân sách Finance 2.000.000đ/ngày) · `cost_budget_per_ticket_vnd` (tham chiếu 1.500đ) · `pilot_scope` (`all` / `warehouse` + danh sách kho / `percent`; đề nói pilot ở 2 depot) · `roi_min`
- [ ] Mỗi số một câu lý do có số → B7.4
- [ ] Pull → sửa → push ngay; báo TV4 (cùng file) và TV2

**Bước 10 · Quyết định v1 🤝 (phút 108–115) → B8 cột v1**
- [ ] Nhận mã base + prepared và output gate từ TV2
- [ ] Điền: commit ký, hash chốt, dòng vượt trần, kho/hãng xấu nhất (quyết định có đổi nếu chỉ nhìn phân khúc đó?), quyết định, 3 bằng chứng có mã lần chạy, dòng `decision_rule` khớp, phần Thu hẹp / Cải tiến / Dừng, bằng chứng còn thiếu, ngày quyết định lại, PIC ký
- [ ] Không chọn Tiếp tục nếu còn `[CHƯA]` hoặc vượt trần; push phiếu B cho TV2

**Bước 11 · Nhận thẻ (phút 125–135)**: ghi `Thẻ đã bốc: Sx` ở đầu Phiếu C (`templates/form-c-incident.md`)

**Bước 12 · Phân tích kinh doanh của thẻ (phút 135–155)**: đọc chi phí mỗi ticket, ROI, trần tiền, theo kho/hãng ở ba mốc; góp nhánh kinh doanh cho fault tree

**Bước 13 · Câu 3.5 phần tiền / phạm vi (phút 155–180) → `business`, C7**
- [ ] Nếu nguyên nhân là tiền, chi phí, phạm vi: sửa `business`, mỗi lần MỘT thứ; push → TV2 chạy eval + grade
- [ ] Không thu hẹp về 0; đọc lại chi phí, ROI, độ phủ; điền dòng tương ứng ở C7

**Bước 14 · Quyết định v2 (phút 185–197) → C12**
- [ ] Cột v2 (như v1, thêm mã ba mốc của thẻ)
- [ ] Mục "Chỉ ở v2": đổi hay giữ so với v1 và vì con số nào; ô còn đỏ; cổng vòng 1 đỡ gì / bỏ sót gì; report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"
- [ ] Nếu Thu hẹp: cắt kho nào, còn bao nhiêu phần trăm, mấy người trực, ticket bị cắt đi đâu
- [ ] Ba dòng bắt buộc, mỗi dòng gắn con số; gửi TV4 chép sang `submission.json`

**Bước 15 · Demo + nộp**: trình bày quyết định v2 và con số đỡ cho nó; giải thích từng ngưỡng; mục cá nhân `TEAM.md`; nộp link LMS

---

### TV4 · Pháp lý, rủi ro và vận hành

**Bước 1 · Cài đặt (phút 0–15)**: clone, test OK; đọc `world.json` mục `staff`, `ops_facts`, `staff_behavior`, `carriers`

**Bước 2 · Câu 1.2 (phút 15–20) → A1**: một mục tiêu nhìn từ chị Oanh (khớp sổ với hãng và shop mỗi tuần), một từ chị Hạnh (duyệt ca trợ lý chuyển sang); dựa PRD §2, §6

**Bước 3 · Câu 1.4, telemetry production (phút 20–35) → A2 cột phải**
- [ ] Tín hiệu thiệt hại cho bên **ngoài** LogiX (hãng, shop, người nhận) khi không có nhãn
- [ ] Điền: hành vi đo, thước đo, dữ liệu, cách tính, **khung thời gian + ngưỡng báo động**, điểm mù

**Bước 4 · Câu 1.5 🤝 (phút 35–40) → A3**

**Bước 5 · Nháp `stop_condition` (phút 40–55)**: một câu "khi … thì dừng …", gửi TV3

**Bước 6 · Câu 2.4, HAZOP vòng 1 (phút 65–72) → B4** (chủ trì)
- [ ] Chọn MỘT tool ghi (`issue_refund` / `file_carrier_fault` / `notify_carrier`); dùng danh sách điểm yếu TV1 gửi
- [ ] ≥ 3 dòng với guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE), ≥ 1 dòng là nhánh chưa thấy trên trace
- [ ] Bảng "ngoài kỹ thuật" ≥ 2 dòng: người duyệt (INCAPABLE), ngân sách (WRONG), phạm vi pilot (INVALID), dữ liệu gửi bên thứ ba (PERTURBED)

**Bước 7 · Câu 2.4, checklist 9 nhóm (phút 72–75) → B5**
- [ ] Mỗi dòng: mục cần kiểm, trạng thái, bằng chứng (mã lần chạy / mục phiếu / số report), **PIC là tên một người cụ thể** (không ghi "cả bàn")
- [ ] Kiểm riêng dòng 3 (bảo mật), 4 (quyền ghi: `config/switches.json`, guard trước lệnh ghi), 8 (dữ liệu cá nhân gửi bên thứ ba)

**Bước 8 · Pre-mortem 🤝 (phút 75–85) → B6**: cầm lăng kính Con người và vận hành + Pháp lý

**Bước 9 · Câu 2.10, cổng vận hành và pháp lý (phút 85–95) → `operating_gates.json` mục `operations`, `legal`**
- [ ] `pic`, `approver_id` (mã trong `staff`) · `reviewers_on_shift` · `review_capacity_per_hour` (≤ số người × 6) · `max_queue_wait_minutes` (tham chiếu SLA 60) · `stop_conditions` (danh sách câu "khi … thì …") · `alert_channel`
- [ ] `legal.pii_fields_blocked_to_third_party` (tên trường trong payload gửi hãng) · `legal.carrier_fault_requires_recorded_cause`
- [ ] Không xếp thật nhiều người trực: mỗi người thêm tốn 30.000đ/ca, report đo cả chi phí
- [ ] Pull → sửa → push ngay; báo TV3 (cùng file) và TV2

**Bước 10 · Runbook 1–3 + Giờ cao điểm (phút 95–105) → B7.5, B7.6**
- [ ] Runbook 1: 4 vai có tên/mã nhân viên, quyền, kênh liên lạc; số người trực, ca/giờ, phạm vi, **khớp config**
- [ ] Runbook 2: mỗi tín hiệu có nguồn (dòng report hoặc metric), mức bình thường, ngưỡng vàng/đỏ, ai quyết
- [ ] Runbook 3: dừng một phần / dừng hẳn, cách dừng (công tắc trong `config/switches.json`), thời hạn tối đa từ tín hiệu đỏ đến dừng xong + người bấm, ticket đang chờ đi đâu, điều kiện bật lại
- [ ] Giờ cao điểm: bao nhiêu ticket/giờ, ai trực, ngưỡng gọi thêm người, ngưỡng thu hẹp/tắt, ảnh hưởng chi phí và ROI

**Bước 11 · Quyết định v1 🤝 (phút 108–115)**: kiểm checklist B5 và runbook khớp số trong config đã chốt

**Bước 12 · Câu 3.0 (phút 125–135) → C1**: cổng vòng 1 đỡ được ô nào (so base với prepared), dòng nào còn vượt trần; mở lại pre-mortem bằng màu khác (lăng kính nào, bàn có nghĩ tới không, lý do còn thiếu)

**Bước 13 · Phần riêng theo thẻ + HAZOP thẻ (phút 135–150) → C3, C4**
- [ ] C3: chỉ điền phần ứng với số thẻ (bảng ở đầu C3; thẻ S4 thì bổ sung mục Giờ cao điểm B7.6)
- [ ] C4: HAZOP của thẻ ≥ 3 dòng, mục riêng, không ghi đè B4

**Bước 14 · Câu 3.3, giả định môi trường (phút 145–150) → C5**: thứ nằm NGOÀI phần mềm mà thiết kế ngầm tin, và vì sao có thể sai; góp nhánh con người/pháp lý cho fault tree

**Bước 15 · Câu 3.5 phần người / pháp lý (phút 155–180) → `operations`, `legal`, C7**
- [ ] Nếu nguyên nhân là người, quy trình, dữ liệu cá nhân: sửa `reviewers_on_shift`, `review_sampling_pct`, `decision_note`, `legal.*`…, mỗi lần MỘT thứ; push → TV2 chạy eval + grade
- [ ] Điền dòng tương ứng ở C7

**Bước 16 · Câu 3.7 (phút 180–190) → C10, C11**
- [ ] C10: ≥ 1 dòng risk register (PIC một người, dấu hiệu là metric trong `monitors.py` hoặc report, nhóm GOVERN/MAP/MEASURE/MANAGE)
- [ ] C11: cập nhật checklist (có PIC), Runbook 4 (sau sự cố), Runbook 5 (3 kịch bản "nếu … thì …")

**Bước 17 · Gom bài (phút 190–200)**
- [ ] `submission/submission.json`: `team`, `members` (`HoVaTen-MSSV`, khớp `TEAM.md`), `incident`, `decision_v1`, `decision_v2`, `three_lines` (chép từ C12); push
- [ ] Cùng TV2 sửa từng dòng `[THIẾU]` của lệnh 7 tới `ĐỦ THÀNH PHẦN`

**Bước 18 · Demo + nộp**: trả lời phần người và quy trình; sau demo nhắc trả số về v2 và chạy lại lệnh 6 + 7; mục cá nhân `TEAM.md`; nộp link LMS

---

## 6. Năm điều không được quên (sai là bài không được tính)

1. Ký tiêu chí và push **trước** lần `eval` đầu tiên.
2. Không sửa `acceptance_criteria.json` sau khi ký; không sửa bản chụp vòng 1 (`guards_round1.py`, `operating_gates.round1.json`, `round1.lock`); không sửa file bị khoá.
3. Không xử lý riêng theo mã ticket hay câu chữ.
4. Không chọn **Tiếp tục** khi report còn vượt trần hoặc còn ngưỡng đã ký chưa đạt.
5. `team` = `K5-L3A-DAY10-NoName-PoCtoPilotGate1`; `members` khớp `TEAM.md`; **mỗi người tự nộp link repo trên LMS**.
