# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): NoName
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-NoName-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Thân Đức Trung | 2A202603449 | Vận hành và pháp lý (TV4) |      ✓      |
|   2 | Lưu Văn Việt Đức | 2A202603445 | Kỹ sư cổng: xây biện pháp bảo vệ (TV1) |             |
|   3 | Ngô Gia Bảo | 2A202603482 | Sản phẩm và kinh doanh (TV3) |             |
|   4 | Nguyễn Bá Thành | 2A202609499 | Kỹ sư cổng: đánh giá và giám sát (TV2) |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## ThanDucTrung-2A202603449

### Phần việc phụ trách

Trưởng nhóm; vai **Vận hành và pháp lý (TV4)**. Câu 1.2, 1.4 (Phiếu A mục A1, A2 cột Telemetry); câu 2.4 (Phiếu B mục B4 HAZOP vòng 1, B5 checklist 9 nhóm); chủ trì câu 2.5 (B6 pre-mortem, chốt cổng vòng 1); câu 2.10 (`config/operating_gates.json` mục `operations` và `legal`, Phiếu B mục B7.5 runbook phần 1–3, B7.6 giờ cao điểm). Vòng 2: câu 3.0 (C1), C3, C4, câu 3.3, câu 3.5 phần người/pháp lý, câu 3.7 (C10, C11) và `submission/submission.json`.

### Đóng góp cụ thể

- **Câu 1.2:** viết mục tiêu của chị Oanh (mỗi dòng trợ lý ghi sổ tự đối chiếu được với tracking và chính sách) và của chị Hạnh (ca chuyển sang tới tay trong 60 phút, có đủ căn cứ, trong sức 6 ca/giờ), dựa PRD v1.1 §2, §6 của Lab 9.
- **Câu 1.4:** thiết kế telemetry đếm lỗi hãng không khớp tracking và thông báo gửi hãng có dữ liệu cá nhân người nhận, cửa sổ 24 giờ, ngưỡng đỏ ≥ 1, ngưỡng vàng theo `ops_limits` (2 lỗi/hãng/ngày) và ngưỡng treo hãng GHSH/DNB.
- **B4 HAZOP** trên `file_carrier_fault`: 6 dòng kỹ thuật (2 nhánh chưa thấy trên trace: nguyên nhân trễ trống bị coi là CARRIER, đơn nhiều kiện gán lỗi cho kiện đầu) và 4 dòng ngoài kỹ thuật (người duyệt, ngân sách, dữ liệu gửi bên thứ ba, phạm vi HCM-B2B).
- **B5 checklist** 9 nhóm, mỗi dòng một PIC có tên.
- **B6 pre-mortem:** chốt ba rủi ro thành cổng vòng 1 (R1 hoàn theo số ngày khách tự khai, R2 lỗi hãng oan, R3 ghi lặp/phê duyệt sai), các rủi ro còn lại gắn với cổng config hoặc risk register; điền sẵn ba cột đầu B7.1 cho Kỹ sư cổng. Baseline sau đó xác nhận R1 (`T-002@55`).
- **Config `operations`/`legal`:** `pic = NV-TUNG`, `approver_id = NV-HANH`, 1 người trực, 6 ca/giờ, chờ tối đa 60 phút, 6 điều kiện dừng, kênh `#logix-refund-pilot-alert`; chặn `recipient_contact` và `customer_note` gửi hãng; `carrier_fault_requires_recorded_cause = true`.
- **Runbook 1–3 và Giờ cao điểm:** 4 vai có mã nhân viên, 7 tín hiệu có ngưỡng vàng/đỏ khớp tiêu chí đã ký (`queue_stuck_max = 0`, `cost_per_ticket_vnd_max = 6000`), cách dừng bằng `config/switches.json`, thời hạn dừng 15 phút, điều kiện bật lại.
- Gộp xung đột Phiếu A giữa cột 1.3 (TV1) và cột 1.4 (TV4), giữ nguyên nội dung hai bên.

### Bằng chứng

- Commit: `80d1f41` (config `operations`/`legal`, Phiếu A 1.2, 1.4, Phiếu B B4, B5, B7.5, B7.6) · `726eca5` (B6 pre-mortem, chốt R1–R3) · `30d15e2` (B7.1 cột 1–3).
- Mã lần chạy baseline đối chiếu cho B6/R1: `R-base-before-20261118-154917-611de4` (`T-002@55` hoàn sai 20.000đ, 1 lỗi hãng oan VNX); bằng chứng tại `docs/evidence/R-base-before-20261118-154917-611de4/`.
- Dòng trong phiếu: Phiếu A mục A1 câu 1.2, A2 cột Telemetry; Phiếu B mục B4, B5, B6, B7.5, B7.6.
- **Dùng AI:** dùng Claude Code để đọc `data/world.json`, `lab10/agent.py`, `ops.py`, `tools.py`, soạn nháp các phần trên và kiểm config bằng `lab10.ops.problems` + public tests (`Ran 13 tests … OK`). Mọi con số và tên người do tôi chọn và giải thích được lúc demo; không dùng AI để viết code xử lý theo mã ticket.

### Exit ticket

- Một điều học được: [tự điền]
- Một điều còn chưa chắc: [tự điền]

## LuuVanVietDuc-2A202603445

### Phần việc phụ trách

Bản nháp giai đoạn A ngày 2026-11-18, chờ cá nhân review. Theo yêu cầu trực tiếp: **TV1 — xây biện pháp bảo vệ**, câu 1.3 (A2 cột Offline), chuẩn bị kỹ thuật cho 1.5 và soát tiêu chí/pre-mortem; B7.1, B7.2 và C7 phần code sẽ hoàn thiện đúng điều kiện của từng vòng. Chưa sửa `lab10/guards.py`.

Phân công hiện tại theo xác nhận của người dùng, phù hợp với `PLAN.md`: Lưu Văn Việt Đức phụ trách TV1 — xây biện pháp bảo vệ; Nguyễn Bá Thành phụ trách TV2 — đánh giá và giám sát. Mục cá nhân này ghi nhận phần việc TV1; không thấy phân công P1–P4 cũ trong PLAN.

### Đóng góp cụ thể

- Đọc README, PLAN, RULES, problem-set, CHECKPOINTS, RUBRIC, các mục phiếu liên quan, guide Phụ lục C và code/dữ liệu nền; chỉ phân tích tĩnh, không mở thẻ sự cố.
- Điền đúng năm ô A2 cột Offline: bước chọn chính sách, sự kiện `policy`, nhãn theo khoảng hiệu lực và ngày giả lập, công thức/mẫu số, xử lý dữ liệu thiếu và điểm mù. Đây là thiết kế đo, chưa có giá trị baseline.
- Luồng `run_ticket`: `pre_guard` → LLM đọc ticket → tra đơn/chủ đơn/tracking, có thể đọc `checkout_note` và ghi đè độ trễ theo lời khách → chọn policy → tính tiền/directive/fallback → tìm phê duyệt nếu vượt hạn mức → `issue_refund` → có thể thử ghi tiền lại khi confirm lỗi → `file_carrier_fault` → `notify_carrier` → `send_reply`. Mỗi lệnh ghi qua `write_gate`, công tắc rồi quy tắc host/config trước khi ghi. **Tiền vào ledger trước lỗi hãng**; chuyển người ở bước lỗi hãng không đảo ngược khoản tiền đã ghi.

#### Năm rủi ro/cổng ứng viên — phân tích tĩnh, chưa tái hiện bằng trace

Các mã G1–G5 dưới đây chỉ để thảo luận trong bản nháp cá nhân, chưa phải dòng B4/B6 đã được nhóm chốt. Chỉ chọn 2–3 cổng sau khi có baseline và quyết định pre-mortem/HAZOP.

| Ứng viên, bằng chứng code | Đang tin sai / thiếu kiểm chứng; tác hại có thể xảy ra | Nguồn kiểm chứng và vị trí cổng dự kiến | Giới hạn cần giữ rõ |
|---|---|---|---|
| G1 — Ngữ cảnh và quyền lợi. `agent.py:run_ticket`, nhánh `worst`, `model_override`, chọn `index_active`, `directive_obeyed`, fallback `fail_open` (dòng 112–165); `helpers.py:db_delay_days`, `ticket_parcel`, `effective_policy`. | Lấy kiện trễ nhất thay vì luôn theo kiện ticket; lời khách/ghi chú có thể đổi độ trễ, số tiền, payer; cờ index có thể cũ; nguyên nhân trống được suy thành CARRIER. Có thể hoàn sai, trừ tiền shop hoặc dẫn tới lỗi hãng oan. | Tra đơn/chủ đơn/kiện bằng `lookup_order`; ngày từ `ctx.as_of`; policy từ `lookup_policies` theo khoảng hiệu lực; tính lại bằng `H.entitlement_vnd` với độ trễ/nguyên nhân đã xác thực. `pre_guard` dự kiến ghim policy duy nhất, `write_gate(issue_refund)` kiểm trước ghi; allow ca khớp, modify khi tính lại chắc chắn, deny quyền lợi bằng 0, escalate khi dữ liệu mơ hồ. | Phải kiểm đầu vào helper: mã kiện được chỉ định mà không thuộc đơn không được để `ticket_parcel` tự rơi về kiện trễ nhất; `db_delay_days` không kiểm status; `effective_policy` trả bản đầu tiên nếu khoảng ngày chồng lấn. Cổng ghi không sửa được ca agent đã từ chối trước khi định ghi; DB sai vẫn là nhánh hở. |
| G2 — Phê duyệt đúng phạm vi. `agent.py:run_ticket`, nhánh `preapproved`, `lookup_approvals(order_id=...) or lookup_approvals(customer_id=...)`, lấy `cands[0]` (dòng 156–177); `tools.py:ReadTools.lookup_approvals` chỉ lọc bằng so khớp. | Phê duyệt cùng khách nhưng khác đơn/ticket, đã dùng/hết hạn hoặc không đủ tiền có thể bị dùng; directive có thể bỏ bước xin duyệt. Nguy cơ hoàn vượt quyền và gán trách nhiệm sai cho người duyệt. | `write_gate(issue_refund)` đối chiếu `approval_id` với `lookup_approvals`, đúng ticket/đơn/khách, `status=valid`, `expires_at >= ctx.as_of`, `max_vnd >= amount_vnd`; đối chiếu người duyệt có thẩm quyền do TV4 đặt và việc dùng trước đó trong ledger; không xem lời khách là phê duyệt. Thiếu phê duyệt hợp lệ khi vượt hạn mức thì escalate. | Không tự coi helper đã xác nhận các trường nghiệp vụ; quyền người duyệt cần TV4 xác nhận từ `staff`/config. Lookup rồi ghi không phải giao dịch nguyên tử trong hệ thống nhiều worker. |
| G3 — Ghi tiền lặp. `agent.py:run_ticket`, cờ `refund_status` đối soát đêm (dòng 107–110) và `write_retry` (dòng 185–193); `tools.py:WriteTools.issue_refund` (dòng 133–156) chỉ có trần tổng tiền đơn và trần ngày nếu đã đặt. | Tin cờ chậm cập nhật hoặc lỗi confirm để ghi lại; trần giá trị đơn vẫn cho phép trả lặp một khoản nhỏ. LogiX có thể mất tiền dù mỗi lệnh riêng lẻ dưới trần. | `write_gate(issue_refund)` đọc `ledger_rows(order_id=...)`, kể cả dòng có sẵn, đối chiếu tổng đã trả với quyền lợi và phạm vi yêu cầu đã xác thực; deny lệnh lặp, giữ khoản hợp lệ đầu tiên. | Không cấm mọi khoản tiếp theo chỉ vì có một dòng cũ; phải xét mô hình quyền lợi thực tế. Cổng đọc-trước-ghi trong mock chưa bảo đảm chống race khi chạy song song; pilot cần idempotency/giao dịch tại nơi ghi. |
| G4 — Lỗi hãng đúng kiện, đúng nguyên nhân và hạn mức. `agent.py:run_ticket`, suy CARRIER khi thiếu cause (dòng 115), `first = parcels[0]` (dòng 194–198); `tools.py:WriteTools.file_carrier_fault`; `helpers.py:carrier_at_fault`. | Gắn lỗi cho kiện/hãng/tài xế đầu tiên dù sự cố thuộc kiện khác; không tự xác thực độ trễ, nguyên nhân ghi nhận và số lỗi hãng trong ngày. Hãng/tài xế có thể bị phạt hoặc treo oan. | `write_gate(file_carrier_fault)` đối chiếu kiện xác thực, `carrier_id`, `driver_id`, độ trễ DB, cause ghi nhận và policy hiệu lực qua `H.carrier_at_fault`; đếm `fault_rows(carrier_id=...)` theo ngày mô phỏng, so `ops_limits().max_auto_strikes_per_carrier_per_day`. Modify khi xác định được đúng kiện; deny lỗi hãng không có căn cứ; ca cần người duyệt trước cả khoản tiền phải phát hiện trước `issue_refund`. | Không suy hãng có lỗi chỉ từ việc khách được hoàn. Tại điểm ghi lỗi hãng, tiền có thể đã ghi; không coi escalate ở đây là ngăn mất tiền. Dữ liệu tracking/cause sai và lịch sử ngoài mock còn là giới hạn. |
| G5 — Payload gửi hãng. `agent.py:run_ticket`, `customer_note=text`, `recipient_contact` ở đơn quà (dòng 199–206); `tools.py:WriteTools.notify_carrier` (dòng 175–187) chỉ lọc tên khóa cấp ngoài nếu config có đặt. | Chữ tự do của khách và thông tin người nhận có thể đi sang bên thứ ba ngoài dữ liệu cần thiết; danh sách chặn hiện trống. Nguy cơ lộ dữ liệu cá nhân. | `write_gate(notify_carrier)` dự kiến tạo payload tối thiểu theo `policy.carrier_notice_fields`; lấy giá trị từ đơn/kiện đã xác thực, đối chiếu đúng hãng và kiểu dữ liệu, bỏ chữ tự do/contact ngoài danh sách bằng modify; allow payload đã khớp. Phối hợp TV4 về mục `legal`, không tự sửa config đó. | Chỉ bỏ một tên trường chưa đủ nếu PII nằm dưới khóa khác; allowlist vẫn phải kiểm nguồn/giá trị. Chặn thông báo không xóa tiền/lỗi hãng đã ghi và không chứng minh tuân thủ pháp lý toàn hệ thống. |

#### Nội dung chuẩn bị gửi nhóm, chưa thay nhóm chốt

- **Câu 1.5/A3:** đề xuất (b): chưa đủ căn cứ nói Y tốt hơn X có ý nghĩa thống kê; mức 1,0 vẫn nằm trong khoảng tin cậy minh họa [0,94; 1,0] của X. Không suy ra hai bản chắc chắn bằng nhau; đây không phải số của nhóm. Để nhóm điền A3.
- **Soát với TV3:** từng điều kiện `decision_rule` phải chỉ rõ bộ/mốc, ngưỡng, đơn vị, hành động và người chịu trách nhiệm; chờ TV3 có bản nháp mới soát được nội dung thực tế. Các khóa ngưỡng ánh xạ tới trường report: `pass_rate`, `pass_k` (đúng cả 5/5), `wrongful_refund_vnd`, `wrongful_carrier_faults`, `pii_leaks`, `escalation_rate`, `cost_per_ticket_vnd`, `roi`, `queue_stuck`. `wrongful_refund_vnd` là tổng cả 5 seed; chỉ số tiền/ngày phải đọc riêng khối `ops`. Chi phí/ticket gồm máy + công duyệt + phí trực; tiền hoàn sai còn bị trừ khi tính ROI. Không đồng nhất ngân sách LLM 1.500đ/ticket với tổng chi phí/ticket.
- **Giới hạn của gate cần TV3/TV2 biết:** `lab10/gate.py:check` bỏ qua ngưỡng null; `main` không đưa `biz_ok` hay `ops.violations` vào điều kiện exit code 0 và không tự áp dụng bốn dòng `decision_rule`. Vì vậy phải đọc cả business_ops, vượt trần, độ phủ và phân khúc; exit code 0 riêng lẻ không đủ để chọn Tiếp tục. Không sửa file gate; nhóm tự quyết theo tiêu chí đã ký.
- **Gửi TV4/pre-mortem:** kỹ thuật — hoàn sai/ghi lặp/lỗi sai hãng (G1–G4); kinh doanh — chuyển người quá nhiều làm chi phí vượt làm tay 10.000đ, hoàn tự động có thể vượt ngân sách Finance 2.000.000đ/ngày; con người/vận hành — một người chỉ duyệt 6 ca/giờ, SLA nhận ca 60 phút, phí trực 30.000đ/người/ca nên chuyển hết hoặc thêm người vô hạn không giải quyết được; pháp lý — hãng/tài xế chịu phạt và dữ liệu người nhận ra ngoài (G4–G5). TV4 chọn MỘT tool để làm HAZOP đủ ≥3 dòng, thêm ≥2 dòng ngoài kỹ thuật; nhóm chọn 2–3 rủi ro, rồi mới gắn mã dòng B4/B6 cho cổng.
- **Nháp B7.2, bước 1:** coi bộ nền đã đọc/chỉnh là dữ liệu phát triển; TV2 chuẩn bị trước hai ticket adhoc mới theo tính chất và giữ kỳ vọng độc lập với kết quả guard. Không đưa ticket ID, order ID, nhãn chấm hoặc câu chữ mẫu vào luật; chốt snapshot vòng 1 trước khi mở đúng thẻ được bốc. Hai ca này là behavioral test bổ sung, không thay thế test ẩn độc lập.
- **Nháp B7.2, bước 2:** khi đến vòng 2, chỉ mở đúng thẻ đã bốc; TV2 đo prepared trước sửa, giữ nguyên snapshot, rồi mỗi lần sửa một nguyên nhân và đo lại thẻ cùng bộ nền. Kết quả thẻ sau khi đã dùng chỉnh cổng phải ghi là kết quả trên dữ liệu đã xem; không suy rộng thành tổng quát hóa. Test ẩn để team chấm chạy sau, không truy tìm/đọc/điều chỉnh theo nó. Chưa điền Phiếu B khi chưa đủ điều kiện vòng 1.
- **Khung demo, chưa có kết quả trước/sau:** “Vấn đề [nhánh và bằng chứng] → cổng [hàm/nhánh thực tế] → nguồn kiểm chứng [bảng/trường] → trước/sau [ticket@seed, mã base/prepared/after do TV2 cung cấp] → giới hạn [DB sai, race, nhánh ngoài code].” Chỉ thay ô bằng kết quả thật; hiện chưa thể trình bày hiệu quả của cổng.

### Bằng chứng

- Repo lúc bắt đầu: nhánh `tv1-guards-vietduc`, HEAD `dedf62ab1fcf70519d0a3a3c71cbe37dfbd01718`, working tree sạch; không đổi nhánh, commit, push hay merge trong lượt này. Danh tính Git local vẫn là leader `2A202603449` / `2A202603449@example.com`; MSSV cá nhân là `2A202603445`.
- Lần chỉnh nhẹ sau review chỉ cập nhật thông tin phân vai trong mục cá nhân này; giữ nguyên bảng thành viên và mục cá nhân người khác, không quy kết ai đã sửa từng dòng.
- Phần đã điền: `templates/form-a-criteria.md`, A2 **chỉ cột Offline**. Không sửa A3/A4, telemetry, phiếu B/C, code hoặc config.
- Kiểm tra thực tế: `python -m unittest discover -s tests` → exit code 0, `Ran 13 tests`, `OK` (Python 3.13.17). Đây là public tests; không phải mã baseline/eval chính thức và không chứng minh không regression trên sự cố/test ẩn.
- Chưa có trace do Codex chạy và chưa nhận report từ TV2. Local không có `config/acceptance_criteria.lock`, `runs/`, `config/round1.lock`, `lab10/guards_round1.py`, `config/operating_gates.round1.json`; tiêu chí còn tên/người ký/decision_rule trống và ngưỡng null, B0/B4/B6 chưa có bằng chứng nhóm chốt. Chưa nhận bằng chứng commit ký/push, mã baseline hay 2–3 dòng rủi ro được chọn để sang B; chưa biết thẻ để sang C. Việc máy TV2 có dữ liệu riêng chưa được xác minh.
- Dùng Codex để đọc repo/code, thiết kế A2, soạn phân tích tĩnh/nội dung gửi nhóm và chạy public tests. Cá nhân cần đọc lại, xác nhận nội dung trước khi commit; chưa có commit/PR hay mã lần chạy mới để khai báo.

### Exit ticket

Để cá nhân tự viết/xác nhận sau khi review, không thay bằng trải nghiệm do AI suy đoán:

- Một điều tôi học được: [tự điền].
- Một điều tôi còn chưa chắc và cách kiểm tra: [tự điền].
