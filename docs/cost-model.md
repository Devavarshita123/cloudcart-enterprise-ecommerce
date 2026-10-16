# Cost Model

## Objective
Make cost assumptions explicit and reviewable before choosing cloud services.

## Model
The demo uses:

`estimated monthly cost = compute hours × compute rate + storage GB × storage rate`

The rates and quantities are supplied explicitly. They are illustrative values, not a current AWS quote. Taxes, data transfer, requests, backups, logs, support, minimum charges, and regional pricing are not included unless modeled separately.

## Guardrails
- Start with local development and no cloud resources.
- Before deployment, identify every resource and its pricing dimension.
- Check region, free-tier eligibility, quotas, storage retention, logs, and data transfer.
- Configure billing alerts/budgets where available, but do not treat alerts as a hard spending cap.
- Review actual billing after testing and remove resources when finished.

A zero estimate in the local demo means only that the entered assumptions specify zero usage. It does not guarantee that a real AWS account has no charges.
