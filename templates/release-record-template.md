# Release record

> This record documents a release decision and release event for one exact communication-product version. It does not create release authority.

## Identification

- Project ID: `REQUIRED-replace-me`
- Release-record ID: `REQUIRED-release-id`
- Communication-product ID: `REQUIRED`
- Communication-product version: `REQUIRED`
- Prepared release package: `blank until approved`
- Release target: `REQUIRED`
- Audience: `REQUIRED`
- Channel: `REQUIRED`
- Purpose: `REQUIRED`
- Responsible owner: `REQUIRED-role-or-account`

## Review basis

- Release-review-readiness record: `REQUIRED`
- Validation-record IDs: `REQUIRED`
- Collaboration record: `REQUIRED`
- Contribution record: `REQUIRED-or-not_applicable`
- Required review records: `REQUIRED-or-not_applicable`
- Restrictions and agreements: `REQUIRED-or-not_applicable`
- Reporting checklist: `REQUIRED-or-not_applicable`
- Accessibility review: `REQUIRED-or-not_applicable`
- Availability statements: `REQUIRED`

## Release decision

Safe default: `not yet reviewed for specified release`.

- Release-decision status: `not yet reviewed for specified release`
- Release-decision scope: `blank until reviewed`
- Release authority: `blank until authority identified`
- Decision date: `blank until decision; ISO 8601 when populated`
- Exact approved package location: `blank until approved`
- Approved package checksum: `optional; blank until calculated`
- Approved audience: `blank until approved`
- Approved channel: `blank until approved`
- Approved purpose: `blank until approved`
- Conditions: `blank until approved; none or describe`
- Limitation or warning: `blank until approved; none or describe`
- Required follow-up: `blank until approved; none or describe`
- Responsible follow-up: `blank until approved; none or describe`
- Expiration or reconsideration date: `optional`

Use exactly: `not yet reviewed for specified release`, `approved for specified release`, `approved for specified release with documented condition`, `not approved for specified release`, `deferred for specified release`, or `superseded before release decision`. Approved with documented condition requires a condition, why it matters, affected audience/purpose/channel/claim/use, warning or limitation, follow-up, responsible follow-up, and expiration or reconsideration date where relevant; empty or `none` condition fields are not allowed. Not approved requires rationale, blocking concern or unmet requirement, authority, date, and return-to-lifecycle-stage decision. Deferred requires reason, unresolved dependency, responsible person, and reconsideration condition or date. Superseded before decision requires replacement product ID/version, reason, date, and responsible owner. A copied record must not imply review, approval, release, withholding, withdrawal, correction, or supersession.

## Release event

Safe default: `not released`.

- Release state: `not released`
- Release date: `blank until released`
- Released version: `blank until released`
- Released location: `blank until released`
- Persistent identifier: `blank until assigned; not required for every output`
- Embargo date: `optional`
- License: `REQUIRED-or-not_applicable`
- Data availability: `REQUIRED`
- Code/software availability: `REQUIRED-or-not_applicable`
- Notification or distribution record: `blank until released or withheld`
- Withholding authority: `blank unless withheld`
- Withholding reason: `blank unless withheld`
- Withdrawal authority: `blank unless withdrawn`
- Previous release-record ID: `blank unless withdrawn or superseded`
- Replacement release-record ID: `blank unless superseded`
- Replacement communication-product ID/version: `blank unless superseded`
- Supersession date: `blank unless superseded`

Use exactly: `not released`, `released`, `withheld`, `withdrawn`, or `superseded`.

`not released` must not contain a release date or released location. `released` requires an approved release-decision status and exact release details. `withheld` requires withholding authority and reason and is not a synonym for not released. `withdrawn` requires a previous release record. `superseded` requires replacement product and release records. Approval alone does not change the release state.

## Corrections and supersession

- Correction needed: `no / yes / unknown`
- Correction type: `typographical or formatting; no change to meaning / factual correction; no change to scientific conclusion / corrected figure or table / corrected availability, citation, or attribution statement / corrected data release / corrected code or software release / scientific correction affecting interpretation / withdrawal / publisher- or authority-defined retraction / other`
- Description: `blank until needed`
- Reason: `blank until needed`
- Affected claims: `blank until needed`
- Whether conclusions changed: `blank until needed`
- Correction authority: `blank until needed`
- Correction date: `blank until needed`
- Audience notification: `blank until needed`
- Replacement product ID/version: `blank until needed`
- Return-to-lifecycle-stage decision: `blank until needed`
- Withdrawal reason: `blank until needed`
- Superseding release-record ID: `blank until needed`

Keep the original product and release record identifiable. Do not silently overwrite history.
