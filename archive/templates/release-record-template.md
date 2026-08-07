# Release record

> This record documents a release decision and release event for one exact communication-product version. It does not create release authority.

## Identification

- Project ID: `REQUIRED-replace-me`
- Release-record ID: `REQUIRED-release-id`
- Communication-product ID: `REQUIRED`
- Communication-product version: `REQUIRED`
- Proposed release package location: `blank until submitted for release decision; REQUIRED before any substantive release decision`
- Proposed release package version: `blank until submitted for release decision; REQUIRED before any substantive release decision`
- Proposed package checksum: `optional; blank until calculated`
- Release target: `REQUIRED`
- Audience: `REQUIRED`
- Channel: `REQUIRED`
- Purpose: `REQUIRED`
- Responsible owner: `REQUIRED-role-or-account`

The proposed package is the exact package considered by the release authority. It must be identifiable before approval, conditional approval, nonapproval, deferral, or pre-decision supersession. A record that is `not yet reviewed for specified release` may retain blank proposed-package fields before submission. The approved package must match the proposed package unless the authority explicitly requires a revised package; if it changes after review, create a new package version and repeat affected review or decision. Approval never applies merely to a title, branch, directory, or changing URL.

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
- Documented condition: `blank unless condition status; none for ordinary approval`
- Why the condition matters: `blank unless condition status; not applicable for ordinary approval`
- Affected audience, purpose, channel, claim, or use: `blank unless condition status; not applicable for ordinary approval`
- Required warning or limitation: `blank unless condition status; none or ordinary product warning for ordinary approval`
- Condition follow-up: `blank unless condition status; none for ordinary approval`
- Condition follow-up owner: `blank unless condition status; not applicable when no follow-up exists`
- Condition expiration or reconsideration date: `blank unless applicable`
- Nonapproval rationale: `blank unless not approved`
- Blocking concern or unmet requirement: `blank unless not approved`
- Required return stage: `blank unless not approved; Analyze / Validate / Collaborate / Communicate / external process / terminal disposition`
- Required corrective action: `blank unless not approved`
- Responsible corrective-action owner: `blank unless not approved`
- Deferral reason: `blank unless deferred`
- Unresolved dependency: `blank unless deferred`
- Dependency owner: `blank unless deferred`
- Reconsideration condition: `blank unless deferred`
- Reconsideration date: `blank unless deferred or date not yet known`
- Replacement communication-product ID: `blank unless superseded before release decision`
- Replacement communication-product version: `blank unless superseded before release decision`
- Pre-decision supersession reason: `blank unless superseded before release decision`
- Pre-decision supersession date: `blank unless superseded before release decision`
- Pre-decision supersession owner: `blank unless superseded before release decision`

Use exactly: `not yet reviewed for specified release`, `approved for specified release`, `approved for specified release with documented condition`, `not approved for specified release`, `deferred for specified release`, or `superseded before release decision`. For conditional approval, condition, why it matters, affected scope, warning, follow-up, and owner must all be substantive; `none`, `not applicable`, and empty values are not allowed for those fields. Nonapproval requires rationale, blocking concern or unmet requirement, authority, decision date, required return stage or terminal disposition, and responsible owner. Nonapproval is not withdrawal or withholding, does not imply that the scientific result is invalid, and applies only to the specified release proposal. Deferral requires reason, unresolved dependency, dependency owner, and reconsideration condition or date; it is not approval, nonapproval, or permission to release, and leaves the state `not released` unless another documented event applies. Superseded before release decision requires all replacement fields above; the state normally remains `not released`, and the replacement does not inherit readiness, review, or approval. A copied record must not imply review, approval, release, withholding, withdrawal, correction, or supersession.

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
- Withholding date: `blank unless withheld`
- Withheld audience or channel: `blank unless withheld`
- Withholding disposition: `blank unless withheld; reconsider later / terminal / replaced / other`
- Withholding reconsideration date or condition: `blank unless applicable`
- Withholding notification: `blank unless applicable`
- Previous release-record ID: `blank unless withdrawn or superseded`
- Withdrawal authority: `blank unless withdrawn`
- Withdrawal date: `blank unless withdrawn`
- Withdrawal reason: `blank unless withdrawn`
- Affected claims or uses: `blank unless withdrawn`
- Audience notification: `blank unless withdrawn`
- Replacement or next action: `blank unless withdrawn`
- Underlying results remain supported: `blank unless withdrawn; yes / no / partly / under reevaluation`
- Withdrawal required return stage: `blank unless withdrawn`
- Replacement release-record ID: `blank unless superseded`
- Replacement communication-product ID/version: `blank unless superseded`
- Supersession date: `blank unless superseded`
- Release supersession reason: `blank unless superseded`
- Release supersession owner: `blank unless superseded`

Use exactly: `not released`, `released`, `withheld`, `withdrawn`, or `superseded`.

`not released` must not contain a release date or released location. `released` requires an approved release-decision status and exact release details. `withheld` means an affirmative decision not to distribute a prepared product and requires authority, reason, date, audience/channel, disposition, and notification where applicable; it is not a synonym for not released. Withholding may follow approval only when the authority deliberately stops distribution and records why. `withdrawn` requires a previous release record and all withdrawal fields; it must not be used for a never-distributed product. `superseded` requires previous and replacement records where applicable, replacement product/version, date, reason, and owner; it remains historically identifiable and does not transfer approval, accessibility review, availability statements, or release conditions. Approval alone does not change the release state. Status-specific fields are authoritative; do not duplicate their meaning in a general summary field.

## Corrections and supersession

- Correction needed: `no / yes / unknown`
- Correction type: `typographical or formatting; no change to meaning / factual correction; no change to scientific conclusion / corrected figure or table / corrected availability, citation, or attribution statement / corrected data release / corrected code or software release / scientific correction affecting interpretation / withdrawal / publisher- or authority-defined retraction / other`
- Description: `blank until needed`
- Reason: `blank until needed`
- Affected claims: `blank until needed`
- Whether conclusions changed: `blank until needed`
- Correction authority: `blank until needed`
- Correction date: `blank until needed`
- Replacement product ID/version: `blank until needed`
- Return-to-lifecycle-stage decision: `blank until needed`

Keep the original product and release record identifiable. Do not silently overwrite history.

## Transfer to Preserve

- Preservation assessment required: `yes / no / unresolved`
- Preservation-record ID: `blank until created`
- Preservation package ID/version: `blank until created`
- Repository or preservation location: `blank until known`
- Transfer owner: `blank until assigned`
- Transfer date: `blank until completed`
- Known preservation limitation: `blank until assessed`

Release does not itself establish preservation. A public release location is not automatically the preservation repository. Preserve is authoritative for selection, deposit, verification, access, and maintenance.
