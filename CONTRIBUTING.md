# Contributing to the GeoEpi Lab Book

Contributions use a branch and pull request; do not commit directly to the default branch. Use focused names such as `docs/topic-name` or `feature/template-name`.

Substantive pages must use the metadata convention. Write original text, cite the evidence or source basis with URL, author or organization, access date, and relevant section where possible. State whether the change creates or alters a lab requirement, and update affected templates or catalog entries.

Reviewers should check scientific accuracy, proportionality, accessibility, provenance, licensing, and whether uncertainty is visible. A pull request cannot turn draft text into approved policy by itself.

Install Quarto and run `quarto preview` for local work or `quarto render` for a complete build. The validation workflow checks metadata and YAML. `_site/` output is ignored and should not be committed.

R and `renv` are deferred: this first pass has no executable R content and does not require an R package environment.
