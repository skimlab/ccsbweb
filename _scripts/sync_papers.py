#!/usr/bin/env python3
"""
CCSB Paper Sync Tool
Discovers publications co-authored by active CCSB members (faculty & students),
creates standardized 3:2 thumbnails (1200x805), generates Jekyll posts in papers/_posts/,
and verifies the site build.
"""

import os
import sys
import re
import json
import time
import argparse
import subprocess
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# Base directories
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PAPERS_POSTS_DIR = os.path.join(REPO_ROOT, "papers", "_posts")
IMAGES_PAPERS_DIR = os.path.join(REPO_ROOT, "images", "papers")
TEAM_POSTS_DIR = os.path.join(REPO_ROOT, "team", "_posts")

USER_AGENT = "CCSBWebPaperSync/1.0 (https://ccsb.pvamu.edu; mailto:ccsb@pvamu.edu)"

def get_active_members():
    """Extracts active faculty and student members from team/_posts/."""
    members = []
    if not os.path.exists(TEAM_POSTS_DIR):
        return members

    for filename in sorted(os.listdir(TEAM_POSTS_DIR)):
        if not filename.endswith(".md"):
            continue
        filepath = os.path.join(TEAM_POSTS_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        if not content.startswith("---"):
            continue
            
        parts = content.split("---", 2)
        if len(parts) < 3:
            continue
            
        frontmatter = parts[1]
        data = {}
        for line in frontmatter.splitlines():
            line = line.strip()
            if ":" in line:
                k, v = line.split(":", 1)
                k = k.strip()
                v = v.strip().strip('"').strip("'")
                data[k] = v
                
        # Filter: active members only (faculty or student, not associate-faculty, not retired/alumni)
        retired = data.get("retired", "false").lower() == "true"
        alumni = data.get("alumni", "false").lower() == "true"
        membership = data.get("membership", "").lower()
        
        if retired or alumni:
            continue
        if membership in ["associate-faculty", "staff"]:
            continue
        if membership not in ["faculty", "student"]:
            continue
            
        name = data.get("name")
        if name:
            members.append({
                "name": name,
                "membership": membership,
                "file": filename
            })
    return members


def get_existing_papers():
    """Reads all existing paper posts and returns sets of identifiers for deduplication."""
    existing_dois = set()
    existing_arxiv_ids = set()
    existing_titles = set()

    if not os.path.exists(PAPERS_POSTS_DIR):
        return existing_dois, existing_arxiv_ids, existing_titles

    for filename in os.listdir(PAPERS_POSTS_DIR):
        if not filename.endswith(".md"):
            continue
        filepath = os.path.join(PAPERS_POSTS_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract DOI
        doi_match = re.search(r"^doi:\s*(.+)$", content, re.MULTILINE | re.IGNORECASE)
        if doi_match:
            doi = doi_match.group(1).strip().strip('"').strip("'")
            doi_clean = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi).lower().strip()
            if doi_clean:
                existing_dois.add(doi_clean)

        # Extract arXiv ID
        arxiv_match = re.search(r"arXiv:([0-9]{4}\.[0-9]{4,5})", content, re.IGNORECASE)
        if arxiv_match:
            existing_arxiv_ids.add(arxiv_match.group(1).lower())
        arxiv_url_match = re.search(r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})", content, re.IGNORECASE)
        if arxiv_url_match:
            existing_arxiv_ids.add(arxiv_url_match.group(1).lower())

        # Extract Title
        title_match = re.search(r"^title:\s*(.+)$", content, re.MULTILINE | re.IGNORECASE)
        if title_match:
            title = title_match.group(1).strip().strip('"').strip("'")
            title_clean = re.sub(r"[^a-z0-9]", "", title.lower())
            if title_clean:
                existing_titles.add(title_clean)

    return existing_dois, existing_arxiv_ids, existing_titles


def search_crossref(member_name, year):
    """Searches Crossref API for papers matching an author in a given year."""
    papers = []
    query = urllib.parse.quote(member_name)
    url = f"https://api.crossref.org/works?query.author={query}&filter=from-pub-date:{year}-01-01&rows=30"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            items = data.get("message", {}).get("items", [])
            for item in items:
                authors = item.get("author", [])
                # Verify member is among authors
                matched = False
                author_names = []
                affiliations = []
                member_parts = member_name.lower().split()
                
                # Known CCSB and PVAMU collaborator keywords
                ccsb_keys = ["suxia cui", "lijun qian", "seungchan kim", "xishuang dong", "tesfamichael kebrom", "mgbemena", "hossain shuvo", "obiomon", "xiangfang li"]

                for a in authors:
                    given = a.get("given", "")
                    family = a.get("family", "")
                    full = f"{given} {family}".strip()
                    if full:
                        author_names.append(full)
                    for aff in a.get("affiliation", []):
                        aff_name = aff.get("name", "")
                        if aff_name:
                            affiliations.append(aff_name)

                    # Check match on target member
                    if family.lower() == member_parts[-1] and (not given or given[0].lower() == member_parts[0][0]):
                        matched = True

                if not matched:
                    continue

                # Filter out homonyms with explicit non-PVAMU affiliations and no CCSB collaborators
                has_pvamu_aff = any(re.search(r"prairie view|pvamu|texas a&m|ccsb", aff, re.I) for aff in affiliations)
                has_ccsb_coauthor = any(
                    any(k in a.lower() for k in ccsb_keys)
                    for a in author_names if a.lower() != member_name.lower()
                )
                
                if affiliations and not has_pvamu_aff and not has_ccsb_coauthor:
                    # Explicit affiliation present but neither PVAMU nor CCSB collaborator
                    continue

                title = item.get("title", [""])[0].strip()
                doi = item.get("DOI", "").strip()
                container = item.get("container-title", [""])[0].strip()
                volume = item.get("volume", "")
                issue = item.get("issue", "")
                page = item.get("page", "")

                # Published date
                pub_date = None
                for date_key in ["published-print", "published-online", "issued", "created"]:
                    date_parts = item.get(date_key, {}).get("date-parts", [[]])[0]
                    if len(date_parts) >= 1 and date_parts[0] == year:
                        y = date_parts[0]
                        m = date_parts[1] if len(date_parts) > 1 else 1
                        d = date_parts[2] if len(date_parts) > 2 else 1
                        pub_date = f"{y:04d}-{m:02d}-{d:02d}"
                        break
                
                if not pub_date:
                    continue

                abstract = item.get("abstract", "")
                # Clean JATS XML tags if present
                if abstract:
                    abstract = re.sub(r"<[^>]+>", "", abstract).strip()

                papers.append({
                    "title": title,
                    "doi": doi,
                    "authors": ", ".join(author_names) if author_names else member_name,
                    "first_author": author_names[0] if author_names else member_name,
                    "year": year,
                    "date": pub_date,
                    "venue": container,
                    "volume": volume,
                    "issue": issue,
                    "page": page,
                    "abstract": abstract,
                    "source": "crossref"
                })
    except Exception as e:
        print(f"Warning: Crossref search error for {member_name}: {e}", file=sys.stderr)

    return papers


def search_arxiv(member_name, year):
    """Searches arXiv API for preprints matching member."""
    papers = []
    member_parts = member_name.split()
    last_name = member_parts[-1]
    query = urllib.parse.quote(f"au:{last_name}")
    url = f"http://export.arxiv.org/api/query?search_query={query}&sortBy=submittedDate&sortOrder=descending&max_results=30"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            root = ET.fromstring(resp.read())
            ns = {"atom": "http://www.w3.org/2005/Atom"}
            for entry in root.findall("atom:entry", ns):
                published = entry.find("atom:published", ns)
                if published is None:
                    continue
                pub_date = published.text[:10]
                if not pub_date.startswith(str(year)):
                    continue

                authors = [a.find("atom:name", ns).text.strip() for a in entry.findall("atom:author", ns)]
                # Check if member in authors
                matched = False
                for a in authors:
                    a_parts = a.lower().split()
                    if a_parts[-1] == last_name.lower():
                        if len(member_parts) > 1 and len(a_parts) > 1:
                            if a_parts[0][0] == member_parts[0][0].lower():
                                matched = True
                        else:
                            matched = True
                if not matched:
                    continue

                title = entry.find("atom:title", ns).text.strip()
                title = re.sub(r"\s+", " ", title)
                summary = entry.find("atom:summary", ns).text.strip()
                summary = re.sub(r"\s+", " ", summary)
                id_url = entry.find("atom:id", ns).text.strip()
                arxiv_id = re.sub(r"^https?://arxiv\.org/abs/", "", id_url)
                # Strip version if needed
                arxiv_base = re.sub(r"v[0-9]+$", "", arxiv_id)

                doi = None
                doi_elem = entry.find("{http://arxiv.org/schemas/atom}doi")
                if doi_elem is not None:
                    doi = doi_elem.text.strip()

                papers.append({
                    "title": title,
                    "doi": doi or "",
                    "arxiv_id": arxiv_base,
                    "authors": ", ".join(authors),
                    "first_author": authors[0] if authors else member_name,
                    "year": year,
                    "date": pub_date,
                    "venue": f"arXiv:{arxiv_base}",
                    "pdf": f"https://arxiv.org/pdf/{arxiv_base}",
                    "abstract": summary,
                    "source": "arxiv"
                })
    except Exception as e:
        print(f"Warning: arXiv search error for {member_name}: {e}", file=sys.stderr)

    return papers


def search_europepmc(member_name, year):
    """Searches Europe PMC API for biomedical and computational biology papers."""
    papers = []
    query = urllib.parse.quote(f'AUTH:"{member_name}" PUB_YEAR:{year}')
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={query}&format=json&pageSize=25"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            results = data.get("resultList", {}).get("result", [])
            for r in results:
                title = r.get("title", "").strip().rstrip(".")
                author_string = r.get("authorString", "")
                doi = r.get("doi", "")
                pmid = r.get("pmid", "")
                pmcid = r.get("pmcid", "")
                journal = r.get("journalTitle", "")
                first_pub = r.get("firstPublicationDate", f"{year}-01-01")
                abstract = r.get("abstractText", "")

                papers.append({
                    "title": title,
                    "doi": doi,
                    "pmid": pmid,
                    "pmcid": pmcid,
                    "authors": author_string or member_name,
                    "first_author": author_string.split(",")[0].strip() if author_string else member_name,
                    "year": year,
                    "date": first_pub,
                    "venue": journal,
                    "abstract": abstract,
                    "source": "europepmc"
                })
    except Exception as e:
        print(f"Warning: Europe PMC search error for {member_name}: {e}", file=sys.stderr)

    return papers


def deduplicate_and_filter(candidates, existing_dois, existing_arxiv_ids, existing_titles):
    """Filters out candidates already in papers/_posts/ and deduplicates within candidate list."""
    seen_dois = set()
    seen_arxiv = set()
    seen_titles = set()
    unique_candidates = []

    for c in candidates:
        doi = c.get("doi", "").lower().strip()
        doi_clean = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi).strip()
        arxiv_id = c.get("arxiv_id", "").lower().strip()
        title = c.get("title", "").strip()
        title_clean = re.sub(r"[^a-z0-9]", "", title.lower())

        # Check existing posts
        if doi_clean and doi_clean in existing_dois:
            continue
        if arxiv_id and arxiv_id in existing_arxiv_ids:
            continue
        if title_clean and title_clean in existing_titles:
            continue

        # Check duplicates in current batch
        if doi_clean and doi_clean in seen_dois:
            continue
        if arxiv_id and arxiv_id in seen_arxiv:
            continue
        if title_clean and title_clean in seen_titles:
            continue

        if doi_clean:
            seen_dois.add(doi_clean)
        if arxiv_id:
            seen_arxiv.add(arxiv_id)
        if title_clean:
            seen_titles.add(title_clean)

        unique_candidates.append(c)

    return unique_candidates


def create_standard_thumbnail(image_path_or_url, dest_path, title="", authors="", venue=""):
    """
    Creates a 1200x805 (3:2) JPEG thumbnail.
    If image_path_or_url is provided, fits and pads it to canvas.
    Otherwise, renders a styled academic paper banner with CCSB colors (#4F2683 purple / #D4AF37 gold).
    """
    target_w, target_h = 1200, 805
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    if image_path_or_url and os.path.exists(image_path_or_url):
        try:
            im = Image.open(image_path_or_url).convert("RGB")
            src_w, src_h = im.size
            scale = min(target_w / src_w, target_h / src_h)
            new_w = int(src_w * scale)
            new_h = int(src_h * scale)
            resized = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
            out = Image.new("RGB", (target_w, target_h), (255, 255, 255))
            offset_x = (target_w - new_w) // 2
            offset_y = (target_h - new_h) // 2
            out.paste(resized, (offset_x, offset_y))
            out.save(dest_path, "JPEG", quality=95)
            return True
        except Exception as e:
            print(f"Error processing image {image_path_or_url}: {e}", file=sys.stderr)

    # Generate styled placeholder card
    out = Image.new("RGB", (target_w, target_h), (250, 250, 252))
    draw = ImageDraw.Draw(out)

    # Top purple banner
    draw.rectangle([(0, 0), (target_w, 48)], fill=(79, 38, 131)) # #4F2683 CCSB Purple
    # Gold accent line
    draw.rectangle([(0, 48), (target_w, 54)], fill=(212, 175, 55)) # #D4AF37 CCSB Gold

    # Center card box
    card_margin = 60
    draw.rounded_rectangle(
        [(card_margin, 100), (target_w - card_margin, target_h - card_margin)],
        radius=16,
        fill=(255, 255, 255),
        outline=(220, 224, 230),
        width=2
    )

    # Decorative icon bar
    draw.rectangle([(card_margin + 40, 150), (card_margin + 50, 230)], fill=(79, 38, 131))

    # Text wrapping helper
    def draw_wrapped_text(text, x, y, max_chars, line_height, fill):
        words = text.split()
        lines = []
        current = []
        for w in words:
            if sum(len(x) + 1 for x in current) + len(w) > max_chars:
                lines.append(" ".join(current))
                current = [w]
            else:
                current.append(w)
        if current:
            lines.append(" ".join(current))
        for line in lines[:5]:
            draw.text((x, y), line, fill=fill)
            y += line_height
        return y

    draw.text((card_margin + 70, 160), "CCSB RESEARCH PUBLICATION", fill=(120, 120, 130))
    y = draw_wrapped_text(title, card_margin + 70, 210, 48, 38, (30, 30, 40))
    y += 20
    draw.text((card_margin + 70, y), f"Authors: {authors[:90]}", fill=(90, 90, 100))
    y += 35
    if venue:
        draw.text((card_margin + 70, y), f"Venue: {venue[:80]}", fill=(79, 38, 131))

    # Bottom border
    draw.rectangle([(0, target_h - 12), (target_w, target_h)], fill=(79, 38, 131))
    out.save(dest_path, "JPEG", quality=95)
    return True


def create_paper_post(paper_data, thumbnail_img_path=None):
    """Creates a markdown post file in papers/_posts/."""
    title = paper_data.get("title", "Untitled").strip()
    pub_date = paper_data.get("date", datetime.now().strftime("%Y-%m-%d"))
    authors = paper_data.get("authors", "").strip()
    first_author = paper_data.get("first_author", "ccsb").strip()
    year = paper_data.get("year", datetime.now().year)
    venue = paper_data.get("venue", "").strip()
    doi = paper_data.get("doi", "").strip()
    arxiv_id = paper_data.get("arxiv_id", "").strip()
    pdf = paper_data.get("pdf", "").strip()
    pmid = paper_data.get("pmid", "").strip()
    pmcid = paper_data.get("pmcid", "").strip()
    abstract = paper_data.get("abstract", "").strip()

    # Generate slug
    fa_clean = re.sub(r"[^a-zA-Z0-9]", "", first_author.split()[-1].lower())
    title_words = re.findall(r"[a-zA-Z0-9]+", title.lower())
    short_title = "-".join([w for w in title_words if len(w) > 2][:5])
    slug = f"{pub_date}-{fa_clean}-{short_title}"

    post_filename = f"{slug}.md"
    post_filepath = os.path.join(PAPERS_POSTS_DIR, post_filename)
    img_filename = f"{slug}.jpg"
    img_filepath = os.path.join(IMAGES_PAPERS_DIR, img_filename)

    # Format thumbnail
    create_standard_thumbnail(thumbnail_img_path, img_filepath, title=title, authors=authors, venue=venue)

    # Build reference citation string
    author_lead = authors.split(",")[0] if authors else "Author"
    if "," in authors:
        ref_lead = f"{author_lead} et al."
    else:
        ref_lead = author_lead

    if venue:
        ref = f"{ref_lead}, {venue}, {year}"
    else:
        ref = f"{ref_lead}, {year}"

    if doi:
        ref += f" | | https://doi.org/{doi}"

    content = f"""---
layout: paper
title: "{title}"
image: /images/papers/{img_filename}
authors: {authors}
year: {year}
ref: {ref}
doi: {doi}
github: 
pdf: {pdf}
keywords: 
PMID: {pmid}
PMCID: {pmcid}
---

# Abstract

{abstract if abstract else "Abstract not available at time of indexing."}
"""

    with open(post_filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Successfully created post: {post_filepath}")
    print(f"Standardized thumbnail: {img_filepath}")
    return post_filepath, img_filepath


def run_sync(target_year=None):
    """Executes the full discovery and addition pipeline."""
    if not target_year:
        target_year = datetime.now().year

    print(f"=== CCSB Paper Sync (Year: {target_year}) ===")
    members = get_active_members()
    print(f"Found {len(members)} active CCSB members (faculty & students):")
    for m in members:
        print(f"  - {m['name']} ({m['membership']})")

    existing_dois, existing_arxiv_ids, existing_titles = get_existing_papers()
    print(f"Indexed existing posts: {len(existing_dois)} DOIs, {len(existing_arxiv_ids)} arXiv IDs, {len(existing_titles)} titles.")

    all_candidates = []
    for m in members:
        name = m["name"]
        print(f"Searching publications for {name}...")
        c_crossref = search_crossref(name, target_year)
        c_arxiv = search_arxiv(name, target_year)
        c_epmc = search_europepmc(name, target_year)
        print(f"  Found {len(c_crossref)} Crossref, {len(c_arxiv)} arXiv, {len(c_epmc)} Europe PMC records.")
        all_candidates.extend(c_crossref)
        all_candidates.extend(c_arxiv)
        all_candidates.extend(c_epmc)
        time.sleep(0.5)

    new_papers = deduplicate_and_filter(all_candidates, existing_dois, existing_arxiv_ids, existing_titles)
    print(f"\nDiscovered {len(new_papers)} new paper(s) to add.")

    added_files = []
    for paper in new_papers:
        print(f"\nAdding: {paper.get('title')}")
        post_path, img_path = create_paper_post(paper)
        added_files.append((post_path, img_path))

    return added_files


def verify_build():
    """Runs bundle exec jekyll build to verify site compilation."""
    print("Verifying site build with Jekyll...")
    try:
        res = subprocess.run(["bundle", "exec", "jekyll", "build"], cwd=REPO_ROOT, capture_output=True, text=True, check=True)
        print("Jekyll build succeeded without errors.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Jekyll build error:\n{e.stderr}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="CCSB Paper Sync Tool")
    subparsers = parser.add_subparsers(dest="command", help="Subcommand to run")

    subparsers.add_parser("get-members", help="List active CCSB faculty and student members")
    
    search_parser = subparsers.add_parser("search", help="Search for new papers")
    search_parser.add_argument("--year", type=int, default=datetime.now().year, help="Publication year")
    search_parser.add_argument("--output", type=str, default="", help="Save candidates JSON to file")

    batch_parser = subparsers.add_parser("add-batch", help="Add papers from a JSON file")
    batch_parser.add_argument("--input", type=str, required=True, help="Input JSON file containing approved papers")

    sync_parser = subparsers.add_parser("sync", help="Run full search and post addition")
    sync_parser.add_argument("--year", type=int, default=datetime.now().year, help="Publication year")

    verify_parser = subparsers.add_parser("verify-build", help="Verify Jekyll build")

    args = parser.parse_args()

    if args.command == "get-members":
        members = get_active_members()
        print(json.dumps(members, indent=2))
    elif args.command == "search":
        members = get_active_members()
        existing_dois, existing_arxiv_ids, existing_titles = get_existing_papers()
        all_candidates = []
        for m in members:
            all_candidates.extend(search_crossref(m["name"], args.year))
            all_candidates.extend(search_arxiv(m["name"], args.year))
            all_candidates.extend(search_europepmc(m["name"], args.year))
        new_papers = deduplicate_and_filter(all_candidates, existing_dois, existing_arxiv_ids, existing_titles)
        output_json = json.dumps(new_papers, indent=2)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(output_json)
            print(f"Discovered {len(new_papers)} candidate paper(s). Saved to {args.output}")
        else:
            print(output_json)
    elif args.command == "add-batch":
        with open(args.input, "r", encoding="utf-8") as f:
            papers_to_add = json.load(f)
        print(f"Adding {len(papers_to_add)} approved paper(s)...")
        for paper in papers_to_add:
            create_paper_post(paper)
        verify_build()
    elif args.command == "sync":
        added = run_sync(args.year)
        if added:
            verify_build()
    elif args.command == "verify-build":
        ok = verify_build()
        sys.exit(0 if ok else 1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
