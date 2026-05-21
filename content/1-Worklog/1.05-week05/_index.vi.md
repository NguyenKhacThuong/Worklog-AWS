---
title: "Tuần 05 – Tự động hoá, IaC và CI/CD"
date: 2026-05-18
draft: false
weight: 5
chapter: false
---

## Mục tiêu

* Thiết lập hạ tầng bằng IaC (Terraform hoặc CloudFormation).
* Xây dựng pipeline CI/CD để build Hugo site và deploy lên S3 + CloudFront.
* Cải thiện bảo mật (IAM least-privilege, Secrets Manager/SSM, KMS).
* Thiết lập giám sát cơ bản (CloudWatch logs/metrics, alarms).
* Thử nghiệm deploy container đơn giản (ECR + ECS Fargate) — tùy thời gian.

## Công việc (gợi ý ngày theo tuần)

| Ngày | Công việc | Ghi chú |
|------|-----------|---------|
| 1 | Viết IaC cho VPC + S3 + CloudFront (mô-đun cơ bản) | Bắt đầu với Terraform hoặc CloudFormation mẫu |
| 2 | Viết IaC cho EC2/ALB/ASG hoặc ECS service | Tái sử dụng template từ tuần trước |
| 3 | Tạo GitHub Actions: build Hugo → deploy S3 → invalidate CloudFront | Lưu secrets vào GitHub secrets hoặc SSM |
| 4 | Thiết lập IAM policies ít quyền nhất, chuyển secrets sang Secrets Manager | Kiểm tra bằng role giả lập |
| 5 | Thiết lập CloudWatch Logs, tạo alarm cơ bản (CPU, 5xx, S3 errors) | Thêm log group cho ứng dụng nếu có |
| 6 | Tạo image Docker cho app mẫu, push lên ECR, deploy bằng ECS Fargate (tùy) | Nếu không kịp, để làm Tuần 6 |

## Thành tựu mong đợi

* Có repo IaC cơ bản để reproduce hạ tầng (dev → staging).
* Có workflow CI/CD tự động deploy site lên S3 và làm sạch cache CloudFront.
* Secrets được quản lý an toàn, IAM được thu hẹp quyền.
* Giám sát cơ bản hoạt động giúp phát hiện sớm sự cố.

## Ghi chú

* Tài nguyên tham khảo: https://cloudjourney.awsstudygroup.com/
