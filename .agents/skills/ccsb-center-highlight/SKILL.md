---
name: ccsb-center-highlight
description: >-
  Generates and updates the weekly center research highlight for the CCSB website,
  synthesizing recent blog announcements, grants, and publications into an engaging,
  linkified summary paragraph with explicit user approval before saving.
---

# CCSB Center Highlight Skill

## Overview

This skill synthesizes recent center milestones, newly funded research grants, seminars, and publications from `blog/_posts/` and `papers/_posts/` into an engaging, cohesive one-paragraph summary for the homepage. It automatically links personnel mentions to their CCSB profile pages and updates `_data/highlight.yml`.

## Principles & Rules

1. **Holistic Synthesis**:
   - Analyzes recent blog posts (grants, seminar talks, conference presentations) and publications across the Center.
   - Highlights key active researchers, students, and faculty (e.g., Dr. Seungchan Kim, Dr. Md Hossain Shuvo, Dr. Tesfamichael Kebrom, Dr. Xishuang Dong, Thanmayee Yeluri, etc.).
2. **Personnel Linkification**:
   - Every mentioned researcher name must be hyperlinked to their team profile page (`[**Dr. First Last**](/team/first-last/)`).
   - The helper script `_scripts/generate_weekly_highlight.py` automatically resolves team slugs and formats markdown links.
3. **Mandatory User Approval**:
   - **The agent MUST ALWAYS present the proposed highlight summary to the user for review before saving to `_data/highlight.yml`.**
   - Provide the generated text, allow the user to edit or refine, and only write the file after explicit confirmation.
4. **Validation**:
   - Always run `bundle exec jekyll build` after updating `_data/highlight.yml` to verify that the home page renders the highlight without errors.

## CLI Utility

The workflow script is located at `_scripts/generate_weekly_highlight.py`.

### Commands

```bash
# 1. Preview the generated highlight (dry-run, does not modify files)
python3 _scripts/generate_weekly_highlight.py --dry-run

# 2. Save using Gemini API or built-in fallback
python3 _scripts/generate_weekly_highlight.py

# 3. Save with a custom/agent-crafted summary paragraph
python3 _scripts/generate_weekly_highlight.py --summary "Your polished summary paragraph..."
```

## Agent Execution Runbook

When asked to generate or update the center highlight:

1. **Preview Current Content**:
   Run `python3 _scripts/generate_weekly_highlight.py --dry-run` to collect recent blog posts and papers, and inspect the draft.
2. **Review & Polish**:
   - Craft or polish the 1-paragraph summary (approx. 75–120 words), ensuring strong scientific narrative, balanced representation across lab projects, and bolded researcher names.
3. **Present for User Approval**:
   - Show the proposed highlight summary in chat.
   - Ask the user: *"Here is the proposed weekly highlight for the homepage. Would you like me to apply this or make any adjustments?"*
   - **WAIT for explicit approval.**
4. **Apply and Save**:
   - Upon confirmation, apply the summary:
     ```bash
     python3 _scripts/generate_weekly_highlight.py --summary "<APPROVED_TEXT>"
     ```
5. **Verify Build**:
   - Run `bundle exec jekyll build` to ensure the home page compiles cleanly.
6. **Confirm**:
   - Report that [`_data/highlight.yml`](file:///Users/sekim/GitHub/ccsbweb/_data/highlight.yml) has been updated and the site build succeeded.
