# S5 · Bàn giao prepared cho TV1 · chưa sửa vòng 2

> Đã có bản sửa R3 vòng 2 và kết quả mới: [bàn giao sau sửa](s5-round2-handoff.md). Những lỗi còn lại và kết luận FAIL vì visible bên dưới là lịch sử trước sửa; bản mới visible đã đạt, vẫn còn vấn đề integrity bộ phát.

> Lần grade mới nhất theo yêu cầu: `R-S5-grade-20261118-171815-6f5ec8`, đo commit `3a2acdc`; [report](evidence/R-S5-grade-20261118-171815-6f5ec8/grade-report.json). Kết quả không đổi vì chưa sửa guards/config: visible và integrity chưa đạt, criteria/regression/monitor đạt. Đây là chạy lại, không phải cải tiến vòng 2. Các số chi tiết bên dưới thuộc lần đo đầu để giữ nguồn bằng chứng.

- Commit đã đo: `5d9cc814cd8cf802e8105ceb93bad4edd4295818`; code/config vòng 1 khớp bản đóng băng hash `6640aec4`.
- Lần grade đầu sau nhận thẻ: `R-S5-grade-20261118-171201-6f5ec8` · kết luận **FAIL**, không gọi là PASS.
- [Report JSON](evidence/R-S5-grade-20261118-171201-6f5ec8/grade-report.json) · [Report Markdown](evidence/R-S5-grade-20261118-171201-6f5ec8/grade-report.md) · [Nhật ký](evidence/R-S5-grade-20261118-171201-6f5ec8/journal.jsonl).
- S5/base `R-S5-before-20261118-171201-6f5ec8`; S5/prepared `R-S5-prepared-20261118-171202-6f5ec8`; S5/after ban đầu `R-S5-after-20261118-171202-6f5ec8`. Report từng mốc nằm cùng thư mục evidence theo run ID.
- Monitor C8 có từ trước khi pack tới; guards/config chưa sửa vòng 2. After ban đầu bằng prepared, không phải bằng chứng đã cải tiến.

| Chỉ số | S5 base | S5 prepared |
|---|---|---|
| Lượt đạt / tổng | 125/150 | 85/90 |
| pass_rate và CI95 | 0,8333 [0,7;0,9667] | 0,9444 [0,8333;1,0] |
| pass_k | 0,8333 | 0,9444 |
| Hoàn sai / lỗi hãng oan | 890.000đ / 20 | 0đ / 0 |
| Hoàn thiếu (5 seed) | 0đ | 60.000đ |
| Chi phí/ticket; ROI | 6.083đ; -0,33 | 3.891đ; 1,57 |
| Ròng/ngày trong phạm vi mô phỏng | -60.486đ | 109.957đ |
| LLM lớn nhất/ticket | 2.412đ | 664đ |
| Coverage; ticket ngoài scope/ngày | 100%; 0 | 60%; 12 |
| Monitor kho cao nhất (proxy) | 20.262,6đ | 4.214,25đ |

Tiền hoàn sai/thiếu là tổng qua 5 seed; số tiền chi phí/lợi ích ngày là trung bình theo mô phỏng. Mẫu prepared khác base vì scope loại HCM-B2B. 12 ticket/ngày đó vẫn cần làm tay; chưa chứng minh tổng hiệu quả trên mọi kho sau thu hẹp. Bộ nền sau có cổng vẫn 110/110, không regression.

## Lỗi cần TV1 sửa ở guards hiện tại

**S5-21@11 prepared**: quyền lợi 22.000đ, ledger_seed đã trả tay 10.000đ; agent đề xuất 22.000đ, R3 thấy 10.000 + 22.000 > 22.000 nên deny. Khách đáng được nhận thêm **12.000đ**. Đây là toàn bộ 5 lỗi còn lại (một ticket, 5 seed), không phải 5 nguyên nhân.

- [Trace prepared](evidence/R-S5-grade-20261118-171201-6f5ec8/S5-21@11-prepared.txt) · [JSON](evidence/R-S5-grade-20261118-171201-6f5ec8/S5-21@11-prepared.json).
- [Trace base](evidence/R-S5-grade-20261118-171201-6f5ec8/S5-21@11-base.txt): trả dư 22.000đ thay vì 12.000đ.
- Hướng kiểm tra tổng quát: tính quyền lợi còn lại từ ledger, phân biệt đã trả đủ/hoàn một phần, điều chỉnh khoản đề xuất trong phạm vi còn lại, rồi kiểm phê duyệt và hạn mức trên khoản thực trả. Không dùng ID hoặc câu chữ để rẽ nhánh.
- Sau sửa: cần refunded 12.000đ, fault MKD/O-2521-P1 và lời trả khớp ledger. Giữ S5-02/S5-20 không trả thêm, không phá bộ nền.

## Các nguồn lỗi khác loại và cổng vòng 1 đã đỡ

- **Hoàn trùng qua ticket khác cùng ngày:** [S5-02 base](evidence/R-S5-grade-20261118-171201-6f5ec8/S5-02@11-base.txt) trả thêm 25.000đ sau S5-01; [prepared](evidence/R-S5-grade-20261118-171201-6f5ec8/S5-02@11-prepared.txt) deny đúng.
- **CSKH tay và agent cùng ghi:** [S5-20 base](evidence/R-S5-grade-20261118-171201-6f5ec8/S5-20@11-base.txt) hoàn thêm 20.000đ dù ledger_seed đã trả đủ; [prepared](evidence/R-S5-grade-20261118-171201-6f5ec8/S5-20@11-prepared.txt) deny đúng. Không nhầm với S5-21 còn phần thiếu hợp lệ.
- **Kho sỉ AI đọc xong vẫn phải duyệt:** [S5-51 base](evidence/R-S5-grade-20261118-171201-6f5ec8/S5-51@11-base.txt) escalated sau đề xuất 230.000đ vượt auto_limit, tốn 565đ máy; nhãn xử lý vẫn pass, lỗi ở kinh tế. Toàn HCM-B2B tốn 11.326đ/ticket; prepared loại khỏi scope, không tuyên bố đã sửa tự động hoá kho này.
- **Ticket dài:** [S5-70 base](evidence/R-S5-grade-20261118-171201-6f5ec8/S5-70@11-base.txt) tốn 2.018đ; [prepared](evidence/R-S5-grade-20261118-171201-6f5ec8/S5-70@11-prepared.txt) budget 1.200đ chuyển người trước đọc, chỉ tốn 200đ máy. [S5-50 base](evidence/R-S5-grade-20261118-171201-6f5ec8/S5-50@11-base.txt) tốn 1.856đ, vừa dài vừa kho sỉ.

Các trace base có nhãn pass vẫn có thể vượt trần vận hành. Không trình bày chúng như lỗi nhãn agent. CLI trace adhoc/single ticket không mô phỏng queue tổng ngày; số tổng dùng grade report.

## Kết quả monitor C8

`monitor ✅`: bộ nền before/after 4.586,4đ; S5 base 20.262,6đ, prepared/after 4.214,25đ. Monitor phát tín hiệu ở cả so sánh before lẫn after. Không dùng nhãn để tính. Proxy không thấy ledger_seed manual hoặc hoàn thiếu, không thay thế under_refund_vnd trong offline report.

## Integrity và điều kiện Gate 1 còn thiếu

`criteria ✅`, `regression ✅`, `monitor ✅`; `visible ❌` do S5-21. Pass_rate 0,9444 < 0,97 và pass_k 0,9444 < 0,95: **chưa đủ căn cứ Tiếp tục**, dù chưa vượt trần chi phí.

`integrity ❌` chỉ do thiếu 28 file gói S1/S2/S3/S4/S6/S7/S8 trong manifest. Bốn file S5 và tất cả file khóa đang có đều khớp hash. Không sửa MANIFEST để bỏ qua; cần Coach cung cấp bộ phát đầy đủ/giải quyết cách kiểm scope. Chưa mở nội dung thẻ khác, chưa có test ẩn.

Phiếu C đã điền phần TV2: C0, C1 dữ kiện, C2, C5 specification, C6 và giá trị C8. TV4 tiếp tục C4/giả định môi trường/risk register/runbook; TV3 tiếp tục quyết định/phạm vi. C7/C9 chỉ điền kết quả sau sửa thực tế. Giữ nguyên snapshot vòng 1 và tiêu chí đã ký.
