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

Preparation statuses `planned`, `in preparation`, `under review`, and `revision required` require release-review readiness to remain `not ready for release review`. Preparation may become `ready for release review` only with either ready readiness status. `superseded` must not retain a ready status.

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
| `CLAIM-001` | `Replace with scoped wording` | `description / comparison / estimate / other` | `RESULT-001` | `VALIDATION-001` | `REQUIRED` | `describe or not_applicable` | `describe or none` | `proposed` |

Use exactly these claim-review states: `proposed`, `under review`, `accepted for current product`, `revision required`, `removed`, and `superseded`. The safe default is `proposed`. Accepted consequential claims require supporting result IDs, a validation-record ID, intended scope, uncertainty, limitation or explicit `none`, responsible reviewer, and review date. Accepted is not release approval. A removed consequential claim records its reason; a superseded claim identifies a replacement claim ID or product version.

The example row is not accepted or released.

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

| Review ID | Review purpose | Object/version | Reviewer | Finding | Response outcome | Decision owner | Review date | Review state |
|---|---|---|---|---|---|---|---|---|
| `blank until review` | `blank until review` | `blank until review` | `blank until review` | `blank until review` | `blank until review` | `blank until review` | `blank until review` | `planned` |

Use exactly these review states: `planned`, `in progress`, `completed`, and `superseded`. The safe default is `planned`. A planned or in-progress review may have a blank response outcome. A completed consequential review requires a finding, one of the Collaborate response outcomes (`accepted and addressed`, `addressed differently`, `deferred`, `not accepted with rationale`, `transferred to another lifecycle stage`, or `unresolved`), decision owner, and date. Completed review is not approval. A superseded review identifies its replacement review or product version.

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

- Working product location: `REQUIRED`
- Exact release-review package location: `blank until ready`
- Release-review package version: `blank until ready`
- Package checksum: `optional; blank until calculated`
- Required reviews complete: `REQUIRED-or-limitations`
- Unresolved concerns: `none or accepted documented condition; describe while not ready`
- Documented limitation: `blank while not ready; none for ordinary ready; REQUIRED for limitation status`
- Why limitation matters: `blank while not ready; not applicable for ordinary ready; REQUIRED for limitation status`
- Affected claim, result, audience, geography, period, use, product, or channel: `blank while not ready; not applicable for ordinary ready; REQUIRED for limitation status`
- Downstream caution or restriction: `blank while not ready; none or ordinary product caution for ordinary ready; REQUIRED for limitation status`
- Required follow-up: `blank while not ready; none or communication-preparation follow-up for ordinary ready; REQUIRED for limitation status`
- Responsible follow-up: `blank while not ready; not applicable when no follow-up exists; REQUIRED for limitation status`
- Readiness status: `not ready for release review`
- Decision-maker: `blank while not ready`
- Decision date: `blank while not ready; ISO 8601 when populated`
- Replacement communication-product ID/version: `blank unless superseded`
- Supersession reason: `blank unless superseded`
- Supersession date: `blank unless superseded`
- Supersession responsible owner: `blank unless superseded`

Use exactly: `not ready for release review`, `ready for release review`, or `ready for release review with documented limitation`. The working product may exist while the product is not ready. The exact release-review package is required only for either ready status. It must not change after the readiness decision without a new package version and renewed affected review. Decision-maker and date remain blank while not ready. Readiness does not grant release approval.
