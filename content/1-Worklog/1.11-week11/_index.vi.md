---
title: "Tuần 11 – Tự động hóa nâng cao và GitOps"
date: 2026-04-20
draft: false
weight: 11
chapter: false
---

## Mục tiêu

* Cải thiện khả năng tự động hóa hạ tầng bằng các mẫu tái sử dụng.
* Xây dựng các module Terraform, workflow CI/CD chung và pipeline kiểm thử.
* Khám phá GitOps để triển khai và promote môi trường một cách nhất quán.
* Xem xét các chiến lược rollback, blue/green và canary.

## Công việc đề xuất

| Ngày | Công việc | Ghi chú |
|------|-----------|---------|
| 1 | Refactor IaC thành các module tái sử dụng và template có tham số | Dùng lại code giữa các môi trường |
| 2 | Thêm validation và kiểm thử cho hạ tầng | Sử dụng terraform fmt, validate và plan check |
| 3 | Xây dựng workflow GitOps cho việc promote môi trường | Sử dụng branch, pull request hoặc repository riêng |
| 4 | Triển khai các chiến lược release blue/green hoặc canary | Giảm rủi ro trong quá trình release |
| 5 | Thêm quy trình rollback và phát hiện drift | Chuẩn bị các bước phục hồi và cảnh báo |
| 6 | Ghi chép các mẫu automation và quy trình vận hành | Lưu lại cách trigger và audit deployment |

## Thành tựu chính

* Tạo ra các module tự động hóa tái sử dụng và pipeline triển khai có thể kiểm thử.
* Áp dụng các nguyên tắc GitOps để promote môi trường an toàn hơn.
* Triển khai các chiến lược release cùng khả năng rollback hiệu quả.
* Ghi lại các mẫu tự động hóa và playbook vận hành rõ ràng hơn.

## Ghi chú

Tham khảo: https://cloudjourney.awsstudygroup.com/