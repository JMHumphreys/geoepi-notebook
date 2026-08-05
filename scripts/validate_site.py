"""Small checks for the draft Quarto site."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"title", "description", "status", "practice-level", "audience", "domains", "topics", "owner", "last-reviewed", "review-cycle"}
errors = []
pages = sorted(ROOT.rglob("*.qmd"))
for page in pages:
    text = page.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{page}: missing YAML front matter")
        continue
    try:
        end = text.index("\n---", 4)
        frontmatter = text[4:end]
        keys = {line.split(":", 1)[0].strip() for line in frontmatter.splitlines() if line and not line.startswith((" ", "#")) and ":" in line}
        if not keys:
            raise ValueError("no metadata keys found")
        metadata = {key: True for key in keys}
    except ValueError as exc:
        errors.append(f"{page}: malformed front matter: {exc}")
        continue
    missing = REQUIRED - set(metadata)
    if missing:
        errors.append(f"{page}: missing metadata: {', '.join(sorted(missing))}")
    for target in re.findall(r"\]\(([^)#]+(?:\.qmd|\.md))\)", text):
        if not (page.parent / target).resolve().exists():
            errors.append(f"{page}: broken internal link -> {target}")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"Validated metadata and internal links for {len(pages)} Quarto pages.")
