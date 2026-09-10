#!/usr/bin/env python3
"""
Generate a 1-paragraph summary/highlight of CCSB's current status
based on recent blog posts and publications, using Gemini API.
"""

import os
import re
import sys
import json
import datetime
from pathlib import Path
import urllib.request
import urllib.error

# Root directories
BASE_DIR = Path(__file__).resolve().parent.parent
BLOG_DIR = BASE_DIR / "blog" / "_posts"
PAPERS_DIR = BASE_DIR / "papers" / "_posts"
OUTPUT_FILE = BASE_DIR / "_data" / "highlight.yml"


def parse_post(file_path: Path):
    """Extract frontmatter and first few paragraphs from a Jekyll markdown post."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

    # Parse YAML frontmatter between --- and ---
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not match:
        return None

    frontmatter_text = match.group(1)
    body_text = match.group(2).strip()

    metadata = {}
    for line in frontmatter_text.splitlines():
        line = line.strip()
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            metadata[key] = val

    # Parse date from filename (YYYY-MM-DD-...) if not in frontmatter
    file_date = None
    fn_match = re.match(r"^(\d{4}-\d{2}-\d{2})", file_path.name)
    if fn_match:
        try:
            file_date = datetime.date.fromisoformat(fn_match.group(1))
        except ValueError:
            pass

    title = metadata.get("title", file_path.stem)
    author = metadata.get("author") or metadata.get("authors", "")

    # Clean up body text for summary context (first 600 characters)
    clean_body = re.sub(r"!\[.*?\]\(.*?\)", "", body_text)
    clean_body = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", clean_body)
    clean_body = re.sub(r"<[^>]+>", "", clean_body)
    clean_body = re.sub(r"\s+", " ", clean_body).strip()
    excerpt = clean_body[:500]

    category = "blog" if "blog" in file_path.parts else "papers"
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", file_path.stem)
    url = f"/{category}/{slug}/"

    return {
        "title": title,
        "author": author,
        "date": file_date,
        "date_str": file_date.isoformat() if file_date else "",
        "filename": file_path.name,
        "excerpt": excerpt,
        "category": category,
        "url": url,
    }


def get_recent_entries():
    """Collect the latest blog posts and publications."""
    blog_posts = []
    if BLOG_DIR.exists():
        for p in BLOG_DIR.glob("*.md"):
            post = parse_post(p)
            if post and post["date"]:
                blog_posts.append(post)

    papers = []
    if PAPERS_DIR.exists():
        for p in PAPERS_DIR.glob("*.md"):
            paper = parse_post(p)
            if paper and paper["date"]:
                papers.append(paper)

    blog_posts.sort(key=lambda x: x["date"], reverse=True)
    papers.sort(key=lambda x: x["date"], reverse=True)

    # Take top recent entries (up to 4 blog posts/grants and 4 papers)
    recent_blogs = blog_posts[:4]
    recent_papers = papers[:4]

    return recent_blogs, recent_papers


def call_gemini(prompt: str, api_key: str) -> str:
    """Call Google Gemini API using standard urllib."""
    models_to_try = [
        "gemini-2.5-flash",
        "gemini-1.5-flash",
    ]

    for model in models_to_try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.3,
                "maxOutputTokens": 2000,
                "thinkingConfig": {
                    "thinkingBudget": 0
                }
            }
        }

        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                candidates = data.get("candidates", [])
                if candidates:
                    parts = candidates[0].get("content", {}).get("parts", [])
                    # In newer Gemini versions, thought parts might have thought: True
                    # Look for non-thought part or concatenate text parts without thought
                    text_parts = []
                    for part in parts:
                        if not part.get("thought"):
                            text_parts.append(part.get("text", ""))
                    text = "".join(text_parts).strip()
                    if not text and parts:
                        text = parts[-1].get("text", "").strip()
                    if text.startswith('"') and text.endswith('"'):
                        text = text[1:-1].strip()
                    if text:
                        return text
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="ignore")
            print(f"Gemini API ({model}) HTTP Error {e.code}: {err_body}")
            continue
        except Exception as e:
            print(f"Gemini API ({model}) failed: {e}")
            continue

    return ""


def generate_fallback_summary(recent_blogs, recent_papers) -> str:
    """Deterministic fallback if API key is not provided or network is offline."""
    top_grant_or_blog = recent_blogs[0] if recent_blogs else None
    top_paper = recent_papers[0] if recent_papers else None

    parts = [
        "The Center for Computational Systems Biology (CCSB) at Prairie View A&M University continues to advance high-impact research at the intersection of computational sciences, genomics, and artificial intelligence."
    ]

    if top_grant_or_blog:
        author_name = top_grant_or_blog.get('author') or 'center researchers'
        parts.append(
            f"Recent highlights include milestone funding and research initiatives led by **{author_name}** such as '{top_grant_or_blog['title']}'."
        )
    if top_paper:
        author_name = top_paper.get('author') or 'faculty'
        parts.append(
            f"Concurrently, **{author_name}** published new findings in '{top_paper['title']}', underscoring CCSB's ongoing contributions to scientific discovery and student training."
        )

    return " ".join(parts)


def format_yaml_multiline(text: str, indent: int = 2) -> str:
    """Format string as YAML multiline block scalar."""
    lines = text.split("\n")
    pad = " " * indent
    return "\n".join(pad + line for line in lines)


def make_label(item, item_type: str) -> str:
    """Generate a clean, compact label for badges/buttons."""
    author = item.get("author", "").split(",")[0].strip()
    title = item.get("title", "")
    if item_type == "paper":
        short_title = title.split(":")[0] if ":" in title else title
        if len(short_title) > 32:
            short_title = short_title[:30].rsplit(" ", 1)[0] + "..."
        if author:
            last_name = author.split()[-1]
            return f"Paper: {short_title} ({last_name})"
        return f"Paper: {short_title}"
    else:
        if "NSF" in title:
            return f"NSF RIA Grant ({author})"
        elif "TAMUS" in title or "REF" in title:
            return f"TAMUS REF Grant ({author})"
        elif "RISE" in title:
            return f"RISE Grant ({author})"
        elif "Seminar" in title:
            return f"Seminar: {author}"
        short_title = title.split(":")[0] if ":" in title else title
        if len(short_title) > 32:
            short_title = short_title[:30].rsplit(" ", 1)[0] + "..."
        return f"{short_title} ({author})" if author else short_title


def main():
    print("CCSB Weekly Highlight Generator")
    print("--------------------------------")

    recent_blogs, recent_papers = get_recent_entries()
    print(f"Found {len(recent_blogs)} recent blog posts and {len(recent_papers)} recent papers.")

    now = datetime.datetime.now()
    monday = now - datetime.timedelta(days=now.weekday())
    period_str = f"Week of {monday.strftime('%B %-d, %Y')}"
    updated_at_str = now.strftime("%Y-%m-%d")

    # Build prompt context
    context_lines = ["Recent Center Announcements & Grants:"]
    for b in recent_blogs:
        context_lines.append(f"- [{b['date_str']}] {b['title']} (Author/PI: {b['author']}): {b['excerpt']}")

    context_lines.append("\nRecent Center Publications:")
    for p in recent_papers:
        context_lines.append(f"- [{p['date_str']}] {p['title']} (Authors: {p['author']}): {p['excerpt']}")

    context_text = "\n".join(context_lines)

    prompt = (
        "You are a scientific communications writer for the Center for Computational Systems Biology (CCSB) "
        "at Prairie View A&M University (PVAMU).\n\n"
        "Based on the following recent center publications, grants, and announcements, write a concise, engaging, "
        "and professional 1-paragraph summary (approx. 70-110 words) highlighting the center's current research status, "
        "recent breakthroughs, and active scientific directions.\n\n"
        "Guidelines:\n"
        "- Exactly one cohesive paragraph.\n"
        "- Bold and highlight the names of all researchers, faculty, PIs, and authors mentioned using markdown bold syntax (e.g., **Dr. Md Hossain Shuvo**, **Dr. Victoria Mgbemena**, **Dr. Tesfamichael Kebrom**, **Dr. Seungchan Kim**).\n"
        "- Maintain an academic yet accessible, proud tone.\n"
        "- Do NOT include headers, bullet points, introductory phrases (like 'Here is a summary'), or quotation marks.\n\n"
        f"Context:\n{context_text}"
    )

    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    summary = ""

    if api_key:
        print("Calling Gemini API...")
        summary = call_gemini(prompt, api_key)
    else:
        print("No GEMINI_API_KEY found in environment.")

    if not summary:
        print("Using fallback summary...")
        summary = generate_fallback_summary(recent_blogs, recent_papers)

    print("\nGenerated Summary:")
    print(summary)
    print()

    # Create YAML structure
    yaml_lines = [
        f"# Auto-generated by _scripts/generate_weekly_highlight.py on {updated_at_str}",
        f'updated_at: "{updated_at_str}"',
        f'period: "{period_str}"',
        'summary: >',
        format_yaml_multiline(summary, indent=2),
        "recent_highlights:",
    ]

    for b in recent_blogs[:2]:
        safe_title = b["title"].replace('"', '\\"')
        label = make_label(b, "blog").replace('"', '\\"')
        yaml_lines.append(f'  - title: "{safe_title}"')
        yaml_lines.append(f'    label: "{label}"')
        yaml_lines.append(f'    url: "{b["url"]}"')
        yaml_lines.append(f'    type: "blog"')
        yaml_lines.append(f'    date: "{b["date_str"]}"')

    for p in recent_papers[:2]:
        safe_title = p["title"].replace('"', '\\"')
        label = make_label(p, "paper").replace('"', '\\"')
        yaml_lines.append(f'  - title: "{safe_title}"')
        yaml_lines.append(f'    label: "{label}"')
        yaml_lines.append(f'    url: "{p["url"]}"')
        yaml_lines.append(f'    type: "paper"')
        yaml_lines.append(f'    date: "{p["date_str"]}"')

    yaml_content = "\n".join(yaml_lines) + "\n"

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(yaml_content, encoding="utf-8")
    print(f"Saved highlight to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
