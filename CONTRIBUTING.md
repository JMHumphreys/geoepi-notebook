# Contributing to the GeoEpi Lab Book

Use a branch and pull request; do not commit directly to `main`. Keep changes focused and explain how they help GeoEpi scientists or collaborators organize real work.

For substantive guidance, link to the source or experience behind the recommendation. State group conventions directly, avoid presenting them as institutional policy unless they are one, and reserve strong requirement language for genuine scientific, security, contractual, or institutional requirements.

Before opening a pull request:

1. Run `quarto render` for the complete site.
2. Run `python scripts/validate_site.py`.
3. Check internal links, downloadable templates, navigation, and the rendered page.
4. Confirm that no credentials, tokens, controlled data, generated output, or local IDE state is included.

The archived lifecycle material is preserved for future work. Do not reintroduce it as a competing top-level navigation unless the information architecture is deliberately revisited.
