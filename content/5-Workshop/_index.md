---
title: "Workshop"
date: 2026-07-01
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

#### Overview
 
This section documents the actual implementation of the graduation workshop project — **AI Content Generator Platform**, a multi-tenant SaaS platform that automates marketing content production using Generative AI (Gemini API), fully deployed on real AWS infrastructure (VPC, RDS Multi-AZ, EC2 Auto Scaling, SQS/Lambda, WAF, CI/CD) over 4 weeks (Week 9–12).
 
All content below reflects the actual deployment.
 
#### Contents
1. [Project Overview](5.1-Workshop-overview)
2. [Prerequisites](5.2-Prerequisite/)
3. [Networking — VPC, Subnets, Security Groups, IAM Role](5.3-Networking/)
4. [Data & Cache — RDS Multi-AZ, ElastiCache Redis, Secrets Manager](5.4-Data-Cache/)
5. [Compute — ALB, Auto Scaling Group, Docker](5.5-Compute/)
6. [Asynchronous Processing — SQS, Lambda Worker, Gemini API](5.6-Async-Worker/)
7. [CDN & Security — S3+Cloudflare, WAF, CloudWatch](5.7-CDN-Security/)
8. [CI/CD — GitHub Actions + OIDC](5.8-CICD/)
9. [Testing & Operations](5.9-Testing/)
10. [Cleanup](5.10-Cleanup/)