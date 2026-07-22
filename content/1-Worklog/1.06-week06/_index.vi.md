---
title: "Quan sát và Giám sát"
date: 2026-04-20
draft: false
weight: 6
chapter: false
pre: " <b> Tuần 06: </b> "

---

## Mục tiêu

* Thiết lập observability cho tài nguyên cloud và các dịch vụ đang triển khai.
* Cấu hình CloudWatch dashboard, log, metric và alarm.
* Sử dụng tracing và giám sát phân tán để hiểu luồng yêu cầu ứng dụng.
* Theo dõi chi phí và phát hiện bất thường sớm hơn.

## Công việc đề xuất

| Ngày | Công việc | Ghi chú |
|------|-----------|---------|
| 1 | Thiết kế dashboard CloudWatch cho các tài nguyên quan trọng | Tập trung vào CPU, bộ nhớ, mạng và latency |
| 2 | Tập hợp log từ EC2, ECS hoặc Lambda vào CloudWatch Logs | Tạo log group và thiết lập retention |
| 3 | Thêm CloudWatch alarm cho lỗi cao, latency và ngưỡng chi phí | Kết nối với SNS để thông báo |
| 4 | Bật AWS X-Ray hoặc distributed tracing cho các gọi dịch vụ | Trực quan hóa tuyến đường yêu cầu và điểm nghẽn |
| 5 | Xem xét AWS Cost Explorer và cấu hình phát hiện bất thường | So sánh chi phí thực tế với dự báo |
| 6 | Ghi chép các mẫu observability và bài học kinh nghiệm | Lưu lại runbook và hành động tiếp theo |

## Thành tựu chính

* Xây dựng dashboard có thể tái sử dụng cho hạ tầng và ứng dụng.
* Tập hợp log và tạo cảnh báo cho các sự cố quan trọng.
* Triển khai tracing và giám sát phân tán để nắm rõ hành trình yêu cầu.
* Xác định xu hướng chi phí và kích hoạt giám sát bất thường.

## Ghi chú

Tham khảo: https://cloudjourney.awsstudygroup.com/