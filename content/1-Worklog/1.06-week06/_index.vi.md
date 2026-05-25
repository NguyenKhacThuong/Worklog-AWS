---
title: "Tuần 06 – Quan sát & Giám sát"
date: 2026-04-20
draft: false
weight: 6
chapter: false
---

## Mục tiêu

* Thiết lập observability cho tài nguyên cloud và dịch vụ triển khai.
* Cấu hình CloudWatch dashboard, log, metric và alarm.
* Sử dụng tracing / giám sát phân tán cho luồng yêu cầu ứng dụng.
* Xem xét chi phí và phát hiện bất thường.

## Công việc (gợi ý theo ngày)

| Ngày | Công việc | Ghi chú |
|------|-----------|---------|
| 1 | Thiết kế dashboard CloudWatch cho tài nguyên chính | CPU, memory, mạng, latency yêu cầu |
| 2 | Tập trung log từ EC2/ECS/Lambda về CloudWatch Logs | Tạo log group và thiết lập retention |
| 3 | Thêm CloudWatch Alarm cho lỗi cao, latency, và ngưỡng chi phí | Kết nối với SNS thông báo |
| 4 | Bật AWS X-Ray hoặc tracing cho gọi dịch vụ | Trực quan hoá đường đi yêu cầu và latency |
| 5 | Kiểm tra Cost Explorer và cấu hình phát hiện bất thường | So sánh chi phí thực tế với dự báo |
| 6 | Ghi chép mẫu observability và bài học rút ra | Lưu lại runbook và cách xử lý |

## Thành tựu

* Xây dựng dashboard tái sử dụng cho tình trạng hạ tầng và ứng dụng.
* Tập trung log và tạo cảnh báo cho các sự cố quan trọng.
* Triển khai tracing / giám sát phân tán để nắm rõ hành trình yêu cầu.
* Xác định xu hướng chi phí và bật giám sát bất thường.

## Ghi chú

Tham khảo: https://cloudjourney.awsstudygroup.com/