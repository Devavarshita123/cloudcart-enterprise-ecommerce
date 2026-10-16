# Security Notes and Lightweight Threat Model

## Assets
- Source code and configuration
- Future customer/order data (not stored by this demo)
- Future credentials and cloud resources (not used by this demo)

## Example threats and controls
| Threat | Demonstration control | Remaining gap |
|---|---|---|
| Malformed order identifier | Strict format validation and control-character rejection | Real API authorization and schema validation not present |
| Sensitive value in logs | Email masking helper | No central log pipeline or formal PII policy |
| Unsafe configuration | Allowlisted values and length checks | No secret manager integration because no secrets are needed |
| Excessive access | Documented least-privilege design principle | No IAM policies are deployed or tested |

## Safe handling rules
- Never commit `.env` files, credentials, access keys, tokens, or personal data.
- Do not paste cloud credentials into source code or chat.
- Use least privilege for any future AWS role.
- Validate data at trust boundaries.
- Keep security claims proportional to evidence.

## Before any real AWS deployment
1. Draw trust boundaries and identify data classifications.
2. Review IAM policies for least privilege.
3. Review network ingress and egress.
4. Define encryption requirements and key policies.
5. Add dependency and secret scanning.
6. Test logging redaction.
7. Verify the deployment's actual cost and remove resources when no longer needed.
