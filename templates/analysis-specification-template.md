# Analysis specification

Replace clearly marked values. Do not include credentials or protected data. Not every field is required for every project; use `not_applicable` or explain why a field is omitted.

## Identification

- Project ID: `REQUIRED-replace-me`
- Analysis ID: `REQUIRED-analysis-id`
- Analysis version: `REQUIRED-version`
- Title: `REQUIRED-short descriptive title`
- Responsible analyst: `REQUIRED-role-or-account`
- Collaborators or reviewers: `optional`
- Current status: `planned`
- Date created: `REQUIRED-ISO-8601-date`
- Date last revised: `optional-ISO-8601-date`

## Purpose

- Scientific or operational objective: `REQUIRED-state the purpose`
- Analysis category: `descriptive | comparative | explanatory | inferential | predictive | forecasting | decision-support | simulation | method development | sensitivity`
- Intended audience or decision: `REQUIRED-or-not_applicable`
- Primary question: `REQUIRED-question`
- Secondary questions: `optional-list`

## Target

- Population or system: `REQUIRED-or-not_applicable`
- Unit of observation: `REQUIRED-or-not_applicable`
- Unit of analysis: `REQUIRED-or-not_applicable`
- Unit of inference: `REQUIRED-or-not_applicable`
- Outcome or response: `REQUIRED-or-not_applicable`
- Comparison or contrast: `REQUIRED-or-not_applicable`
- Prediction target or forecast horizon: `REQUIRED-or-not_applicable`
- Spatial support: `REQUIRED-or-not_applicable`
- Temporal support: `REQUIRED-or-not_applicable`
- Uncertainty quantity to report: `REQUIRED-or-not_applicable`

## Data

- Dataset IDs and versions: `REQUIRED-record each input`
- Readiness status: `ready for analysis | ready for analysis with documented limitation`
- Readiness limitations: `REQUIRED-none or describe`
- Authoritative location: `REQUIRED-reference`
- Intended subset: `optional`
- Planned joins: `optional`
- Planned exclusions: `optional`
- Restrictions: `REQUIRED-public, restricted, or agreement reference`

## Planned method and settings

- Method or model family: `REQUIRED-describe in ordinary language`
- Variables: `REQUIRED-response, predictors, confounders, or not_applicable`
- Transformations: `optional`
- Interactions: `optional`
- Offsets or denominators: `optional`
- Weights: `optional`
- Spatial structure: `optional`
- Temporal structure: `optional`
- Grouping or hierarchical structure: `optional`
- Missing-data treatment: `REQUIRED-or-not_applicable`
- Consequential software or package: `optional`
- Settings or parameter record: `REQUIRED-reference`

## Randomness and scenarios

- Deterministic or stochastic: `REQUIRED`
- Seed plan: `REQUIRED-or-not_applicable`
- Scenario IDs: `optional`
- Parameter-set IDs: `optional`
- Replicate plan: `optional`
- Partition or resampling plan: `optional`

## Intended outputs

- Tables: `optional`
- Figures: `optional`
- Maps: `optional`
- Estimates: `optional`
- Predictions or forecasts: `optional`
- Simulation summaries: `optional`
- Operational products: `optional`

## Analysis classification

Mark all that apply and explain overlaps:

- [ ] Exploratory
- [ ] Planned primary
- [ ] Planned secondary
- [ ] Sensitivity
- [ ] Post hoc
- [ ] Final reporting analysis

## Changes

| Date | Change | Reason | Information that prompted it | Responsible person | New analysis version | Classification after change |
|---|---|---|---|---|---|---|
| `ISO-8601-date` | `REQUIRED-or-none` | `REQUIRED-or-not_applicable` | `REQUIRED-or-not_applicable` | `REQUIRED-or-not_applicable` | `REQUIRED-or-not_applicable` | `REQUIRED-or-not_applicable` |

## Readiness for validation

- Current status: `not ready for validation`
- Decision-maker: `blank until reviewed`
- Decision date: `blank until reviewed; ISO 8601 when recorded`
- Limitations: `none or describe consequence, restriction, decision-maker, and follow-up`

This specification records analysis design and execution readiness. It does not establish model validity, predictive accuracy, scientific correctness, or that validation has occurred.
