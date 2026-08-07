# End-to-end lifecycle review

This internal review record documents a consistency and usability review of the GeoEpi research lifecycle. It is not a new Lab Book page, an institutional approval, or a records-retention policy.

## Scope

- Starting commit: `0b089647fb555208b659d9c47368ee83c9ee4231` on `main`.
- Branch: `feature/lifecycle-consistency-plain-language-resources`.
- Pages reviewed: 62 rendered Quarto pages, including the eight lifecycle landing pages, Start Here pages, all lifecycle subpages, Resources, Templates, and linked guidance.
- Templates reviewed: 24 raw templates, plus the Templates index and authoring template.
- Catalog entries reviewed: 47 entries in `resources/catalog.yml`.
- Configuration and validation reviewed: `_quarto.yml`, `scripts/validate_site.py`, metadata requirements, internal-link checks, and raw-template publishing.
- Commands used: `python scripts/validate_site.py`; `quarto render`; `git diff --check`; targeted searches for controlled statuses, stale stage references, technical jargon, and template-to-record links.
- Rendered-site checks: the home page, Start Here, Research Practices, all eight lifecycle landing pages, Resources, Templates, representative subpages, raw-template links, Mermaid diagrams, tables, sidebars, search-index output, resource URL cells, and the resource-link enhancement script were inspected in generated HTML. Long status labels, tables, sidebar content, and raw-template links were checked structurally for narrow-width risks. Interactive local-file browser inspection was unavailable in this environment, so this is not a claim of full accessibility conformance or a substitute for human visual review.

## Review categories and finding statuses

Issues are classified as lifecycle inconsistency, status inconsistency, terminology inconsistency, duplicated requirement, missing cross-link, unclear authority, disproportionate requirement, template mismatch, resource-page defect, rendering defect, accessibility issue, editorial issue, or unresolved institutional question.

Finding statuses are **identified**, **corrected**, **retained with rationale**, **institutional decision required**, and **deferred**.

| Finding ID | Location | Category | Finding | Scientific or practical consequence | Resolution | Files changed | Status |
|---|---|---|---|---|---|---|---|
| E2E-001 | `resources/index.qmd` | resource-page defect | The listing requested `author` and `categories`, while the catalog defines `author_or_organization` and `topics`; the URL was not displayed. | Scientists could not reliably see who issued a resource or open its source landing page. | Use the catalog field names and include a visible URL/source field. | `resources/index.qmd` | corrected |
| E2E-002 | `scripts/validate_site.py` and rendered Resources page | resource-page defect | Existing validation did not check that catalog URLs became rendered hyperlinks. | A catalog could appear complete while source links were absent. | Validate catalog structure locally and, when rendered HTML exists, compare catalog URLs with external anchors. | `scripts/validate_site.py` | corrected |
| E2E-003 | Collaborate shared-records guidance | missing cross-link | The page still described Preserve as a future stage after Preserve was implemented. | Contributors could miss preservation of unreleased or restricted history. | Link the completed Preserve stage and retain return-path language. | `practices/collaborate/working-agreements-and-shared-records.qmd` | corrected |
| E2E-004 | Preserve package guidance | terminology inconsistency | “Artifact” was used without an immediate audience-level definition. | Readers could interpret the term as requiring a specialized archival object model. | Define it as a retained file, dataset, record, code version, or other project material. | `practices/preserve/preservation-packages-manifests-and-metadata.qmd` | corrected |
| E2E-005 | Lifecycle landing pages and transitions | lifecycle inconsistency | Stage functions, gates, safe defaults, authoritative records, and return paths were compared end to end. | The main risk was semantic drift between adjacent stages, especially release versus preservation and analysis versus validation. | Retain distinct boundaries; record the transition matrix below as the review baseline. | none beyond targeted fixes | retained with rationale |
| E2E-006 | Status and template vocabulary | status inconsistency | Similar words such as ready, approved, released, deposited, and verified describe different decisions. | Collapsing them could imply scientific approval or evidence that was not recorded. | Retain separate controlled vocabularies and authoritative-record assignments. | none beyond existing refined guidance | retained with rationale |
| E2E-007 | Templates and cross-stage records | template mismatch | Small projects can satisfy several information requirements in one durable record; high-consequence work may need separate records. | A one-file-per-concept interpretation would be disproportionate, while copied summaries could obscure authority. | Retain proportionality and link summaries to authoritative records. | none beyond existing templates | retained with rationale |
| E2E-008 | Institutional review | unresolved institutional question | The Lab Book does not itself assign records, privacy, repository, community, or release authority. | Human review is needed before any proposed minimum is adopted. | Add a review guide that separates scientific guidance, proposed lab minimum, institutional authority, unresolved decisions, and optional stronger practice. | `docs/institutional-review-guide.md` | corrected |

## Lifecycle boundaries

| Stage | Primary function | Boundary retained in review |
|---|---|---|
| Plan | Purpose, question, intended use, scope, responsibilities, anticipated data, analysis approach, risks, and completion criteria. | Planning does not claim that data were acquired, organized, analyzed, or validated. |
| Acquire | Collection or receipt, source identity, snapshot/extraction, permissions, intake checks, and acceptance into project storage. | Intake acceptance does not make data analysis-ready or scientifically valid. |
| Organize | Structure, identifiers, schema, provenance, spatial/temporal conventions, controlled transformations, and analysis readiness. | Organization does not answer the scientific question or validate a method. |
| Analyze | Analysis design, execution, outputs, computational record, and result traceability. | A produced result is not thereby supported for consequential use. |
| Validate | Assumptions, diagnostics, performance, sensitivity, uncertainty, validation evidence, and intended-use decision. | Validation does not establish collaboration agreement, release approval, or preservation. |
| Collaborate | Roles, review, disagreement, contributions, credit, partner conditions, continuity, and readiness to communicate. | Collaboration readiness does not authorize release. |
| Communicate | Audience, purpose, claims, products, reporting, visual presentation, availability, release review, release decision/event, corrections, and supersession. | Release does not establish long-term preservation. |
| Preserve | Selection, package, deposit, verification, integrity, authorized access continuity, migration, maintenance, and deaccession. | Preserve does not establish retention law, authorize destruction, or guarantee permanent execution. |

The lifecycle is iterative rather than strictly linear. Problems can return work to an earlier stage: acquisition problems to Plan or Acquire; organization problems to Acquire; changed inputs or methods to Analyze; changed interpretation or support to Validate; contributor or partner changes to Collaborate; changed product packages to Communicate; and changed preservation packages to renewed preservation verification.

## Transition inventory

| Transition | Outgoing evidence | Receiving stage accepts | Safe or limited path |
|---|---|---|---|
| Plan → Acquire | source, permissions, anticipated data, intake criteria, and responsible person are identified | a collection or receipt can be recorded and inspected | unresolved scope returns to Plan |
| Acquire → Organize | source identity, received snapshot/extract, restrictions, and intake status are recorded | accepted-for-staging data, including documented limitations | rejected or unclear intake remains in Acquire or returns to Plan |
| Organize → Analyze | schema, identifiers, provenance, spatial/temporal conventions, and readiness decision are recorded | ready or ready-with-documented-limitation data | not-ready data remain visible and return to Organize or Acquire |
| Analyze → Validate | analysis version, inputs, settings, run, output, and result trace are identified | candidate results with an intended-use question | failed or incomplete runs remain in Analyze |
| Validate → Collaborate | validation evidence and scoped conclusion are recorded | a result and limitation set that collaborators can review | changed support returns to Validate; changed method returns to Analyze |
| Collaborate → Communicate | roles, contributions, partner conditions, review responses, and communication readiness are recorded | a product with claims, audience, and review context | unresolved contributor or partner issues remain in Collaborate |
| Communicate → Preserve | product/release/correction records identify exact versions and access conditions | selected released, unreleased, restricted, negative, or inconclusive materials | changed product returns to Communicate; changed preservation scope reopens Preserve |

## Controlled status inventory

The following vocabularies remain separate because they answer different scientific or operational questions. A safe default does not represent completed work.

| Stage / record | Exact allowed values | Safe default | Nondefault evidence or replacement rule |
|---|---|---|---|
| Project status / README | project-specific current status, with the authoritative project record identified | blank until assessed | Do not treat the README summary as replacing a decision record. |
| Intake acceptance | `received`; `pending validation`; `pending clarification`; `accepted for staging`; `accepted with documented limitation`; `rejected`; `superseded` | `received` | Acceptance has a responsible decision-maker; limitations carry forward; superseded deliveries identify the replacement. |
| Analysis readiness | `not ready for analysis`; `ready for analysis`; `ready for analysis with documented limitation` | `not ready for analysis` | Readiness requires the organization/readiness record; limitation fields are substantive. |
| Analysis/result | `planned`; `produced`; `incomplete`; `candidate for validation`; `failed`; `superseded` | `planned` | Candidate results identify validation scope; failures and supersession remain identifiable. |
| Validation checks | `planned`; `completed`; `completed with limitation`; `failed`; `inconclusive`; `not applicable`; `superseded` | `planned` | Completed, failed, and inconclusive checks require evidence, finding, reviewer/analyst, and date. |
| Validation conclusion | `not yet evaluated`; `validation in progress`; `supported for stated use`; `supported for stated use with documented limitation`; `evidence inconclusive`; `not supported for stated use`; `superseded` | `not yet evaluated` | Decision-maker and date are required for substantive conclusions; supersession identifies a replacement. |
| Collaboration readiness | `not ready for communication`; `ready for communication`; `ready for communication with documented limitation` | `not ready for communication` | The collaboration agreement or equivalent record is authoritative; limitation fields are substantive. |
| Product preparation | `planned`; `in preparation`; `under review`; `revision required`; `ready for release review`; `superseded` | `planned` | Preparation does not approve release; superseded products identify replacements. |
| Claim review | `proposed`; `under review`; `accepted for current product`; `revision required`; `removed`; `superseded` | `proposed` | Accepted consequential claims link results and validation; removed/superseded claims retain rationale or replacement. |
| Communication review | `planned`; `in progress`; `completed`; `superseded` | `planned` | Completed consequential review records finding, response, owner, and date; review is not approval. |
| Release-review readiness | `not ready for release review`; `ready for release review`; `ready for release review with documented limitation` | `not ready for release review` | Exact product/package, claims, evidence, restrictions, and authority are identified. |
| Release decision | `not yet reviewed for specified release`; `approved for specified release`; `approved for specified release with documented condition`; `not approved for specified release`; `deferred for specified release`; `superseded before release decision` | `not yet reviewed for specified release` | Approval is scoped to an exact package and authority; conditional, nonapproval, deferral, and supersession fields are substantive. |
| Release state | `not released`; `released`; `withheld`; `withdrawn`; `superseded` | `not released` | Released requires an approved exact version and event; withdrawn requires a previous release; superseded identifies replacement. |
| Preservation selection | `not yet assessed for preservation`; `selected for preservation`; `not selected for long-term preservation`; `preservation decision deferred`; `superseded preservation decision` | `not yet assessed for preservation` | Selection, nonselection, deferral, and supersession each require their specified authority, scope, date, custody, and replacement fields. Nonselection never authorizes destruction. |
| Preservation outcome | `not deposited`; `deposited`; `verified`; `verified with documented limitation`; `deposit rejected`; `deaccessioned`; `superseded` | `not deposited` | Deposit requires receipt; verification requires deposit and evidence; rejection requires attempted submission and safe custody; deaccession requires prior deposit and authority; supersession requires replacement. |
| Manifest inclusion | `planned for inclusion`; `included`; `externally referenced`; `excluded with rationale`; `unavailable`; `superseded` | `planned for inclusion` | Path, durable identifier, rationale, limitation, or replacement is required according to status. |
| Manifest verification | `not verified`; `verified`; `verified with limitation`; `failed`; `not applicable` | `not verified` | Verification evidence, limitation, failure response, or genuine nonapplicability is recorded in the manifest or linked preservation record. |
| Preservation event | `planned`; `completed`; `completed with documented limitation`; `failed`; `superseded` | `planned` | A completed event identifies source, result, reason, process, validation, information changed, and earlier-version availability. |

## Authoritative records

| Decision or condition | Authoritative record |
|---|---|
| Project scope and responsibility | Project README or charter |
| Data intake acceptance | Data-intake record |
| Analysis readiness | Organization/readiness record |
| Analysis execution | Execution or run record |
| Result identity | Result-traceability record |
| Validation conclusion | Validation record |
| Collaboration readiness | Collaboration agreement or equivalent |
| Contributions and credit | Contribution record |
| Communication-product readiness | Communication-product record |
| Release decision and event | Release record |
| Preservation selection and outcome | Preservation plan and record |
| Package contents | Preservation-package manifest |
| Project end or indefinite pause | Closeout record |
| Transfer of responsibility | Handoff record |

Summaries in a README, closeout record, or readiness checklist point to these records; they do not silently replace them.

## Plain language, examples, and proportionality

The review retained scientific terms such as estimand, forecast horizon, coordinate reference system, convergence, posterior, random seed, replicate, sensitivity, and uncertainty because they carry meaning for the intended audience. Software and archival terms remain only where they name a real practice or standard, and are defined when they could be misunderstood. The revised Preserve package page defines “artifact” in ordinary project terms.

Examples were checked for ecological field work, disease surveillance, county-week epidemiology, spatial/raster analysis, Bayesian models, stochastic simulation, genomics, laboratory/sensor data, operational forecasts, and HPC. The guidance retains proportionality: one durable record may satisfy several requirements; a small internal analysis need not create a separate formal record for each stage; a DOI, BagIt package, RO-Crate, public release, or preservation of every intermediate file is not universal.

## Resource-page review

The root cause was a schema mismatch between the listing fields and `resources/catalog.yml`. The page now uses `author_or_organization`, `topics`, `resource_type`, `review_status`, and `url`, while the catalog remains authoritative. The validator checks unique IDs, titles, URL syntax, tracking parameters, duplicate title/URL pairs, required author/topic fields, and rendered anchor coverage when `_site/resources/index.html` exists. It does not perform live external link checks.

## Navigation and rendered-site review

The lifecycle order is Plan → Acquire → Organize → Analyze → Validate → Collaborate → Communicate → Preserve, with Preserve last and no ninth stage. Landing-page starting points, sidebar order, previous/next navigation, search text, raw-template links, and links from Communicate to Preserve were checked. The rendered review specifically inspected long controlled-status labels, tables, callouts, Mermaid diagrams, external resource links, raw Markdown/CSV links, and narrow-width wrapping. The review does not claim complete accessibility conformance or permanent external-link availability.

## Open institutional questions

- Which institutional records schedules, funder terms, contracts, data-use agreements, privacy/security rules, and community governance requirements apply to each project class?
- Which roles may make retention, release, access, repository, deaccession, and supersession decisions?
- Which repositories and storage services are approved for restricted, proprietary, Indigenous, Tribal, community-governed, or sensitive ecological materials?
- Who funds continuing storage, migration, repository fees, and successor ownership?
- What accessibility and language standards should the Lab adopt for public and internal products?

These questions remain intentionally unresolved; the Lab Book does not invent answers.
