# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| `main`  | :white_check_mark: |
| all older tags | :x:      |

We only actively maintain and patch the code in the `main` branch.  Issues in other branches or tags may be addressed at our discretion.

## Reporting a Vulnerability

If you discover a security vulnerability in **pihole‑whitelist**, please report it **privately** so we can fix it before public disclosure.

1. **GitHub Security Advisory**  
   - Go to the **Security** tab of this repository.  
   - Select **Advisories**, then **Create new advisory**.  
   - Fill in as much detail as you can (affected versions, repro steps, impact).  
   - This creates a private thread for confidential discussion.

2. **Email**  
   If you don’t have GitHub access, send an encrypted or plain‐text email to: powersmjustin@gmail.com

Subject: **Security vulnerability in pihole‑whitelist**

Include:
- Affected version(s)  
- Detailed description and proof‐of‐concept or reproduction steps  
- Suggested mitigation or patch  

## Response and Disclosure Policy

- We acknowledge all reports within **5 business days**.  
- We aim to produce a public patch or updated release within **30 calendar days** of confirmation.  
- Once a patch is available, we will coordinate a public disclosure, crediting the reporter if desired.

## Severity Classification

We triage incoming reports roughly as follows:

- **Critical**: Remote code execution, SQL injection, or any vulnerability allowing full compromise.  
- **High**: Authentication bypass, privilege escalation, or data exfiltration.  
- **Medium**: Denial‑of‑service, information leakage of non‑PII data.  
- **Low**: Minor input validation issues, low‑impact misconfigurations.

## After a Fix

Once a fix is released:

- We will tag the patched commit and publish a new release.  
- Users are encouraged to upgrade immediately.  

---

*Thank you for helping keep pihole‑whitelist safe!*  
