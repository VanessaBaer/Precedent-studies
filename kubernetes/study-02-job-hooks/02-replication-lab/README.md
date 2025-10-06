# 02 – Replication Lab (Kubernetes Focus)

Here we replicate and observe Kubernetes behavior directly.

## Steps
1. `helm template . > rendered.yaml`
2. `kubectl apply --dry-run=client -f rendered.yaml`
3. `kubectl create -f rendered.yaml`
4. Observe Job and Pod behavior:
   ```bash
   kubectl get jobs,pods
   kubectl logs job/<job-name>
5. Validate completion, retries, and environment variable injection.

Goal: Understand how Kubernetes executes Jobs and manages their lifecycle.