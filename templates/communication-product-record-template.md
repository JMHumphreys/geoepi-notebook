# Communication-product record

> This record identifies the evidence, audience, claims, review, and readiness of a communication product. It does not authorize release.

## Identification

- Project ID: `REQUIRED-replace-me`
- Communication-product ID: `REQUIRED-product-id`
- Title: `REQUIRED`
- Product type: `manuscript / report / briefing / map / dashboard / bulletin / release / other`
- Product version: `REQUIRED`
- Product owner: `REQUIRED-role-or-account`
- Authoritative location: `REQUIRED`
- Date created: `REQUIRED-ISO-8601-date`
- Last reviewed: `optional-ISO-8601-date`
- Product-preparation status: `planned`

Use exactly: `planned`, `in preparation`, `under review`, `revision required`, `ready for release review`, or `superseded`. The safe default is `planned`.

## Audience and purpose

- Audience: `REQUIRED`
- Purpose: `REQUIRED`
- Intended action or decision: `REQUIRED`
- Channel: `REQUIRED`
- Internal or external: `REQUIRED`
- Urgency: `optional`
- Current-through date: `optional`
- Expiration or stale-after date: `optional`
- Restrictions: `REQUIRED-or-not_applicable`

## Evidence

- Result IDs: `REQUIRED`
- Validation-record IDs: `REQUIRED`
- Collaboration-record ID: `REQUIRED`
- Analysis version: `REQUIRED`
- Data versions: `REQUIRED`
- Contribution-record ID: `REQUIRED-or-not_applicable`

## Claim table

| Claim ID | Proposed wording | Claim type | Supporting result IDs | Validation record | Scope | Uncertainty | Limitation | Review status |
|---|---|---|---|---|---|---|---|
| `CLAIM-001` | `Replace with scoped wording` | `description / comparison / estimate / other` | `RESULT-001` | `VALIDATION-001` | `REQUIRED` | `describe or not_applicable` | `describe or none` | `planned` |

The example row is not approved or released.

## Product contents

- Text or narrative location: `REQUIRED`
- Figures: `REQUIRED-or-not_applicable`
- Tables: `REQUIRED-or-not_applicable`
- Maps: `REQUIRED-or-not_applicable`
- Supplements: `REQUIRED-or-not_applicable`
- Data package: `REQUIRED-or-not_applicable`
- Code/software package: `REQUIRED-or-not_applicable`
- Availability statements: `REQUIRED`

## Reporting and accessibility

- Applicable reporting guideline: `REQUIRED-or-not_applicable`
- Completed-checklist location: `REQUIRED-or-not_applicable`
- Accessibility review: `REQUIRED-or-not_applicable`
- Alt-text location: `REQUIRED-or-not_applicable`
- Table or text alternatives: `REQUIRED-or-not_applicable`
- Unresolved issue: `none or describe`

## Review record

| Review ID | Review purpose | Object/version | Reviewer | Finding | Response | Decision owner | Date | Status |
|---|---|---|---|---|---|---|---|---|
| `blank until review` | `blank until review` | `blank until review` | `blank until review` | `blank until review` | `blank until review` | `blank until review` | `blank until review` | `planned` |

Reuse the Collaborate response vocabulary where practical. Review is not approval.

## Restrictions and availability

- Data availability: `REQUIRED`
- Code availability: `REQUIRED`
- Software availability: `REQUIRED-or-not_applicable`
- Licenses: `REQUIRED-or-not_applicable`
- Confidentiality: `REQUIRED-or-not_applicable`
- Partner conditions: `REQUIRED-or-not_applicable`
- Indigenous, Tribal, or community authority: `REQUIRED-or-not_applicable`
- Embargo: `REQUIRED-or-not_applicable`
- Release authority: `REQUIRED`

## Ready for release review

This section is authoritative for release-review readiness. Safe default: `not ready for release review`.

- Exact product version: `REQUIRED`
- Exact package location: `REQUIRED`
- Required reviews complete: `REQUIRED-or-limitations`
- Unresolved concerns: `none or accepted documented condition; describe while not ready`
- Documented limitation: `blank while not ready; REQUIRED for limitation status`
- Why limitation matters: `blank while not ready; REQUIRED for limitation status`
- Affected scope: `blank while not ready; REQUIRED for limitation status`
- Downstream caution: `blank while not ready; REQUIRED for limitation status`
- Required follow-up: `blank while not ready; REQUIRED for limitation status`
- Responsible follow-up: `blank while not ready; REQUIRED for limitation status`
- Readiness status: `not ready for release review`
- Decision-maker: `blank while not ready`
- Decision date: `blank while not ready; ISO 8601 when populated`

Use exactly: `not ready for release review`, `ready for release review`, or `ready for release review with documented limitation`. Readiness does not grant release approval.
