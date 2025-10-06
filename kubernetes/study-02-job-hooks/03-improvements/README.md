
---

### 🚀 **03-improvements/README.md**

```markdown
# 03 – Improvements (Kubernetes-Centric Enhancements)

Enhancements applied:
- Added `ttlSecondsAfterFinished: 300`
- Defined CPU/memory requests and limits
- Added `backoffLimit: 2`
- Changed `imagePullPolicy: IfNotPresent`
- Improved annotations and comments

**Why These Matter**
- TTL cleans up Jobs after completion
- Resource limits prevent cluster exhaustion
- Backoff limits reduce unnecessary retries
- Improved scheduling ensures better resilience
