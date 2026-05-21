---
title: "Tuần 08 – Mạng & Kết nối"
date: 2026-06-08
draft: false
weight: 8
chapter: false
---

## Mục tiêu

* Thiết kế kiến trúc mạng VPC an toàn và mở rộng.
* Cấu hình subnet, route table, NAT gateway và security group.
* Triển khai mô hình kết nối như VPC peering hoặc Transit Gateway.
* Xem xét bảo mật mạng và luồng traffic.

## Công việc (gợi ý theo ngày)

| Ngày | Công việc | Ghi chú |
|------|-----------|---------|
| 1 | Thiết kế VPC với public/private subnet | Bao gồm tách biệt dịch vụ và NAT/IGW |
| 2 | Tạo route table, NACL và security group | Áp dụng nguyên tắc least-privilege |
| 3 | Kết nối VPC qua peering hoặc Transit Gateway | Kiểm tra route và truy cập |
| 4 | Cấu hình VPN/Direct Connect hoặc mô phỏng site-to-site | Ghi lại sơ đồ mạng |
| 5 | Kiểm tra traffic và bảo mật ingress/egress | Dùng VPC Flow Logs nếu có |
| 6 | Ghi chép thiết kế mạng và các tradeoff | Tổng hợp best practice |

## Thành tựu

* Xây dựng kiến trúc VPC phân đoạn và chịu lỗi.
* Triển khai routing an toàn và quản lý truy cập outbound bằng NAT.
* Kết nối các VPC hoặc môi trường để trao đổi dịch vụ.
* Ghi lại kiến trúc mạng và giả định bảo mật.

## Ghi chú

Tham khảo: https://cloudjourney.awsstudygroup.com/