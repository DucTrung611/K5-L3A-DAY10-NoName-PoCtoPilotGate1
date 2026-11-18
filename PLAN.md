# Kế hoạch và chia việc · LAB 10 · Bàn NoName

Repo: `K5-L3A-DAY10-NoName-PoCtoPilotGate1` (giá trị `team` trong tiêu chí và `submission.json` phải ghi **y hệt** tên này).

Đề đầy đủ: [README.md](README.md), [problem-set.md](problem-set.md), [RUBRIC.md](RUBRIC.md). File này chỉ để bàn biết **ai làm gì, lúc nào**.

## 1. Bốn người, ba vai

| Người | Vai | Phụ trách chính | File được sửa |
|---|---|---|---|
| **P1** (trưởng nhóm, chủ repo) | Kỹ sư cổng 1 (chính) | Chạy lệnh, git (ký, chốt, push), code cổng `guards.py`, câu 1.3, 2.1, 2.6, 2.7 | `lab10/guards.py`, `config/acceptance_criteria.json` (chỉ bấm ký) |
| **P2** | Kỹ sư cổng 2 | Đọc trace, bảng soát lỗi, behavioral test, chỉ số theo dõi `monitors.py`, câu 2.2, 2.8, 3.1, 3.6 | `lab10/monitors.py` |
| **P3** | Sản phẩm và kinh doanh | Tiêu chí và ký, bản đồ dữ liệu, cổng `business`, quyết định v1/v2, câu 1.1, 1.5, 1.6, 2.3, 2.9, 3.2, C12 | `config/acceptance_criteria.json`, `config/operating_gates.json` → `business` |
| **P4** | Vận hành và pháp lý | Mục tiêu 2 người, telemetry, HAZOP, checklist 9 nhóm, cổng `operations`/`legal`, runbook, bài nộp, câu 1.2, 1.4, 2.4, 2.10, 3.3, 3.7 | `config/operating_gates.json` → `operations`, `legal`; `submission/submission.json` |

Cả bàn cùng làm: câu 1.5, 2.5 (pre-mortem), 3.0, 3.4 (fault tree), quyết định v1 và v2.

**Luật làm việc với git:** chỉ P1 commit/push các mốc quan trọng (ký, chốt vòng 1). Người khác sửa phiếu thì mỗi người một mục, pull trước khi push để tránh xung đột. Tuyệt đối **không mở rồi lưu** `config/acceptance_criteria.json` sau khi ký.

## 2. Trước buổi / phút 0–15 · Cài đặt

| Việc | Ai |
|---|---|
| Repo để **Private**, mời tài khoản team chấm quyền Read, mời P2–P4 | P1 |
| Mỗi người clone repo, chạy `git remote add upstream https://github.com/VinUni-AI20k/K5_L3_Day10_PoC-to-Pilot_Gate1_student.git` | Mọi người |
| `git config user.name "<MSSV trưởng nhóm>"`, `git config user.email "<MSSV>@example.com"` | Mọi người |
| `python -m unittest discover -s tests` → `Ran 13 tests … OK` | Mọi người |
| Điền bảng thành viên `TEAM.md` (Họ tên, MSSV, vai) | P1 |
| Chọn eval card + PRD v1.1 từ Lab 9 làm bản chung | P3 |

## 3. Khối 1 · phút 15–65 · Phiếu A · **CHƯA chạy `lab10.eval`**

| Phút | P1 | P2 | P3 | P4 |
|---|---|---|---|---|
| 15–20 | Đọc `lab10/helpers.py`, `guards.py`, `data/world.json` | Như P1 | **1.1** mục tiêu hệ thống (A1) | **1.2** mục tiêu chị Oanh + chị Hạnh (A1) |
| 20–35 | **1.3** offline metric cho MỘT bước (A2, cột Offline) | Hỗ trợ 1.3, đọc `ops_facts` cho P3 | Nháp ngưỡng `business_ops` từ `ops_facts` | **1.4** telemetry production (A2, cột phải) |
| 35–40 | **1.5** cả bàn (A3) | | | |
| 40–60 | Soát `decision_rule` khớp với cổng sẽ viết | Soát 4 câu hỏi (A4 bước 2) | **1.6** câu "Nếu … thì …", ranh giới đầu ra, điền `acceptance_criteria.json` | Viết `stop_condition`, soát góc ai thiệt / bên thứ ba |
| 60–65 | **Ký**: `python -m lab10.criteria sign` → commit + push đúng lệnh máy in | | Điền A5 (giờ ký, mã commit) | |

Số tham khảo khi chọn ngưỡng (`data/world.json`): làm tay 10.000đ/ticket; trần LLM 1.500đ/ticket; ngân sách hoàn tự động 2.000.000đ/ngày; trần 300.000đ/khách/ngày; SLA duyệt 60 phút; 1 người duyệt 6 ca/giờ. **Không chép ngưỡng từ file example** (bị trừ điểm C1).

## 4. Khối 2A · phút 65–85 · Phiếu B (chưa sửa code/config)

| Phút | P1 | P2 | P3 | P4 |
|---|---|---|---|---|
| 65–75 | **2.1**: `eval --suite base --stage base --note "baseline"` → `gate --run …`; điền B0 dòng 1, B1 | **2.2**: `trace --suite base --ticket T-002 --seed 55`; bảng soát lỗi B2 | **2.3** bản đồ dữ liệu + ví dụ drift (B3) | **2.4** HAZOP vòng 1 (B4, ≥ 3 dòng + ≥ 2 dòng ngoài kỹ thuật) + checklist 9 nhóm (B5, **mỗi dòng 1 PIC có tên**) |
| 75–85 | **2.5** pre-mortem cả bàn (B6): đủ 4 lăng kính, chọn 2–3 lý do thành cổng | | | |

## 5. Khối 2B · phút 85–105 · cổng phòng ngừa

| P1 | P2 | P3 | P4 |
|---|---|---|---|
| **2.6** code 2–3 cổng trong `guards.py` theo pre-mortem/HAZOP (B7.1). Chạy `eval --suite base --stage after` + unittest, **không được làm hỏng ca đang đúng** | **2.8** behavioral test: 1 tính chất + 2 ticket hiểm bằng `trace --adhoc` (B7.3). Cùng P1 soát trace sau khi có cổng | **2.9** điền `business` trong `operating_gates.json` + lý do có số (B7.4) | **2.10** điền `operations`, `legal` (B7.5); runbook 1–3 + Giờ cao điểm (B7.6) **khớp con số trong config** |
| **2.7** hai bước tránh rò rỉ dữ liệu (B7.2) | | | |

Gợi ý cổng: không viết theo mã ticket hay câu chữ cụ thể (test ẩn sẽ bắt); dựa vào nguồn sự thật (`H.db_delay_days`, `H.entitlement_vnd`, `H.carrier_at_fault`, `ctx.tools.ops_limits()`). Đừng "cho chắc thì chuyển người": hàng chờ và chi phí cũng được chấm.

## 6. Chốt vòng 1 · phút 105–115

1. P1: `python -m lab10.checkpoint` (máy in `ĐÃ CHỐT …`) → `eval --suite base --stage prepared` → `gate --run …`.
2. Cả bàn quyết định **v1**; P3 điền cột v1 ở B8 (ba bằng chứng có mã lần chạy, dòng `decision_rule`, kho/hãng xấu nhất, ngày quyết định lại).
3. P1 commit + push đúng lệnh ở cuối B8. Không ai sửa `guards_round1.py`, `operating_gates.round1.json`, `round1.lock`.

## 7. Khối 3 · phút 125–200 · Phiếu C (thẻ sự cố)

| Phút | P1 | P2 | P3 | P4 |
|---|---|---|---|---|
| 125–135 | `git pull --no-rebase --no-edit --allow-unrelated-histories -X ours upstream main`; `python -m lab10.grade --incident Sx` **trước khi sửa** | Đọc `incidents/Sx/card.md` | Ghi `Thẻ đã bốc:` (Phiếu C), điền C0 | **3.0** C1: cổng vòng 1 đỡ gì, mở lại pre-mortem |
| 135–155 | Trace ≥ 2 ticket hỏng khác kiểu | **3.1** C2 bảng soát lỗi (≥ 2 nguồn khác nhau, ≥ 1 lỗi chìm) | **3.2** specification (C5) | C3 phần riêng theo thẻ; C4 HAZOP thẻ (≥ 3 dòng); **3.3** giả định môi trường (C5) |
| 150–155 | **3.4** fault tree trước khi sửa (C6), cả bàn; mỗi lá có ticket@seed | | | |
| 155–180 | **3.5** sửa `guards.py` cho nguyên nhân kỹ thuật; chạy `eval --suite Sx --stage after`, `eval --suite base --stage after`, `grade` | **3.6** thêm hàm vào `monitors.py`, đăng ký `MONITORS`; điền C8 | Sửa `business` nếu nguyên nhân là tiền/phạm vi; C7 | Sửa `operations`/`legal` nếu nguyên nhân là người/pháp lý; C7 |
| 180–185 | Kiểm report có `monitor ✅`, `regression ✅` | C9 fault tree sau khi sửa | | **3.7** C10 risk register, C11 checklist + runbook 4–5 |
| 185–200 | Chạy lệnh 7 | | **Quyết định v2** C12 + ba dòng bắt buộc | Điền `submission/submission.json` (`members` dạng `HoVaTen-MSSV`), chạy `python -m lab10.check_submission --collect` tới `ĐỦ THÀNH PHẦN` |

Chỉ một thay đổi mỗi lần chạy, ghi rõ trong `--note`.

## 8. Demo và nộp · phút 200–240

- Demo: P1 chiếu ba cột `base · prepared · after`; P3 trình bày quyết định v2; P2 chạy ticket hiểm; P4 trả lời phần người/quy trình.
- Sau demo: trả mọi con số đã đổi thử về bản v2, chạy lại `grade` và lệnh 7.
- P1 push lần cuối (README mục 6). **Mỗi người** viết mục cá nhân + exit ticket trong `TEAM.md` và **tự nộp link repo trên LMS**.

## 9. Năm điều không được quên (sai là bài không được tính)

1. Ký tiêu chí và push **trước** lần `eval` đầu tiên.
2. Không sửa `acceptance_criteria.json` sau khi ký; không sửa bản chụp vòng 1; không sửa file bị khoá.
3. Không xử lý riêng theo mã ticket hay câu chữ.
4. Không chọn **Tiếp tục** khi report còn vượt trần hoặc còn ngưỡng đã ký chưa đạt.
5. `team` = `K5-L3A-DAY10-NoName-PoCtoPilotGate1`; `members` khớp `TEAM.md`.

## 10. Todo list theo từng người

Đánh dấu `[x]` khi xong. Dòng có ⛔ là điểm chặn: cả bàn chờ việc đó xong mới đi tiếp.

### P1 · Kỹ sư cổng chính (trưởng nhóm)

**Cài đặt**
- [ ] Repo Private, mời team chấm (Read) và P2–P4
- [ ] Gắn `upstream`, đặt `user.name`/`user.email` (MSSV, email giả), test `Ran 13 tests OK`
- [ ] Điền bảng thành viên `TEAM.md`

**Vòng 1**
- [ ] Câu 1.3: offline metric cho MỘT bước (Phiếu A, A2 cột Offline)
- [ ] ⛔ Ký: `python -m lab10.criteria sign` → commit + push đúng lệnh máy in (sau khi P3 điền xong tiêu chí)
- [ ] Câu 2.1: `eval --suite base --stage base --note "baseline"` → `gate --run …`; điền B0 dòng 1, B1
- [ ] Câu 2.6: code 2–3 cổng trong `lab10/guards.py` (theo lý do pre-mortem đã chọn); `eval --stage after` + unittest; điền B7.1
- [ ] Câu 2.7: hai bước tránh rò rỉ dữ liệu (B7.2)
- [ ] ⛔ `python -m lab10.checkpoint` → `eval --stage prepared` → `gate`; điền B0 dòng 2–3 (sau khi P3, P4 điền xong config)
- [ ] Commit + push lệnh cuối B8

**Vòng 2**
- [ ] ⛔ `git pull … upstream main`; `python -m lab10.grade --incident Sx` TRƯỚC khi sửa
- [ ] Trace ≥ 2 ticket hỏng khác kiểu, chuyển kết quả cho P2
- [ ] Câu 3.5: sửa `guards.py` cho nguyên nhân kỹ thuật; chạy `eval --suite Sx --stage after`, `eval --suite base --stage after`, `grade`; điền C0, phần code ở C7
- [ ] Kiểm report có `integrity ✅`, `visible ✅`, `regression ✅`, `monitor ✅`
- [ ] Push lần cuối; viết mục cá nhân + exit ticket trong `TEAM.md`; nộp link LMS

### P2 · Kỹ sư cổng 2

**Vòng 1**
- [ ] Đọc `lab10/helpers.py`, `guards.py`, `data/world.json`; hỗ trợ P1 câu 1.3
- [ ] Soát 4 câu hỏi của tiêu chí (Phiếu A, A4 bước 2)
- [ ] Câu 2.2: `trace --suite base --ticket T-002 --seed 55`; bảng soát lỗi B2 (3 phần)
- [ ] Câu 2.8: 1 tính chất + 2 ticket hiểm chạy bằng `trace --adhoc`; dán kết quả vào B7.3
- [ ] Soát trace sau khi có cổng: không ca đang đúng nào bị hỏng

**Vòng 2**
- [ ] Câu 3.1: bảng soát lỗi của thẻ C2 (≥ 2 lỗi nguồn khác nhau, ≥ 1 lỗi chìm), ghi tác hại
- [ ] Câu 3.6: thêm hàm mới vào `lab10/monitors.py`, đăng ký `MONITORS`; điền C8 (ba ô + giá trị nền/thẻ)
- [ ] Câu 3.7 (phần cây): fault tree SAU khi sửa (C9)
- [ ] Demo: chạy ticket hiểm khi bàn kia phản biện
- [ ] Viết mục cá nhân + exit ticket trong `TEAM.md`; nộp link LMS

### P3 · Sản phẩm và kinh doanh

**Vòng 1**
- [ ] Chọn eval card + PRD v1.1 từ Lab 9 làm bản chung
- [ ] Câu 1.1: mục tiêu cấp hệ thống (A1)
- [ ] Câu 1.6: câu "Nếu … thì …" cho từng chỉ số, hai câu ranh giới đầu ra, bước 3 (A4)
- [ ] Điền `config/acceptance_criteria.json`: `team`, `signed_by`, 5 ngưỡng `required`, `escalation_rate_max`, `business_ops`, `stop_condition`, 4 dòng `decision_rule` (KHÔNG chép example)
- [ ] Điền A5 (giờ ký, mã commit) sau khi P1 ký
- [ ] Câu 2.3: bản đồ dữ liệu + ví dụ drift (B3)
- [ ] Câu 2.9: điền `operating_gates.json` mục `business` + lý do có số (B7.4)
- [ ] Quyết định v1: điền cột v1 ở B8 (3 bằng chứng có mã lần chạy, dòng `decision_rule`, kho/hãng xấu nhất, ngày quyết định lại)

**Vòng 2**
- [ ] Ghi `Thẻ đã bốc:` đầu Phiếu C
- [ ] Câu 3.2: specification (C5)
- [ ] Câu 3.5 (phần tiền/phạm vi): sửa `business` nếu cần; điền dòng tương ứng C7
- [ ] Quyết định v2: C12 (cột v2, mục "Chỉ ở v2", ba dòng bắt buộc) — không chọn Tiếp tục nếu còn vượt trần
- [ ] Demo: trình bày quyết định v2 và con số đỡ cho nó
- [ ] Viết mục cá nhân + exit ticket trong `TEAM.md`; nộp link LMS

### P4 · Vận hành và pháp lý

**Vòng 1**
- [ ] Câu 1.2: mục tiêu chị Oanh và chị Hạnh (A1)
- [ ] Câu 1.4: telemetry production (A2 cột phải, có khung thời gian + ngưỡng báo động)
- [ ] Viết nháp `stop_condition` cho P3
- [ ] Câu 2.4: HAZOP vòng 1 (B4, ≥ 3 dòng + ≥ 2 dòng ngoài kỹ thuật)
- [ ] Câu 2.4: checklist 9 nhóm việc (B5), mỗi dòng 1 PIC có tên
- [ ] Câu 2.10: điền `operating_gates.json` mục `operations` (`pic`, `approver_id`, `reviewers_on_shift`, `review_capacity_per_hour`, `max_queue_wait_minutes`, `stop_conditions`, `alert_channel`) và `legal`
- [ ] Runbook 1–3 (B7.5) và Giờ cao điểm (B7.6), số khớp config

**Vòng 2**
- [ ] Câu 3.0: C1 (cổng vòng 1 đỡ gì, mở lại pre-mortem)
- [ ] C3 phần riêng theo thẻ; C4 HAZOP của thẻ (≥ 3 dòng)
- [ ] Câu 3.3: giả định môi trường (C5)
- [ ] Câu 3.5 (phần người/pháp lý): sửa `operations`/`legal` nếu cần; điền dòng tương ứng C7
- [ ] Câu 3.7: risk register C10, cập nhật checklist C11, runbook 4–5
- [ ] Điền `submission/submission.json` (`members` dạng `HoVaTen-MSSV`); chạy `python -m lab10.check_submission --collect` tới `ĐỦ THÀNH PHẦN`
- [ ] Viết mục cá nhân + exit ticket trong `TEAM.md`; nộp link LMS

### Cả bàn (cùng ngồi)

- [ ] Câu 1.5: chọn kết luận về khoảng tin cậy (A3)
- [ ] Câu 2.5: pre-mortem 4 lăng kính, chọn 2–3 lý do thành cổng (B6)
- [ ] Chốt quyết định v1
- [ ] Câu 3.4: fault tree TRƯỚC khi sửa (C6), mỗi lá có bằng chứng
- [ ] Chốt quyết định v2
- [ ] Demo ba mốc; sau demo trả số về bản v2, chạy lại `grade` + lệnh 7
