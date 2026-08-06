# Project readiness checklist

> Mark each item pass, fail, not applicable, or exception. Link evidence rather than relying on memory.

## Project identity and planning

- [ ] Identity, objective, audience, outputs, owner, status, and authoritative location are recorded.
- [ ] README contains the concise scope statement; a separate charter exists if project triggers require one.
- [ ] Data locations, restrictions, and contacts are recorded.

## Data-intake acceptance

- [ ] Authorization, provider, source ID, and snapshot/release/extraction/acquisition ID are recorded when data are received.
- [ ] A separate intake ID is recorded when repeated, corrected, multi-handler, recurring, regulated, operational, or high-consequence intake makes it conditionally required.
- [ ] The delivered source package is preserved at an authoritative location.
- [ ] Expected and received contents, restrictions, technical inspection, and content inspection are recorded.
- [ ] Discrepancies and replacement deliveries are linked rather than silently overwritten.
- [ ] The status is recorded as received, pending validation, pending clarification, accepted for staging, accepted with documented limitation, rejected, or superseded before staging.
- [ ] If accepted with documented limitation, the limitation, consequence, downstream restriction, responsible decision-maker, and follow-up are recorded.

## Data organization and analysis readiness

- [ ] The accepted snapshot and preserved source package are distinguishable from staged and derived objects.
- [ ] Source data are preserved and provenance is documented.
- [ ] Dataset IDs, versions, key relationships, schema, units, codes, missingness, and derivations are documented.
- [ ] Consequential transformations, corrections, exclusions, code, configuration, and provenance are recoverable.
- [ ] Spatial and temporal conventions are documented where applicable.
- [ ] Structural checks, limitations, restrictions, and unresolved discrepancies are recorded.
- [ ] An authoritative analysis-ready object and responsible decision-maker are identified.
- [ ] Readiness status does not default to an approved state.
- [ ] The dataset status is recorded as **not ready for analysis**, **ready for analysis**, or **ready for analysis with documented limitation**.
- [ ] For either ready status, the readiness decision-maker and ISO 8601 decision timestamp are recorded.
- [ ] A documented limitation includes its consequence, downstream restriction, responsible decision-maker, and follow-up.

## Computational workflow preparation

- [ ] Code, configuration, parameters, and environment record are discoverable.
- [ ] Consequential manual steps and decisions are documented.
- [ ] Planned QA/QC checks and expected outputs are defined.
- [ ] This preparation is understood not to validate a model or result.

## Analysis design and execution

- [ ] The analysis objective and quantity, comparison, prediction, pattern, or simulation outcome are recorded.
- [ ] The dataset ID, version, readiness status, limitation, subset, and restrictions are recorded.
- [ ] The analysis classification is recorded as exploratory, planned primary, planned secondary, sensitivity, post hoc, or final reporting analysis as applicable.
- [ ] The method, variables, transformations, exclusions, settings, and intended outputs are recorded.
- [ ] Code, settings, software, environment, and each consequential execution are identifiable.
- [ ] Seeds, scenarios, parameter sets, partitions, and replicates are recorded where needed.
- [ ] Expected outputs are compared with outputs actually produced.
- [ ] Warnings, failures, retries, cancellations, incomplete runs, and manual recovery are visible.

## Ready for validation

- [ ] Important candidate results trace to the analysis data, analysis version, code, settings, run, and output.
- [ ] The analysis readiness status is explicitly **not ready for validation**, **ready for validation**, or **ready for validation with documented limitation**.
- [ ] A responsible analyst or reviewer and ISO 8601 decision timestamp are recorded for a ready status.
- [ ] Any documented limitation includes its consequence, downstream restriction, responsible decision-maker, and follow-up.
- [ ] The readiness decision records that validation has not yet occurred.

## Result and release review

- [ ] Results trace to inputs, code, parameters, environment, and output/run IDs.
- [ ] Clean execution/render succeeds or failure is documented.
- [ ] Limitations, restrictions, licenses, and availability statements are current.
- [ ] Appropriate review is recorded.

## Handoff and closeout events

- [ ] If responsibility changes: access, locations, known issues, unfinished work, and reproduction steps are recorded and accepted by the incoming owner.
- [ ] If work pauses indefinitely or ends: final/authoritative version and archive or retention decision are named.
- [ ] Handoff or closeout owner and date are recorded only for the corresponding event.

**Reviewer:**
**Date:**
**Exceptions:**
