---
title: "Week 05 – Automation, IaC and CI/CD"
date: 2026-05-18
draft: false
weight: 5
chapter: false
---

## Goals

* Provision infrastructure using IaC (Terraform or CloudFormation).
* Build a CI/CD pipeline to build the Hugo site and deploy to S3 + CloudFront.
* Improve security (least-privilege IAM, Secrets Manager/SSM, KMS).
* Set up basic observability (CloudWatch logs/metrics, alarms).
* Optional: container deployment (ECR + ECS Fargate) as a mini project.

## Suggested tasks (by day)

| Day | Task | Notes |
|-----|------|-------|
| 1 | Write IaC for VPC + S3 + CloudFront (basic module) | Start with Terraform or CloudFormation sample |
| 2 | Write IaC for EC2/ALB/ASG or ECS service | Reuse previous templates where possible |
| 3 | Create GitHub Actions: build Hugo → deploy to S3 → invalidate CloudFront | Store secrets in GitHub Secrets or SSM |
| 4 | Implement least-privilege IAM policies; migrate secrets to Secrets Manager | Test with least-privilege roles |
| 5 | Configure CloudWatch Logs and alarms (CPU, 5xx, S3 errors) | Add log groups for any app services |
| 6 | Build Docker image, push to ECR, deploy with ECS Fargate (optional) | If time runs out, shift to Week 6 |

## Expected outcomes

* A reproducible IaC repo for dev/staging environments.
* A working CI/CD workflow that deploys the site automatically and invalidates CloudFront cache.
* Secrets centrally managed and IAM tightened.
* Basic observability to surface issues early.

## Notes

* Reference: https://cloudjourney.awsstudygroup.com/
