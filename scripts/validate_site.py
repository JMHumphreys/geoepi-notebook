"""Validate the active GeoEpi Lab Book structure and internal links."""

from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
ACTIVE_DIRS = {"start", "organization", "data", "compute", "tools", "templates", "resources", "about"}
REQUIRED_TEMPLATES = {
    "project-overview-template.md",
    "data-management-plan-template.md",
    "controlled-data-inventory-template.csv",
    "subproject-registry-template.yml",
    "subproject-readme-template.md",
    "geoepi-metadata-template.yml",
}
errors = []


def active_qmd_pages():
    pages = [ROOT / "index.qmd"]
    for directory in sorted(ACTIVE_DIRS):
        pages.extend(sorted((ROOT / directory).glob("*.qmd")))
    return pages


def front_matter(text, path):
    if not text.startswith("---\n"):
        errors.append(f"{path}: missing YAML front matter")
        return set()
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        errors.append(f"{path}: malformed YAML front matter")
        return set()
    keys = set()
    for line in match.group(1).splitlines():
        if line and not line[0].isspace() and ":" in line:
            keys.add(line.split(":", 1)[0].strip())
    for key in ("title", "description"):
        if key not in keys:
            errors.append(f"{path}: active page is missing {key} metadata")
    return keys


def check_source_links(path, text):
    for raw_target in re.findall(r"\]\(([^)]+)\)", text):
        target = raw_target.strip().split("#", 1)[0].split("?", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:", "tel:", "<")):
            continue
        target_path = (path.parent / target).resolve()
        if not target_path.exists():
            errors.append(f"{path}: broken internal link -> {raw_target}")


class AnchorParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.hrefs.append(href)


def check_rendered_links():
    site = ROOT / "_site"
    if not site.exists():
        errors.append("_site: rendered site is missing; run quarto render")
        return
    search_index = site / "search.json"
    if search_index.exists():
        search_text = search_index.read_text(encoding="utf-8")
        if re.search(r'"href":"[^\"]*(archive|practices|domains|standards)/', search_text):
            errors.append(f"{search_index}: archived or superseded page appears in search index")
    for page in sorted(site.rglob("*.html")):
        parser = AnchorParser()
        parser.feed(page.read_text(encoding="utf-8"))
        for href in parser.hrefs:
            parsed = urlparse(href)
            if parsed.scheme or href.startswith("//") or href.startswith("#"):
                continue
            target = (page.parent / parsed.path).resolve()
            if parsed.path.endswith("/"):
                target = target / "index.html"
            if not target.exists():
                errors.append(f"{page}: rendered link does not resolve -> {href}")


pages = active_qmd_pages()
for page in pages:
    text = page.read_text(encoding="utf-8")
    front_matter(text, page)
    check_source_links(page, text)

template_dir = ROOT / "templates"
actual_templates = {path.name for path in template_dir.iterdir() if path.is_file() and path.name != "index.qmd"}
missing_templates = REQUIRED_TEMPLATES - actual_templates
if missing_templates:
    errors.append(f"templates: missing active templates: {', '.join(sorted(missing_templates))}")

for forbidden in ("_site", ".quarto", ".vscode", ".idea"):
    if (ROOT / forbidden).exists() and forbidden in {".vscode", ".idea"}:
        errors.append(f"{forbidden}: local IDE state should not be present")

for path in ROOT.rglob("*"):
    if not path.is_file() or "archive" in path.parts or ".git" in path.parts or ".github" in path.parts:
        continue
    if path.suffix.lower() not in {".qmd", ".md", ".yml", ".yaml", ".csv", ".py"}:
        continue
    text = path.read_text(encoding="utf-8", errors="ignore")
    if re.search(r"(?i)(password|passwd|secret|token)\s*[:=]\s*[^<\n]+", text) and path.name not in {"validate_site.py"}:
        errors.append(f"{path}: possible credential or secret material")

check_rendered_links()

if errors:
    print("\n".join(errors))
    sys.exit(1)

print(f"Validated {len(pages)} active Quarto pages, six active templates, and rendered internal links.")
