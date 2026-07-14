# VMware AVI Tenant Provisioning

Focused Python automation for creating a VMware AVI Load Balancer tenant through the AVI Controller API.

## Objective

Provision a tenant using environment-driven configuration without committing controller URLs, usernames, passwords, or session tokens.

## Setup

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
copy .env.example .env
```

Update `.env` with your AVI controller values:

```text
AVI_CONTROLLER_URL=https://avi-controller.example.com
AVI_USERNAME=replace-with-controller-user
AVI_PASSWORD=replace-with-controller-password
AVI_TENANT_NAME=Hariharan Demo Tenant
AVI_VERIFY_TLS=true
```

## Run

```bash
python tenant_provisioning.py
```

## Production Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Operations Guide](docs/OPERATIONS.md)
- [Architecture Diagram](docs/diagrams/architecture.mmd)
- [Workflow Diagram](docs/diagrams/workflow.mmd)
- [Security Policy](SECURITY.md)
- [Contributing Guide](CONTRIBUTING.md)

