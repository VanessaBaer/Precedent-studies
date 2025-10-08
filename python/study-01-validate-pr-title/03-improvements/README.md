## `03-improvements/README.md`
```markdown
# 03 – Improvements (Production-Ready)

What’s improved and why:
- **argparse**: Avoid mutating `sys.argv`; robust flag parsing.
- **Input validation**: Enforce `owner/repo` format.
- **GraphQL variables**: Prevent malformed queries; support special chars.
- **Error handling**: Detect GraphQL `errors` and missing nodes; return **exit 2** for operational failures.
- **Policy clarity**: `--full-match` and `--ignore-case` switches.
- **CI semantics**: Exit codes — `0` pass, `1` policy fail, `2` operational error.

### Examples
```bash
# Conventional commits (full, case-insensitive)
python 03-improvements/validate_pr_title.py \
  --repository-name <ORG>/<REPO> \
  --pull-request-id 123 \
  --regex "(feat|fix|docs|chore)(\\([^)]+\\))?: .{10,}" \
  --full-match --ignore-case
