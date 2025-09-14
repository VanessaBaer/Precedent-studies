# 03 – Improvements

This folder contains my **refactored version** of the Deployment with best practices applied.

## Purpose
- Improve on the precedent study by addressing gaps and risks.
- Apply production-grade enhancements such as secrets management and security contexts.
- Demonstrate my ability to evolve existing manifests.

## Files
- `deployment-improved.yaml` – Deployment with improvements (readinessProbe, securityContext, etc.).
- `secret-db.yaml` – Example Secret to securely store DB credentials.
- `values.schema.json` – Enforces required Helm values (image, db server, etc.).
- `github-actions-ci.yaml` – Example CI/CD workflow to lint and validate Helm templates.
- `README.md` – Notes on the improvements and why they matter.

## Key Improvements
- Added `readinessProbe` to ensure only ready Pods receive traffic.
- Moved DB credentials into a Kubernetes Secret.
- Added `securityContext` for better pod hardening.
- Defined `containerPort` explicitly.
- Provided CI/CD validation workflow for automated checks.

## Learning Outcome
This shows I can take a baseline manifest, **analyze gaps**, and **apply modern best practices** to make it production-ready.