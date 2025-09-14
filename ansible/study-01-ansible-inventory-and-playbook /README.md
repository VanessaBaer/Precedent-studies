# Ansible First Playbook — Story of Progression

This repo shows the journey of writing our first Ansible playbook.

## Structure
- **01-precedent-study/** → Original baseline as provided.
- **02-replication-lab/** → Replication walkthrough with checkpoints (conceptual only).
- **03-improvements/** → Refactored version with best practices.

## Story of Progression
1. **Baseline (01):** A simple playbook that installs and starts httpd.  
2. **Replication (02):** Step-by-step validation of connectivity, execution, and idempotency.  
3. **Improvements (03):** Refactored with variables, cross-platform support, and better security.  

⚠️ **Note:** These notes are for study purposes only. Actual replication (e.g., `ansible -m ping` checks) requires a prepared environment with Vagrant/VMs and SSH keys, which is not available here.


# **Analysis of the Study**

### What was done and why

- A **simple Ansible playbook (`web-svc.yaml`)** was written to:
    1. Install the `httpd` package.
    2. Ensure the `httpd` service is started and enabled.
- The **inventory file** defines the managed host (`web01`) with connection details (user, IP, SSH key).
- The **goal**: demonstrate how Ansible automates configuration management (installing packages + managing services).
- **Verification**: Used `ansible -m ping` to check connectivity and then executed the playbook with `ansible-playbook`.

### Goals, tools, and concepts

- **Tools:** Ansible (playbooks, inventory, modules).
- **Concepts:**
    - *Playbooks* = YAML describing tasks.
    - *Idempotency* = Ansible ensures repeated runs don’t change the system unnecessarily.
    - *Inventory* = Defines hosts and connection details.
    - *Modules* (`yum`, `service`) = Reusable units to perform actions.

### Best practices followed

- Used `become: yes` for privilege escalation.
- Tasks are descriptive (`install httpd`, `start service`).
- Demonstrated **idempotency** (changed=0 on rerun).

### Mistakes or risks

- Hardcoded package (`httpd`) limits portability (won’t work on Ubuntu without `apt`).
- Private key permissions issue had to be manually fixed (`chmod 600 private_key`).
- No error handling (handlers, retries, or failure strategies missing).
- Inventory uses plain private key filename instead of vault/encrypted secret.

# **Reflection & Learning**

- Playbooks enforce **idempotency**: repeated runs are safe.
- Inventory files decouple connection details from playbooks.
- This example can be extended into a mini-project by:
    - Supporting multiple OS families (`when: ansible_os_family`).
    - Adding variables (`vars.yaml`) for package/service names.
    - Adding CI check with `ansible-lint`.