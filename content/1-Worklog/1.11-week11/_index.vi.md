---
title: "Tuần 11 – Tự động hoá nâng cao & GitOps"
date: 2026-04-20
draft: false
weight: 11
chapter: false
---

## Mục tiêu

* Cải thiện tự động hoá hạ tầng bằng các mẫu tái sử dụng.
* Xây dựng module Terraform, workflow CI/CD chung, và pipeline kiểm thử.
* Khám phá GitOps để triển khai và promote môi trường.
* Xem xét chiến lược rollback, blue/green hoặc canary.

## Công việc (gợi ý theo ngày)

| Ngày | Công việc | Ghi chú |
|------|-----------|---------|
| 1 | Refactor IaC thành module tái sử dụng và template tham số | Dùng lại code giữa các môi trường |
| 2 | Thêm validation và unit test cho hạ tầng | Dùng terraform fmt, validate, plan check |
| 3 | Xây workflow GitOps cho promote môi trường | Dùng branch, PR, hoặc repository riêng |
| 4 | Triển khai chiến lược release blue/green hoặc canary | Giảm rủi ro khi release |
| 5 | Thêm rollback và phát hiện drift | Chuẩn bị bước phục hồi và cảnh báo |
| 6 | Ghi chép mẫu automation và quy trình vận hành | Lưu cách trigger và audit deploy |

## Thành tựu

* Tạo module tự động hoá tái sử dụng và pipeline triển khai có thể kiểm thử.
* Áp dụng nguyên tắc GitOps để promote môi trường an toàn hơn.
* Triển khai chiến lược release và khả năng rollback.
* Ghi lại mẫu tự động hoá và playbook vận hành.

## Ghi chú

Tham khảo: https://cloudjourney.awsstudygroup.com/