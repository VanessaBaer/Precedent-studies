# Kubernetes Precedent Study: xxx-service Deployment

This project shows how I learn from **precedent studies** and extend them into **hands-on replication labs** and **improvements**.

---

## Structure

- **01-precedent-study/**
  - Contains the original `deployment.yaml` taken as a precedent study.
  - Shows the baseline state before any modifications.

- **02-replication-lab/**
  - My step-by-step guided lab where I lint, render, and validate the precedent locally.
  - Includes checkpoints to prove understanding without deploying to a cluster.

- **03-improvements/**
  - My refactored Deployment and supporting files with best practices applied:
    - readinessProbe
    - Secret for DB credentials
    - securityContext
    - CI/CD validation workflow
    - values.schema.json

---

## Learning Path

1. **Study the precedent.**  
2. **Replicate it safely** with linting, templating, and validation.  
3. **Improve it** with production-ready enhancements.  

This demonstrates my ability to:
- Analyze existing work  
- Recreate it with safe validation  
- Improve it with modern DevOps best practices  

---

# 🔎 Analyze the Study

## What was done and why

- A **Kubernetes Deployment** for a service named `comms-service`.
- It’s Helm-templated to make the image, DB connection, OTEL config, and resources configurable via `values.yaml`.
- Adds **Prometheus scrape annotations** to expose `/metrics` on port `8080`.
- Includes **startup** and **liveness** probes hitting `/healthz` on `8080`.
- Limits rollout history with `revisionHistoryLimit: 2`.
- Schedules Pods on Linux nodes via `nodeSelector`.

## Goals, tools, and concepts involved

- **Kubernetes** (Deployment, Probes, Labels/Selectors).
- **Helm** templating (`.Values`, `.Chart.AppVersion`, pipelines like `| default` and `| nindent`).
- **Observability** (Prometheus annotations).
- **Telemetry** (OpenTelemetry env vars).
- **Config management** (values > templates).

## Best practices followed (👍)

- **Selector ↔ labels** are consistent (`app: comms-service`).
- **Probes present** (startup + liveness).
- **Limited revision history** to reduce stored ReplicaSets.
- **Values-driven resources**: `{{ .Values.resources | toYaml | nindent 10 }}`.
- **Template defaults** (`db.database | default .Release.Namespace`).
- **Linux node targeting**—explicit and predictable scheduling.

## Mistakes or risks (🚩) & quick wins

1. **No readinessProbe**  
   Add one so the Service routes traffic only when ready.  

2. **Database credentials inline in values**  
   Move to **Secrets** and reference with `env.valueFrom.secretKeyRef`. Never store passwords in `values.yaml`.  

3. **Prometheus annotations vs Operator**  
   If you use **Prometheus Operator**, prefer a **Service + ServiceMonitor** over Pod annotations.  

4. **OpenTelemetry var names**  
   Common names are `OTEL_EXPORTER_OTLP_ENDPOINT` and `OTEL_SERVICE_NAME`. Confirm your app’s expected env keys.  

5. **No containerPort**  
   Add `containerPort: 8080` (helps tooling and docs).  

6. **Security posture**  
   Add `securityContext` (runAsNonRoot, readOnlyRootFilesystem), drop capabilities.  

7. **Release hygiene**  
   Consider `imagePullPolicy`, **checksum annotations** for config/secret rollouts, **pod anti-affinity/topology spread**, **PDB**, **HPA**.  

---

# 🧠 Reflection & Learning

## Key takeaways

- Helm lets you **parameterise** Deployments; keep secrets out of values.  
- Health probes should include **readiness** for safe traffic routing.  
- Observability differs between **annotations** and **ServiceMonitor** (Operator).  
- Hardening via `securityContext`, resource requests/limits, and topology policies is essential for production.  

