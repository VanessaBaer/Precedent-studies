# 02 — Replication Lab

This folder walks through replicating the precedent study with checkpoints.

## Steps
1. Create inventory file.
2. Verify connectivity with `ansible -m ping`.
3. Run `ansible-playbook -i inventory web-svc.yaml`.
4. Confirm idempotency on second run.

## Checkpoints
- ✅ Ping success (would confirm host reachable)
- ✅ Playbook run: changed=2 (would confirm httpd installed & service started)
- ✅ Playbook rerun: changed=0 (would confirm idempotency)

⚠️ **Note:** These commands are **not executed here** due to missing environment (VMs/SSH keys). They are kept as conceptual learning checkpoints.
