---
title: "Workshop"
date: 2024-01-01
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

#### Tổng quan
 
Mục này trình bày chi tiết quá trình tự triển khai dự án workshop — **AI Content Generator Platform**, nền tảng SaaS đa tenant tự động hóa sản xuất nội dung marketing bằng Generative AI (Gemini API), triển khai đầy đủ trên hạ tầng AWS thật (VPC, RDS Multi-AZ, EC2 Auto Scaling, SQS/Lambda, WAF, CI/CD) trong 4 tuần (Tuần 9–12).
 
Toàn bộ nội dung dưới đây là báo cáo thực tế đã triển khai.
 
#### Nội dung
1. [Tổng quan dự án](5.1-Workshop-Overview/)
2. [Chuẩn bị](5.2-Prerequisite/)
3. [Networking — VPC, Subnet, Security Group, IAM Role](5.3-Networking/)
4. [Dữ liệu & Cache — RDS Multi-AZ, ElastiCache Redis, Secrets Manager](5.4-Data-Cache/)
5. [Compute — ALB, Auto Scaling Group, Docker](5.5-Compute/)
6. [Xử lý bất đồng bộ — SQS, Lambda Worker, Gemini API](5.6-Async-Worker/)
7. [CDN & Bảo mật — S3+Cloudflare, WAF, CloudWatch](5.7-CDN-Security/)
8. [CI/CD — GitHub Actions + OIDC](5.8-CICD/)
9. [Kiểm thử & Vận hành](5.9-Testing/)
10. [Dọn dẹp tài nguyên](5.10-Cleanup/)