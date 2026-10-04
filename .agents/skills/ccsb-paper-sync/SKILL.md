---
name: ccsb-paper-sync
description: >-
  Searches for publications co-authored by active CCSB members (faculty and students, excluding associate members),
  deduplicates against existing papers, formats standard 3:2 landscape thumbnails (1200x805),
  generates Jekyll post files in papers/_posts/, and validates the site build.
---

# CCSB Paper Sync Skill

## Overview

This skill automates discovering newly published papers co-authored by current Center for Computational Systems Biology (CCSB) members, formatting them into Jekyll paper posts, standardizing their thumbnail cards, and ensuring the website compiles without errors.

## Principles & Rules

1. **Active Members Only**:
   - Queries only active faculty and student members listed in `team/_posts/*.md`.
   - Excludes associate members (`membership: associate-faculty`), staff, and alumni/retired members.
2. **Authorship**:
   - Any co-authored paper with an active CCSB member is eligible (no positional restrictions).
3. **Deduplication**:
   - Checks DOIs, arXiv IDs, and normalized titles against all existing posts in `papers/_posts/`.
4. **Mandatory Approval for Antigravity Agent**:
   - **When running as an Antigravity agent, the agent MUST ALWAYS ask for user approval before creating posts or thumbnail files.**
   - Never write to `papers/_posts/` or `images/papers/` until the user has reviewed the candidate list and explicitly approved the additions.
5. **Standardized Thumbnails**:
   - All thumbnail images must be strictly saved to `images/papers/` with an exact 3:2 landscape aspect ratio (`1200×805` px) on a clean white background.
   - For open-access papers, extract key figures from the PDF.
   - For paywalled or figure-less papers, synthesize an academic methodology diagram using `generate_image` or the built-in Pillow card renderer.
6. **Validation**:
   - Always run `bundle exec jekyll build` after adding posts to verify zero build errors.

## CLI Utility

The workflow script is located at `_scripts/sync_papers.py`.

### Commands

```bash
# 1. List active members
python3 _scripts/sync_papers.py get-members

# 2. Search for new candidate papers
python3 _scripts/sync_papers.py search --year 2026

# 3. Add approved papers from a JSON file
python3 _scripts/sync_papers.py add-batch --input approved_papers.json

# 4. Verify site compilation
python3 _scripts/sync_papers.py verify-build
```

## Agent Execution Runbook (When Run as Antigravity Agent)

When invoked on a schedule or by user prompt:

1. **Search for Candidate Papers**:
   Run `python3 _scripts/sync_papers.py search --year <YEAR>`.
2. **Present Candidates & Request Approval**:
   - If no new papers are found, inform the user that the literature check is complete and the site is already up to date.
   - If candidate papers are discovered, format them into a clear summary table showing:
     - **Title**
     - **Authors** (highlighting the active CCSB member)
     - **Venue / Journal**
     - **Date / Year**
     - **DOI or arXiv Link**
   - **Ask for approval**: Prompt the user (or use `ask_question`) to ask which papers should be added to the website.
   - **WAIT for explicit user confirmation before creating any files.**
3. **Generate Posts & Thumbnails (Only Upon User Approval)**:
   - For each approved paper:
     - Check if open-access PDF figures can be extracted, or synthesize a clean 1200×805 architecture diagram using `generate_image`.
     - Write the Jekyll post in `papers/_posts/` following the site schema.
     - Save the standardized thumbnail in `images/papers/` at `1200×805` (3:2 landscape).
4. **Verify Site Build**:
   Run `bundle exec jekyll build` to ensure no build errors or broken references.
5. **Summarize Additions**:
   Provide a concise confirmation with clickable links to the newly created post and image files.
