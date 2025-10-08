# 02 – Replication Lab (Unified Walkthrough)

Goal: Reproduce the behavior **safely and locally** without hitting real APIs.

## How This Lab Works
We stub `utils/github.py` to return deterministic data and include a fixture JSON for the PR title. This lets you practice:
- Running the baseline flow
- Toggling bot behavior
- Switching between passing/failing titles
- Checking exit codes

## Steps & Checkpoints

1) **Happy path (passes)**
```bash
python 01-precedent-study/validate_pr_title_baseline.py \
  --repository-name org/repo \
  --pull-request-id 100 \
  --regex "JIRA-[0-9]+"
