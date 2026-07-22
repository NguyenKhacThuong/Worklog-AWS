---
title: "Tuần 05 – Tự động hóa, IaC và CI/CD"
date: 2026-04-20
draft: false
weight: 5
chapter: false
---

## Mục tiêu

* Cài đặt hạ tầng bằng Infrastructure as Code với Terraform hoặc CloudFormation.
* Xây dựng quy trình CI/CD để build site Hugo và deploy lên S3 cùng CloudFront.
* Cải thiện bảo mật bằng IAM least-privilege và quản lý secrets.
* Thiết lập giám sát cơ bản bằng CloudWatch logs, metrics và alarm.
* Khám phá triển khai container đơn giản với ECR và ECS Fargate nếu thời gian cho phép.

## Công việc đề xuất

| Ngày | Công việc | Ghi chú |
|------|-----------|---------|
| 1 | Viết IaC cho VPC, S3 và CloudFront bằng module tái sử dụng | Bắt đầu với template Terraform hoặc CloudFormation đơn giản |
| 2 | Tạo IaC cho EC2, ALB, ASG hoặc ECS service | Tái sử dụng template từ các tuần trước |
| 3 | Tạo GitHub Actions để build Hugo, deploy lên S3 và invalidate CloudFront | Lưu secrets trong GitHub Secrets hoặc SSM |
| 4 | Áp dụng IAM policy theo nguyên tắc least-privilege và chuyển secrets sang Secrets Manager | Kiểm tra bằng vai trò thử nghiệm |
| 5 | Cấu hình CloudWatch Logs và alarm cho CPU, 5xx và lỗi S3 | Thêm log group cho dịch vụ ứng dụng nếu cần |
| 6 | Build image Docker, push lên ECR và deploy bằng ECS Fargate nếu còn thời gian | Nếu không kịp, chuyển sang Tuần 6 |

## Thành tựu chính

* Xây dựng được cấu hình hạ tầng có thể tái tạo thông qua IaC.
* Thiết lập workflow CI/CD tự động deploy site và làm mới cache CloudFront.
* Thu hẹp phạm vi IAM và tập trung quản lý secrets.
* Nâng cao khả năng giám sát và phát hiện sự cố sớm hơn.

## Ghi chú

Tham khảo: https://cloudjourney.awsstudygroup.com/
