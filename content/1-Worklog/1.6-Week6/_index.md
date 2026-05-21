---
title: "Week 06 – Observability & Monitoring"
date: 2026-05-25
draft: false
weight: 6
chapter: false
---

## Goals

* Implement observability for cloud resources and deployed services.
* Configure CloudWatch dashboards, logs, metrics, and alarms.
* Use tracing and distributed monitoring for application requests.
* Review cost visibility and identify any anomalies.

## Suggested tasks (by day)

| Day | Task | Notes |
|-----|------|-------|
| 1 | Design CloudWatch dashboards for key resources | CPU, memory, network, request latency |
| 2 | Centralize logs from EC2/ECS/Lambda into CloudWatch Logs | Create log groups and retention policies |
| 3 | Add CloudWatch Alarms for high error rate, latency, and budget threshold | Integrate with SNS notifications |
| 4 | Enable AWS X-Ray or tracing for service calls | Visualize request paths and latencies |
| 5 | Review AWS Cost Explorer and set up cost anomaly detection | Compare actual spend to forecast |
| 6 | Document observability patterns and lessons learned | Capture runbook steps and issues |

## Achievements

* Built reusable dashboards for infrastructure and application health.
* Centralized logging and created alerts for critical incidents.
* Implemented tracing or distributed monitoring for service visibility.
* Identified cost patterns and configured anomaly detection.

## Notes

Reference: https://cloudjourney.awsstudygroup.com/