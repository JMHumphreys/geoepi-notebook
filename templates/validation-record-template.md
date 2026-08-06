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
- Started date: `REQUIRED-ISO-8601-date`
- Completed date: `optional-ISO-8601-date`
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
| `CHECK-001` | `verification/diagnostic/prediction/sensitivity/uncertainty` | `REQUIRED` | `REQUIRED` | `REQUIRED` | `planned` | `REQUIRED` | `REQUIRED` | `REQUIRED-ISO-8601-date` |

Allowed check statuses are **planned**, **completed**, **completed with limitation**, **failed**, **inconclusive**, **not applicable**, and **superseded**.

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
- Supported use: `REQUIRED-or-not_applicable`
- Unsupported use: `REQUIRED-or-not_applicable`
- Documented limitation: `REQUIRED-or-none`
- Downstream caution: `REQUIRED-or-none`
- Required follow-up: `REQUIRED-or-none`
- Reevaluation trigger: `REQUIRED`
- Return to Analyze required: `yes/no; explain`
- Replacement analysis ID: `REQUIRED-or-not_applicable`
- Decision-maker: `REQUIRED-role-or-account`
- Decision date: `REQUIRED-ISO-8601-date`

Use only these overall conclusion statuses:

- `not yet evaluated`
- `validation in progress`
- `supported for stated use`
- `supported for stated use with documented limitation`
- `evidence inconclusive`
- `not supported for stated use`
- `superseded`

This validation record does not authorize publication or release.
