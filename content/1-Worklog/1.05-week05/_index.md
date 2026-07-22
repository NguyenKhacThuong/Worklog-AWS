---
title: "Week 05 – Automation, IaC, and CI/CD"
date: 2026-04-20
draft: false
weight: 5
chapter: false
---

## Objectives

* Provision infrastructure using Infrastructure as Code with Terraform or CloudFormation.
* Build a CI/CD workflow to build the Hugo site and deploy it to S3 and CloudFront.
* Improve security posture by applying least-privilege IAM policies and secret management.
* Set up basic observability using CloudWatch logs, metrics, and alarms.
* Optionally explore container deployment with ECR and ECS Fargate.

## Suggested tasks

| Day | Task | Notes |
|-----|------|-------|
| 1 | Write IaC for VPC, S3, and CloudFront using a reusable module | Start with a simple Terraform or CloudFormation template |
| 2 | Create IaC for EC2, ALB, ASG, or an ECS service | Reuse previous templates where possible |
| 3 | Create a GitHub Actions workflow to build Hugo, deploy to S3, and invalidate CloudFront | Store secrets in GitHub Secrets or SSM |
| 4 | Apply least-privilege IAM policies and move secrets to Secrets Manager | Validate permissions with a test role |
| 5 | Configure CloudWatch logs and alarms for CPU, 5xx errors, and S3 issues | Add log groups for application services |
| 6 | Build a Docker image, push it to ECR, and deploy it with ECS Fargate if time allows | If not, defer this to Week 6 |

## Key achievements

* Built a more reproducible infrastructure setup through IaC.
* Set up an automated deployment workflow for the site and cache invalidation.
* Tightened IAM and centralized secret management.
* Improved observability and early issue detection.

## Notes

Reference: https://cloudjourney.awsstudygroup.com/

