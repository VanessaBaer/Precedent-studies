# 🧩 Kubernetes Job Hooks for PostgreSQL Lifecycle (Helm-Assisted)

This repository explores how **Kubernetes Jobs** can automate database creation and deletion using **Helm hooks** as triggers.

## 🗂 Folder Structure

| Folder | Purpose |
|---------|----------|
| `01-precedent-study/` | Original Kubernetes manifests templated by Helm |
| `02-replication-lab/` | Validation and walkthrough of Job behavior |
| `03-improvements/` | Enhanced, production-ready Job definitions |

## 🌱 Story of Progression

1️⃣ **Baseline:** Observe the original Helm-templated Kubernetes Job  
2️⃣ **Replication:** Run, validate, and understand Kubernetes Job mechanics  
3️⃣ **Improvements:** Add cleanup, limits, observability, and operational safety

```mermaid
flowchart LR
    A[01-precedent-study] --> B[02-replication-lab]
    B --> C[03-improvements]
    C --> D[Operational Best Practices]
