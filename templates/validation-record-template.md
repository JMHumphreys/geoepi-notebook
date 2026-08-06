# Validation record

Replace clearly marked values. Do not include credentials or protected data.

## Identification

- Validation ID: `REQUIRED-validation-id`
- Analysis ID: `REQUIRED-analysis-id`
- Analysis version: `REQUIRED-version`
- Candidate result IDs: `REQUIRED-list`
- Validation-plan reference: `REQUIRED-path-or-reference`
- Responsible analyst: `REQUIRED-role-or-account`
- Reviewer: `optional`
- Started date: `blank until validation begins; ISO 8601 when populated`
- Completed date: `blank until validation is completed; ISO 8601 when populated`
- Current conclusion status: `not yet evaluated`

## Validation scope

- Intended use: `REQUIRED`
- Population or system: `REQUIRED`
- Geographic scope: `REQUIRED`
- Temporal scope: `REQUIRED`
- Spatial and temporal support: `REQUIRED`
- Forecast horizon: `optional-or-not_applicable`
- Limitations carried into validation: `none or describe`

## Check record

| Check ID | Category | Question | Method or evidence | Finding | Status | Evidence location | Reviewer | Date |
|---|---|---|---|---|---|---|---|---|
| `CHECK-001` | `verification/diagnostic/prediction/sensitivity/uncertainty` | `REQUIRED` | `planned method or evidence` | `blank until assessed` | `planned` | `blank until evidence exists` | `optional until reviewed` | `blank until performed` |

Allowed check statuses are **planned**, **completed**, **completed with limitation**, **failed**, **inconclusive**, **not applicable**, and **superseded**. Completed, failed, or inconclusive checks require a finding, evidence location, responsible analyst or reviewer, and date.

## Evidence summary

- Evidence supporting the result: `REQUIRED-or-none`
- Evidence challenging the result: `REQUIRED-or-none`
- Failed checks: `REQUIRED-or-none`
- Inconclusive checks: `REQUIRED-or-none`
- Missing evidence: `REQUIRED-or-none`
- Sensitivity findings: `REQUIRED-or-not_applicable`
- Uncertainty implications: `REQUIRED-or-not_applicable`
- Reviewer comments: `REQUIRED-or-none`

## Overall conclusion

- Conclusion status: `not yet evaluated`
- Supported use: `blank until a conclusion is recorded; not applicable for unsupported conclusions`
- Unsupported use: `blank until a conclusion is recorded; not applicable for supported conclusions`
- Documented limitation: `blank until a conclusion is recorded; none or describe`
- Downstream caution: `blank until a conclusion is recorded; none or describe`
- Required follow-up: `blank until a conclusion is recorded; none or describe`
- Reevaluation trigger: `blank until a conclusion is recorded; none or describe`
- Return to Analyze required: `blank until a conclusion is recorded; yes/no and explain`
- Replacement validation ID: `REQUIRED-or-not_applicable`
- Replacement analysis ID: `REQUIRED-or-not_applicable`
- Decision-maker: `blank until a conclusion is recorded`
- Decision date: `blank until a conclusion is recorded; ISO 8601 when populated`

The started date is required once validation begins. The completed date is required for a completed substantive conclusion. Decision-maker and decision date remain blank while the status is **not yet evaluated** or **validation in progress**. They are required when the status becomes **supported for stated use**, **supported for stated use with documented limitation**, **evidence inconclusive**, **not supported for stated use**, or **superseded**.

Use only these overall conclusion statuses:

- `not yet evaluated`
- `validation in progress`
- `supported for stated use`
- `supported for stated use with documented limitation`
- `evidence inconclusive`
- `not supported for stated use`
- `superseded`

Supersession may refer to a newer validation record for this analysis version or to a validation record for a replacement analysis version. The earlier record must be preserved, and its conclusion does not transfer automatically.

This validation record does not authorize publication or release.
