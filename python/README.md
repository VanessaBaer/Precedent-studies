# 🧪 Precedent Study: PR Title Policy Checker

This repository documents a learning journey from an **original PR title validator** → a **safe replication lab** → a **production-ready** implementation.

## Story of Progression

Baseline ➜ Replication ➜ Improvements

- **01 – Precedent Study:** Original script (as found).
- **02 – Replication Lab:** Safe, local walkthrough with stubs/fixtures and checkpoints.
- **03 – Improvements:** Hardened script for CI (argparse, error handling, clear exit codes).

## Quick Start
```bash
python 03-improvements/validate_pr_title.py \
  --repository-name <ORG>/<REPO> \
  --pull-request-id 123 \
  --regex "(feat|fix|docs|chore)(\\([^)]+\\))?: .{10,}" \
  --full-match --ignore-case
