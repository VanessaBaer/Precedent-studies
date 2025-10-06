
---

### 📘 **01-precedent-study/README.md**

```markdown
# 01 – Baseline Precedent Study

This folder contains the **original Helm-templated Kubernetes Jobs** that run before installation (`pre-install`) and after deletion (`post-delete`).

**Focus:** Kubernetes Job mechanics and how Helm’s hook annotations trigger them.

**What to Observe:**
- The `batch/v1` Job controller behavior.
- `env`, `envFrom`, and Secret handling.
- Hook annotations and lifecycle order.
