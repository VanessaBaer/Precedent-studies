
## `01-precedent-study/README.md`
```markdown
# 01 – Precedent Study (Baseline)

This folder contains the original script exactly as found. It:
- Parses CLI flags for repository, PR id, and regex.
- Skips bot-authored PRs.
- Queries GitHub GraphQL for the PR title.
- Validates the title against the supplied regex.

Use this as the reference baseline. See `02-replication-lab/` for a safe, guided walkthrough.
