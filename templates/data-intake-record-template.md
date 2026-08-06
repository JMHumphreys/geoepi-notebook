# Data intake record

> Complete one record per delivery, extraction, or intake event. Mark required fields, and use optional prompts when they help explain the delivery. Do not include credentials, PII, protected data contents, or protected agreement text.

## Required identification

- **Project ID or authoritative project context:**
- **Source ID:**
- **Snapshot/release/extraction/acquisition ID:**
- **Intake ID, if conditionally required:** For a simple one-time delivery, this may be the snapshot ID. Use a separate intake ID for repeated, corrected, multi-handler, recurring, regulated, operational, or high-consequence workflows.
- **Provider:**
- **Received by:**
- **Receipt date/time and time zone:**
- **Acquisition method:** download / transfer / API / database / field or laboratory export / other
- **Authorization, agreement, or approved-location reference:** Record a reference only; do not copy protected agreement contents into the repository.
- **Delivery description:**
- **Authoritative source location:**
- **File-manifest location, if used:** Use `not applicable` for a simple delivery without a manifest.
- **Expected versus received contents:**
- **Restrictions or license:**

## Inspection record

- **Technical inspection:** file count, sizes, readability, format, encoding, schema, archive integrity, spatial/sequence checks as applicable.
- **Content inspection:** identifiers, units, dates, geography, categories, missingness, documentation, and obvious truncation/corruption.
- **Anomalies:**
- **Clarification requests:**

## Replacement or superseded delivery

- **Prior intake or snapshot ID:**
- **Replacement intake or snapshot ID:**
- **Reason for replacement:**
- **Earlier delivery status:** rejected / superseded / unchanged pending review
- **Affected files or objects:**

## Decision

- **Status:** received / pending validation / pending clarification / accepted for staging / accepted with documented limitation / rejected / superseded
- **Decision by:**
- **Decision date:**
- **Accepted-for-staging by, if applicable:**
- **Accepted-for-staging date, if applicable:**
- **Next action:**

## Required when accepted with documented limitation

- **Limitation:**
- **Likely consequence:**
- **Downstream restriction:**
- **Responsible decision-maker:**
- **Required follow-up and due point:**
