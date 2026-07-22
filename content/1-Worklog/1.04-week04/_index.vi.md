---
title: "Tự động mở rộng và Phân phối nội dung"
date: 2026-04-20
draft: false
weight: 4
chapter: false
pre: " <b> Tuần 04: </b> "

---

## Mục tiêu

* Cấu hình EC2 Auto Scaling Group kết hợp với Application Load Balancer.
* Thiết lập CloudFront cho website tĩnh trên S3 nhằm cải thiện hiệu năng phân phối.
* Thực hành quản trị DNS cơ bản với Route 53.
* Hiểu kiến trúc high availability 3 tầng trên AWS.

## Công việc đề xuất

| Ngày | Công việc | Bắt đầu | Kết thúc | Tài liệu |
|------|-----------|---------|---------|---------|
| 1 | Tạo launch template và Auto Scaling Group | 2026-05-11 | 2026-05-11 | https://000006.awsstudygroup.com |
| 2 | Gắn Application Load Balancer vào Auto Scaling Group | 2026-05-12 | 2026-05-12 | https://000006.awsstudygroup.com |
| 3 | Kiểm thử scale-out bằng cách tăng tải CPU và quan sát instance được khởi chạy | 2026-05-13 | 2026-05-13 | https://000006.awsstudygroup.com |
| 4 | Tạo CloudFront distribution trỏ tới bucket S3 | 2026-05-14 | 2026-05-14 | https://000094.awsstudygroup.com |
| 5 | Cấu hình hosted zone trong Route 53 và tạo A record | 2026-05-15 | 2026-05-15 | https://000010.awsstudygroup.com |
| 6 | Vẽ sơ đồ kiến trúc và cập nhật worklog | 2026-05-16 | 2026-05-16 | Tài liệu nội bộ |

## Thành tựu chính

* Cấu hình Auto Scaling Group tự động thêm instance khi CPU vượt 70%.
* Gắn ALB để phân phối lưu lượng đều giữa các instance.
* Thiết lập CloudFront và xác nhận cache hit qua header X-Cache.
* Tạo Route 53 record để trỏ domain tới CloudFront distribution.
* Vẽ và trình bày sơ đồ kiến trúc high availability 3 tầng cho mentor.

## Ghi chú

Tham khảo: https://cloudjourney.awsstudygroup.com/1-explore/