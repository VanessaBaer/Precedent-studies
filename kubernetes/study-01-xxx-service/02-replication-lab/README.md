# 02 – Replication Lab

This folder contains my **guided lab** where I replicated the precedent study locally in a safe way, without deploying to a cluster.

## Purpose
- Validate the precedent manifest using Helm and schema tools.
- Practice Helm templating, linting, and rendering.
- Add **checkpoints** to confirm correctness at each step.

## Files
- `values.yaml` – Minimal values for rendering the Deployment.
- `rendered.yaml` – Output from `helm template`.
- `lint-results.txt` – Results from `helm lint`.
- `validation-results.txt` – Results from `kubeconform` or `kubeval`.
- `README.md` – Step-by-step unified walkthrough with explanations, commands, and checkpoints.

## Learning Outcome
This shows that I can take an existing manifest, **understand it**, and **replicate it safely** with validation.
