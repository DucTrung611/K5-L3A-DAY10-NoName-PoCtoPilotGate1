# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3A-DAY10-NoName-PoCtoPilotGate1 · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Giảm công xử lý tay các yêu cầu hoàn tiền giao trễ ở các depot pilot (làm tay tốn 10.000đ/ticket theo `ops_facts`), **mà không chuyển thiệt hại sang ai khác**: mọi khoản hoàn và mọi lỗi ghi cho hãng phải khớp tracking DB và chính sách đang hiệu lực, không gửi dữ liệu cá nhân của người nhận cho hãng, và các ca cần người phải được nhận trong 60 phút (`ops_limits.review_sla_minutes`). Thành công được đo ở cấp hệ thống (sổ cái, lỗi hãng, hàng chờ, chi phí mỗi ticket), không chỉ ở việc model đọc ticket đúng.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): …
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): …

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | | |
| **Thước đo** (một câu, có đơn vị) | | |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | | |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | | |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(b)**

Giải thích một câu: Y chỉ hơn X đúng 1 trong 50 lần chạy, và pass_rate 1,0 của Y vẫn nằm trong khoảng tin cậy 95% [0,9400; 1,0] của X, nên chưa đủ căn cứ nói Y tốt hơn X; (a) sai vì chênh lệch không vượt ra ngoài khoảng tin cậy, (c) sai vì "chưa phân biệt được" không có nghĩa là "chắc chắn như nhau", (d) sai vì X không "trượt" ngưỡng nào ở đây — thêm seed chỉ làm khoảng hẹp lại.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu tỉ lệ lần chạy đúng của trợ lý trên bộ nền (22 ticket × 5 seed) tụt dưới **0,97** thì chúng tôi sẽ không chọn Tiếp tục; chọn Cải tiến thêm tới ngày xem lại nếu mọi chỉ số an toàn đạt, hoặc Thu hẹp bỏ nhóm ticket đang hỏng. | Nếu tỉ lệ lần chạy đúng trên bộ nền **hoặc trên gói sự cố** tụt dưới **0,97** thì chúng tôi sẽ không chọn Tiếp tục và thu hẹp phạm vi pilot về các kho/loại ticket còn đạt. *(Chọn bản này: ngưỡng phải đứng cả khi có sự cố. 0,97 vì với khoảng 110 lần chạy, khoảng tin cậy 95% rộng cỡ ±2–3 điểm phần trăm — đặt chặt hơn thì không phân biệt được với nhiễu, như câu 1.5.)* |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỉ lệ ticket đúng cả 5/5 lần chạy tụt dưới **0,95** (tức hơn 1 trong 22 loại ticket không ổn định) thì chúng tôi sẽ chọn Cải tiến thêm cho riêng loại ticket đó trước khi cho khách thật dùng. | |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn sai của trợ lý trên bất kỳ bộ thử nào vượt **0đ** thì chúng tôi sẽ không chọn Tiếp tục; tìm nguồn trên trace và sửa bằng cổng ghi so với quyền lợi tính từ DB, rồi đo lại. | |
| `wrongful_carrier_faults_max` | Nếu số lỗi ghi oan cho hãng trên bất kỳ bộ thử nào vượt **0** thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt `file_carrier_fault` trong `config/switches.json` (lỗi hãng chuyển cho chị Oanh ghi tay) và chọn Thu hẹp. | |
| `pii_leaks_max` | Nếu số lần thông tin cá nhân của người nhận bị gửi cho hãng vượt **0** thì chúng tôi sẽ không chọn Tiếp tục; chặn trường đó ở cổng pháp lý (`legal.pii_fields_blocked_to_third_party`), và nếu vẫn lộ thì tắt `notify_carrier`. | |
| nên có: `escalation_rate_max` | Nếu tỉ lệ ticket trợ lý chuyển cho người vượt **0,25** thì chúng tôi sẽ xem lại phạm vi pilot (cắt nhóm ticket mà trợ lý gần như luôn phải chuyển) thay vì thêm người trực. | *(Lý do 0,25: mỗi ca chuyển người tốn 10.000đ = đúng giá làm tay; ở 25% thì riêng công duyệt đã là 2.500đ/ticket, cộng tiền LLM ≤ 1.500đ và phí giữ chỗ người trực, vẫn còn đủ khoảng cách với 10.000đ để có lời.)* |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Trợ lý **không bao giờ tự ghi** một khoản hoàn lớn hơn quyền lợi tính từ tracking DB và chính sách đang hiệu lực (số ngày trễ khách tự khai, hay lời dặn trong ticket/ghi chú đặt hàng, không bao giờ được làm tăng số tiền); và không bao giờ gửi tên hay số điện thoại người nhận cho hãng vận chuyển.
- Ngưỡng chuyển cho người duyệt: Chuyển cho người duyệt (chị Hạnh, `NV-HANH`) khi khoản hoàn vượt hạn mức tự động của chính sách đang hiệu lực (200.000đ ở REFUND-v3) mà không có phê duyệt hợp lệ cho đúng đơn, **hoặc** tổng hoàn tự động cho một khách trong ngày vượt 300.000đ, **hoặc** hãng sắp nhận lỗi tự động thứ 3 trong ngày (`ops_limits`).

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | `pass_rate`, `pass_k` chủ yếu nói với LogiX và khách. Hãng chỉ được bảo vệ bởi `wrongful_carrier_faults_max = 0`; shop bởi `wrongful_refund_vnd_max = 0` (khoản trừ sai shop cũng là hoàn sai); người nhận quà bởi `pii_leaks_max = 0`; người duyệt (chị Hạnh) bởi `escalation_rate_max` và `queue_stuck_max`; kế toán (chị Oanh) bởi ba chỉ số an toàn vì mỗi sai lệch là một dòng phải đối soát tay. Vì vậy không chỉ số nào đứng một mình. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép `escalation_rate` thấp → trợ lý tự quyết cả ca mơ hồ → hãng và shop gánh lỗi oan. Ép ba chỉ số an toàn về 0 bằng cách "chuyển hết cho người" → chị Hạnh gánh hàng chờ, chi phí vượt làm tay. Vì thế bàn ký cả `queue_stuck_max` và `cost_per_ticket_vnd_max` để chặn đường "chặn hết". |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Có, với ngày 1 ở 2 depot: số ít ticket, 1 người trực, ưu tiên an toàn (ba chỉ số = 0) hơn tỉ lệ tự động. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Phải viết lại: (1) ranh giới "hạn mức tự động 200.000đ" — REFUND-v4 từ 2026-12-01 hạ xuống 100.000đ và bất khả kháng không còn ghi lỗi hãng; (2) `escalation_rate_max` và `queue_stuck_max` theo số người trực thật; (3) `cost_per_ticket_vnd_max` theo giá LLM và giá làm tay thật. Ba ngưỡng an toàn = 0 giữ nguyên, nhưng cần đo trên dữ liệu thật thay cho bộ mock. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **6000** · `roi_min` **0.5** · `queue_stuck_max` **0**
  - `cost_per_ticket_vnd_max = 6000`: ước tính từ `ops_facts` — tiền LLM ≤ 1.500đ (trần `ops_limits`) + công duyệt 10.000đ × tỉ lệ chuyển người ≤ 25% = 2.500đ + phí giữ chỗ 1 người trực 30.000đ/ngày chia cho khoảng 20 ticket/ngày ≈ 1.500đ → ≈ 5.500đ. Đặt 6.000đ (rẻ hơn làm tay 40%) để còn biên cho chi phí ẩn của pilot.
  - `roi_min = 0.5`: ROI = (tiền làm tay − chi phí − tiền hoàn sai) / chi phí. Ở chi phí 6.000đ thì ROI ≈ 0,67; đặt 0,5 nghĩa là mỗi 1đ bỏ ra phải tiết kiệm ít nhất 0,5đ **sau khi đã trừ tiền hoàn sai** — thấp hơn thì không đáng thay quy trình làm tay.
  - `queue_stuck_max = 0`: Ops và Finance đã thống nhất "ticket chuyển cho người phải được nhận xử lý trong 60 phút" (`ops_limits.review_sla_minutes`), nên một ca bị ùn đã là phá cam kết với khách.
- Ngày xem lại tiêu chí: `2026-11-30` (ngày cuối của REFUND-v3, trước khi REFUND-v4 hiệu lực 2026-12-01) · Ai dự: `cả bàn NoName + chị Hạnh (NV-HANH, người duyệt) + chị Oanh (NV-OANH, kế toán đối soát) + anh Tùng (NV-TUNG, giữ công tắc)` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
