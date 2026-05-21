---
title: "Tuần 04 – Scale & Phân phối nội dung"
date: 2026-05-11
draft: false
weight: 4
chapter: false
---

## Mục tiêu

* Cấu hình EC2 Auto Scaling Group với Application Load Balancer.
* Thiết lập CloudFront CDN cho S3 static website.
* Thực hành Route 53 quản lý DNS cơ bản.
* Hiểu kiến trúc High Availability 3-tier trên AWS.

### Công việc

| Ngày | Công việc | Bắt đầu | Kết thúc | Tài liệu |
|------|-----------|---------|---------|---------|
| 1 | Tạo Launch Template, Auto Scaling Group | 2026-05-11 | 2026-05-11 | https://000006.awsstudygroup.com |
| 2 | Gắn Application Load Balancer vào Auto Scaling Group | 2026-05-12 | 2026-05-12 | https://000006.awsstudygroup.com |
| 3 | Test scale-out: tăng tải CPU, quan sát thêm instance | 2026-05-13 | 2026-05-13 | https://000006.awsstudygroup.com |
| 4 | Tạo CloudFront distribution trỏ vào S3 | 2026-05-14 | 2026-05-14 | https://000094.awsstudygroup.com |
| 5 | Cấu hình Route 53 hosted zone, tạo A record | 2026-05-15 | 2026-05-15 | https://000010.awsstudygroup.com |
| 6 | Vẽ sơ đồ kiến trúc tổng hợp, cập nhật worklog | 2026-05-16 | 2026-05-16 | Tài liệu nội bộ |

### Thành tựu

* Cấu hình Auto Scaling Group tự động thêm instance khi CPU > 70%.
* Gắn ALB phân phối traffic đều giữa các instance.
* Thiết lập CloudFront, kiểm tra cache hit qua header X-Cache.
* Tạo Route 53 record, trỏ domain vào CloudFront distribution.
* Vẽ và trình bày sơ đồ kiến trúc High Availability 3-tier với mentor.

### Ghi chú

Tham khảo: https://cloudjourney.awsstudygroup.com/1-explore/