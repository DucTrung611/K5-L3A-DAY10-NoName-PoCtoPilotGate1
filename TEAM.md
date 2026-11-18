# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): NoName
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-NoName-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S5

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
- **Vòng 2, thẻ S5 (chi phí):** C1 đối chiếu base với prepared bằng trace (cổng R3 chặn hoàn trùng `S5-02`, `pilot_scope` cắt kho sỉ `S5-51`, trần chi phí chặn ticket dài `S5-70`; bỏ sót `S5-21` hoàn thiếu 12.000đ và câu trả lời sai "chưa hoàn khoản nào") và mở lại pre-mortem; C4 HAZOP của thẻ trên `issue_refund` (5 dòng, 1 nhánh chưa thấy trên trace: CSKH ghi tay xen giữa lúc cổng đọc sổ và lúc trợ lý ghi); câu 3.3 giả định môi trường (trợ lý là nơi duy nhất ghi sổ, khách gửi một ticket ngắn); C10 risk register 2 dòng; C11 checklist sau sự cố, Runbook 4–5; `submission/submission.json` (team, members, incident, v1).

### Bằng chứng

- Commit: `80d1f41` (config `operations`/`legal`, Phiếu A 1.2, 1.4, Phiếu B B4, B5, B7.5, B7.6) · `726eca5` (B6 pre-mortem, chốt R1–R3) · `30d15e2` (B7.1 cột 1–3).
- Mã lần chạy baseline đối chiếu cho B6/R1: `R-base-before-20261118-154917-611de4` (`T-002@55` hoàn sai 20.000đ, 1 lỗi hãng oan VNX); bằng chứng tại `docs/evidence/R-base-before-20261118-154917-611de4/`.
- Dòng trong phiếu: Phiếu A mục A1 câu 1.2, A2 cột Telemetry; Phiếu B mục B4, B5, B6, B7.5, B7.6; Phiếu C mục C1, C4, C5 (câu 3.3), C10, C11.
- Trace dùng cho Phiếu C (lệnh `lab10.trace`, không ghi nhật ký): `S5-01`, `S5-02`, `S5-03`, `S5-20`, `S5-21`, `S5-51`, `S5-70` @ seed 11, mốc base và prepared.
- **Dùng AI:** dùng Claude Code để đọc `data/world.json`, `lab10/agent.py`, `ops.py`, `tools.py`, soạn nháp các phần trên và kiểm config bằng `lab10.ops.problems` + public tests (`Ran 13 tests … OK`). Mọi con số và tên người do tôi chọn và giải thích được lúc demo; không dùng AI để viết code xử lý theo mã ticket.

### Exit ticket

- Một điều học được: [tự điền]
- Một điều còn chưa chắc: [tự điền]

## LuuVanVietDuc-2A202603445

### Phần việc phụ trách

**TV1 — Kỹ sư cổng: xây biện pháp bảo vệ.** Phụ trách câu 1.3/A2 cột Offline, triển khai R1–R3 trong `lab10/guards.py`, giải thích B7.1 và hai bước tránh leakage tại B7.2; phần code C7 sẽ thực hiện khi đủ bằng chứng vòng 2. TV2 phụ trách các phép đo chính thức.

### Đóng góp cụ thể

- Thiết kế metric A2 cho bước chọn chính sách: nhãn theo khoảng hiệu lực tại ngày giả lập, công thức E/N, nhóm loại trừ, N=0 và điểm mù. Đây là thiết kế metric; không tự gán kết quả đo cho metric này.
- Giai đoạn A đã đọc code, phân tích tĩnh và đề xuất G1–G5. Đó là lịch sử chuẩn bị; quyết định triển khai vòng 1 của nhóm là **R1 → R2 → R3 tại B6**, không phải triển khai toàn bộ G1–G5.
- Triển khai R1: xác thực đơn/chủ đơn/kiện, tính quyền lợi theo tracking và policy hiệu lực, sửa khoản vượt và từ chối quyền lợi bằng 0. Triển khai R2: kiểm đúng kiện/hãng/tài xế/độ trễ/cause và hạn mức lỗi hãng; phát hiện điều kiện chuyển người trước ghi tiền khi cần. Triển khai R3: kiểm ledger, retry, tổng quyền lợi và phê duyệt, giữ các khoản hoàn một phần hợp lệ.
- Code TV1 ở commit `d7efdd3`, merge qua [PR #3](https://github.com/DucTrung611/K5-L3A-DAY10-NoName-PoCtoPilotGate1/pull/3) tại `47f1bcf`. Đã tự thử bằng trace, public tests và kiểm tra trong bộ nhớ trong lượt triển khai; không nhận các lệnh đo chính thức của TV2 là phần việc mình thực hiện.
- B7.1 đã liên kết R1/R2/R3 với B4/B6 và bằng chứng tích hợp. B7.2 được hoàn thiện ở lượt tài liệu này: phân biệt dữ liệu phát triển, bộ S5 đã xem khi dùng chỉnh vòng 2 và test ẩn độc lập.
- B7.3 do **TV2** thực hiện: BT-01 từ chối khoản hoàn không đủ điều kiện, BT-02 sửa 57.000đ xuống 25.000đ và độ trễ 18 xuống 4 ngày; giữ ca hợp lệ xử lý được. Hai ca không thay thế đánh giá S5/test ẩn và không chứng minh mọi nhánh R3.

### Bằng chứng và trạng thái hiện tại

- Lịch sử chuẩn bị: lúc bắt đầu giai đoạn A ở nhánh `tv1-guards-vietduc`, HEAD `dedf62a`, chưa viết guard và chưa nhận baseline. Các ghi nhận đó không còn mô tả trạng thái hiện tại. Danh tính Git dùng MSSV leader theo README; MSSV cá nhân là **2A202603445**.
- Tiêu chí đã ký ở `806ad8c`; baseline TV2 cung cấp là `R-base-before-20261118-154917-611de4`: 109/110 đạt, hoàn sai 20.000đ, một lỗi hãng oan, ca hỏng T-002@55. [Bàn giao baseline](docs/tv1-baseline-handoff.md).
- TV2 đo bản tích hợp `47f1bcf`: `R-base-after-20261118-162239-21c937`, **110/110 đạt**, không ca mới hỏng so baseline trên bộ nền; hoàn sai/lỗi hãng oan/PII đều 0. Đây là kết quả code/config tích hợp, không tách hiệu quả riêng từng thay đổi. [Report after](docs/evidence/R-base-after-20261118-162239-21c937/report.json).
- TV2 đã thực hiện checkpoint tại commit `a49cb34`, hash `6640aec4`, taken_at `2026-11-18T16:42:37` theo lock. Run **base/prepared** `R-base-prepared-20261118-164237-21c937` đạt 110/110; ghi nhận tại `e230d3c`. Giữ nguyên `guards_round1.py`, `operating_gates.round1.json`, `round1.lock`. [Report prepared](docs/evidence/R-base-prepared-20261118-164237-21c937/report.json).
- [BT-01/BT-02 và oracle](docs/evidence/behavioral-round1-47f1bcf/manifest.json), [B7.1/B7.2/B7.3](templates/form-b-evaluation-gates.md), [bàn giao vòng 1](docs/tv1-round1-handoff.md). B8 hiện đã có quyết định v1/PIC của nhóm; lượt này không sửa hoặc ký thay.
- Nhóm được giao S5. Tại lượt kiểm tra tài liệu trên main `0f568c3`, repo chưa có bốn file `incidents/S5/{card.json,card.md,tickets.jsonl,world_patch.json}` và chưa tìm thấy report/run ID/trace **S5/prepared** trong bằng chứng local. **Base/prepared không phải S5/prepared.** Chưa triển khai vòng 2; không suy từ việc thiếu file local rằng nhóm chưa từng xem thẻ.
- Giới hạn: bộ nền đạt và CI trên mock không chứng minh toàn bộ sự cố, test ẩn hoặc production. R1 có bằng chứng trực tiếp T-002@55; các nhánh khác còn phụ thuộc độ đúng của DB, đồng bộ ledger, tải thực và đánh giá sự cố. Rủi ro chạy đồng thời cần kiểm soát tại storage.

### Sử dụng AI

Dùng Codex để đọc code/tài liệu, thiết kế A2, hỗ trợ triển khai và review R1–R3, chạy trace/public tests/kiểm tra trong bộ nhớ, soạn nội dung bàn giao và cập nhật B7.2/mục cá nhân. Các phép đo baseline, after, prepared, behavioral tests chính thức và checkpoint nêu trên do TV2 thực hiện. Cá nhân tự review nội dung và tự xác nhận exit ticket; không dùng AI viết thay trải nghiệm học tập.

### Exit ticket

Để cá nhân tự viết/xác nhận sau khi review, không thay bằng trải nghiệm do AI suy đoán:

- Một điều tôi học được: [tự điền].
- Một điều tôi còn chưa chắc và cách kiểm tra: [tự điền].
