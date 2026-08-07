"""Small checks for the draft Quarto site."""
from pathlib import Path
import re
import sys
from html.parser import HTMLParser
from urllib.parse import parse_qs, urlparse


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"title", "description", "status", "practice-level", "audience", "domains", "topics", "owner", "last-reviewed", "review-cycle"}
errors = []


def normalize_url(value):
    parsed = urlparse(value)
    return parsed._replace(fragment="").geturl().rstrip("/")


class ResourceLinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href")
            self.current = {"href": href or "", "text": []}

    def handle_data(self, data):
        if self.current is not None:
            self.current["text"].append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self.current is not None:
            self.links.append({"href": self.current["href"], "text": " ".join(self.current["text"]).strip()})
            self.current = None


def validate_resources():
    catalog_path = ROOT / "resources" / "catalog.yml"
    page_path = ROOT / "resources" / "index.qmd"
    catalog_text = catalog_path.read_text(encoding="utf-8")
    catalog = []
    for block in re.split(r"(?m)^- id:\s*", catalog_text)[1:]:
        lines = block.splitlines()
        entry_id = lines[0].strip()
        fields = {}
        for line in lines[1:]:
            match = re.match(r"^\s+([A-Za-z0-9_]+):\s*(.*)$", line)
            if match:
                fields[match.group(1)] = match.group(2).strip().strip('"')
        fields["id"] = entry_id
        catalog.append(fields)
    if not catalog:
        errors.append(f"{catalog_path}: no catalog entries found")
        return
    ids = []
    catalog_urls = []
    seen_pairs = set()
    for entry in catalog:
        if not isinstance(entry, dict):
            errors.append(f"{catalog_path}: each catalog entry must be a mapping")
            continue
        entry_id = entry.get("id")
        title = entry.get("title")
        if not entry_id:
            errors.append(f"{catalog_path}: resource entry is missing an id")
        elif entry_id in ids:
            errors.append(f"{catalog_path}: duplicate resource id: {entry_id}")
        ids.append(entry_id)
        if not title:
            errors.append(f"{catalog_path}: {entry_id or '<unknown>'} has an empty title")
        if not entry.get("author_or_organization"):
            errors.append(f"{catalog_path}: {entry_id or '<unknown>'} is missing author_or_organization")
        if "topics" not in entry or entry.get("topics") in (None, "", []):
            errors.append(f"{catalog_path}: {entry_id or '<unknown>'} is missing topics")
        url = entry.get("url")
        if url is None:
            continue
        if not isinstance(url, str) or not url.strip():
            errors.append(f"{catalog_path}: {entry_id or '<unknown>'} has an empty URL")
            continue
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            errors.append(f"{catalog_path}: invalid resource URL for {entry_id}: {url}")
        if any(key.lower().startswith("utm_") for key in parse_qs(parsed.query)):
            errors.append(f"{catalog_path}: tracking parameter in resource URL for {entry_id}: {url}")
        pair = (title, normalize_url(url))
        if pair in seen_pairs:
            errors.append(f"{catalog_path}: duplicate title-and-URL pair for {entry_id}")
        seen_pairs.add(pair)
        catalog_urls.append(normalize_url(url))

    page_text = page_path.read_text(encoding="utf-8")
    template_match = re.search(r"template:\s*([^\s]+)", page_text)
    if template_match:
        template_path = page_path.parent / template_match.group(1)
        if template_path.exists():
            page_text += template_path.read_text(encoding="utf-8")
    for field in ("author_or_organization", "topics", "url"):
        if field not in page_text:
            errors.append(f"{page_path}: resource listing does not reference catalog field {field}")

    rendered = ROOT / "_site" / "resources" / "index.html"
    if rendered.exists():
        parser = ResourceLinkParser()
        rendered_text = rendered.read_text(encoding="utf-8")
        parser.feed(rendered_text)
        anchors = [link for link in parser.links if link["href"].startswith(("http://", "https://"))]
        expected_by_url = {}
        for entry in catalog:
            url = entry.get("url")
            if isinstance(url, str) and url.startswith(("http://", "https://")):
                expected_by_url[normalize_url(url)] = expected_by_url.get(normalize_url(url), 0) + 1
        rendered_by_url = {}
        for link in anchors:
            normalized = normalize_url(link["href"])
            if normalized in expected_by_url:
                rendered_by_url[normalized] = rendered_by_url.get(normalized, 0) + 1
        for url, expected_count in expected_by_url.items():
            if rendered_by_url.get(url, 0) != expected_count:
                errors.append(f"{rendered}: rendered anchor count for {url} is {rendered_by_url.get(url, 0)}; expected {expected_count}")
        for entry in catalog:
            url = entry.get("url")
            if not url or not isinstance(url, str) or not url.startswith(("http://", "https://")):
                continue
            matches = [
                link for link in anchors
                if normalize_url(link["href"]) == normalize_url(url)
                and re.sub(r"\s+", " ", link["text"]).strip() == re.sub(r"\s+", " ", entry.get("title", "")).strip()
            ]
            if not matches:
                errors.append(f"{rendered}: missing static resource anchor for {entry['id']}: {url}")
                continue
            if not matches[0]["text"]:
                errors.append(f"{rendered}: resource anchor has empty text for {entry['id']}")
        if re.search(r'<td class="listing-title">\s*<a\s+href=""', rendered_text):
            errors.append(f"{rendered}: empty resource-title anchor href")


validate_resources()
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
