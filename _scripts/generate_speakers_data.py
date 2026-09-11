#!/usr/bin/env python3
"""
generate_speakers_data.py
Extracts and consolidates seminar speakers across CCSB seminar history (2019-2026):
  - talks/index.md (current/upcoming Fall 2026 schedule)
  - blog/_posts/*Seminar*.md (all published seminar posts with abstracts, photos, links)
  - talks/old/talks-*.html (historical semester schedules with detailed affiliations)

Generates:
  - _data/seminar_speakers.json (complete data feed for the interactive map and directory)
  - _data/institutions.yml (coordinate registry for all universities and institutes)
"""

import os
import re
import json
import glob
from html.parser import HTMLParser
from datetime import datetime

# Geocoded institution directory
INSTITUTIONS = {
    "Prairie View A&M University": {
        "city": "Prairie View",
        "state": "TX",
        "country": "USA",
        "lat": 30.0931,
        "lng": -95.9890
    },
    "Texas A&M University": {
        "city": "College Station",
        "state": "TX",
        "country": "USA",
        "lat": 30.6187,
        "lng": -96.3365
    },
    "Texas A&M University Rangel College of Pharmacy": {
        "city": "Kingsville",
        "state": "TX",
        "country": "USA",
        "lat": 27.5259,
        "lng": -97.8814
    },
    "The University of Texas MD Anderson Cancer Center": {
        "city": "Houston",
        "state": "TX",
        "country": "USA",
        "lat": 29.7071,
        "lng": -95.3970
    },
    "Johns Hopkins University": {
        "city": "Baltimore",
        "state": "MD",
        "country": "USA",
        "lat": 39.3299,
        "lng": -76.6205
    },
    "TGen (Translational Genomics Research Institute)": {
        "city": "Phoenix",
        "state": "AZ",
        "country": "USA",
        "lat": 33.4533,
        "lng": -112.0664
    },
    "Stanford University": {
        "city": "Stanford",
        "state": "CA",
        "country": "USA",
        "lat": 37.4275,
        "lng": -122.1697
    },
    "Purdue University": {
        "city": "West Lafayette",
        "state": "IN",
        "country": "USA",
        "lat": 40.4237,
        "lng": -86.9212
    },
    "Princeton University": {
        "city": "Princeton",
        "state": "NJ",
        "country": "USA",
        "lat": 40.3440,
        "lng": -74.6514
    },
    "University of Houston": {
        "city": "Houston",
        "state": "TX",
        "country": "USA",
        "lat": 29.7199,
        "lng": -95.3422
    },
    "University of Alabama": {
        "city": "Tuscaloosa",
        "state": "AL",
        "country": "USA",
        "lat": 33.2140,
        "lng": -87.5391
    },
    "Arizona State University": {
        "city": "Tempe",
        "state": "AZ",
        "country": "USA",
        "lat": 33.4242,
        "lng": -111.9281
    },
    "University of Pittsburgh": {
        "city": "Pittsburgh",
        "state": "PA",
        "country": "USA",
        "lat": 40.4444,
        "lng": -79.9608
    },
    "Binghamton University, State University of New York": {
        "city": "Binghamton",
        "state": "NY",
        "country": "USA",
        "lat": 42.0886,
        "lng": -75.9699
    },
    "University of Texas at San Antonio": {
        "city": "San Antonio",
        "state": "TX",
        "country": "USA",
        "lat": 29.5828,
        "lng": -98.6198
    },
    "University of Texas at Arlington": {
        "city": "Arlington",
        "state": "TX",
        "country": "USA",
        "lat": 32.7292,
        "lng": -97.1131
    },
    "University of Central Florida": {
        "city": "Orlando",
        "state": "FL",
        "country": "USA",
        "lat": 28.6024,
        "lng": -81.2001
    },
    "Columbus State University": {
        "city": "Columbus",
        "state": "GA",
        "country": "USA",
        "lat": 32.4998,
        "lng": -84.9427
    },
    "US Environmental Protection Agency Region 6": {
        "city": "Dallas",
        "state": "TX",
        "country": "USA",
        "lat": 32.7844,
        "lng": -96.7997
    },
    "Oklahoma State University": {
        "city": "Stillwater",
        "state": "OK",
        "country": "USA",
        "lat": 36.1265,
        "lng": -97.0734
    },
    "Brigham and Women's Hospital / Harvard Medical School": {
        "city": "Boston",
        "state": "MA",
        "country": "USA",
        "lat": 42.3361,
        "lng": -71.1065
    },
    "Cold Spring Harbor Laboratory": {
        "city": "Cold Spring Harbor",
        "state": "NY",
        "country": "USA",
        "lat": 40.8598,
        "lng": -73.4682
    },
    "General Sir John Kotelawala Defence University": {
        "city": "Ratmalana",
        "state": "Western Province",
        "country": "Sri Lanka",
        "lat": 6.8198,
        "lng": 79.8879
    },
    "University of Texas at Dallas": {
        "city": "Richardson",
        "state": "TX",
        "country": "USA",
        "lat": 32.9857,
        "lng": -96.7501
    },
    "Texas Tech University": {
        "city": "Lubbock",
        "state": "TX",
        "country": "USA",
        "lat": 33.5843,
        "lng": -101.8783
    },
    "USDA-ARS Dale Bumpers National Rice Research Center": {
        "city": "Stuttgart",
        "state": "AR",
        "country": "USA",
        "lat": 34.4695,
        "lng": -91.4154
    },
    "Microsoft": {
        "city": "Redmond",
        "state": "WA",
        "country": "USA",
        "lat": 47.6423,
        "lng": -122.1369
    },
    "Brigham Young University": {
        "city": "Provo",
        "state": "UT",
        "country": "USA",
        "lat": 40.2518,
        "lng": -111.6493
    },
    "Baylor College of Medicine": {
        "city": "Houston",
        "state": "TX",
        "country": "USA",
        "lat": 29.7107,
        "lng": -95.3948
    },
    "Sandia National Laboratories": {
        "city": "Livermore",
        "state": "CA",
        "country": "USA",
        "lat": 37.6749,
        "lng": -121.7068
    },
    "UPMC / University of Pittsburgh School of Medicine": {
        "city": "Pittsburgh",
        "state": "PA",
        "country": "USA",
        "lat": 40.4430,
        "lng": -79.9602
    },
    "USC Institute of Translational Genomics": {
        "city": "Los Angeles",
        "state": "CA",
        "country": "USA",
        "lat": 34.0625,
        "lng": -118.2045
    }
}

def detect_institution(text):
    """
    Identifies the speaker's then-current home institution from their affiliation text.
    Strictly uses current affiliation at the time of the seminar, NOT education or past positions.
    """
    t = text.lower()
    
    # If explicitly PVAMU in speaker affiliation
    if "prairie view" in t or "pvamu" in t:
        return "Prairie View A&M University"

    # External institutions
    if "stanford" in t:
        return "Stanford University"
    if "princeton" in t:
        return "Princeton University"
    if "purdue" in t:
        return "Purdue University"
    if "brigham young" in t or re.search(r"\bbyu\b", t):
        return "Brigham Young University"
    if "brigham" in t or "harvard" in t:
        return "Brigham and Women's Hospital / Harvard Medical School"
    if "johns hopkins" in t:
        return "Johns Hopkins University"
    if "tgen" in t or "translational genomics" in t:
        return "TGen (Translational Genomics Research Institute)"
    if "pittsburgh" in t or "upmc" in t:
        return "University of Pittsburgh"
    if "university of alabama" in t or ("alabama" in t and not "birmingham" in t):
        return "University of Alabama"
    if "central flori" in t or re.search(r"\bucf\b", t):
        return "University of Central Florida"
    if "columbus state" in t:
        return "Columbus State University"
    if "arizona state" in t or re.search(r"\basu\b", t):
        return "Arizona State University"
    if "university of houston" in t or re.search(r"\buh\b", t):
        return "University of Houston"
    if "bingham" in t or "suny" in t:
        return "Binghamton University, State University of New York"
    if "san antonio" in t or re.search(r"\butsa\b", t):
        return "University of Texas at San Antonio"
    if "arlington" in t or re.search(r"\buta\b", t):
        return "University of Texas at Arlington"
    if "environmental protection agency" in t or re.search(r"\bepa\b", t):
        return "US Environmental Protection Agency Region 6"
    if "oklahoma state" in t:
        return "Oklahoma State University"
    if "cold spring harbor" in t:
        return "Cold Spring Harbor Laboratory"
    if "kotelawala" in t or "sri lanka" in t:
        return "General Sir John Kotelawala Defence University"
    if "ut dallas" in t or "texas at dallas" in t or re.search(r"\butd\b", t):
        return "University of Texas at Dallas"
    if "texas tech" in t or re.search(r"\bttu\b", t):
        return "Texas Tech University"
    if "rice research" in t or "usda-ars" in t or "usda" in t:
        return "USDA-ARS Dale Bumpers National Rice Research Center"
    if "microsoft" in t:
        return "Microsoft"
    if "baylor" in t:
        return "Baylor College of Medicine"
    if "sandia" in t:
        return "Sandia National Laboratories"
    if "md anderson" in t or "m.d. anderson" in t:
        return "The University of Texas MD Anderson Cancer Center"
    if "rangel" in t or ("pharmacy" in t and "texas a&m" in t):
        return "Texas A&M University Rangel College of Pharmacy"
    if "texas a&m" in t or re.search(r"\btamu\b", t) or "tigss" in t:
        return "Texas A&M University"

    # Default fallback
    return "Prairie View A&M University"

class TableRowParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cells = []
        self.current_cell = []
        self.links = []
        self.in_cell = False

    def handle_starttag(self, tag, attrs):
        if tag in ("td", "th"):
            self.in_cell = True
            self.current_cell = []
        if tag == "a":
            for k, v in attrs:
                if k == "href":
                    self.links.append(v)

    def handle_endtag(self, tag):
        if tag in ("td", "th") and self.in_cell:
            self.in_cell = False
            self.cells.append(" ".join("".join(self.current_cell).split()))

    def handle_data(self, data):
        if self.in_cell:
            self.current_cell.append(data)

def parse_date_str(date_str, fallback_year):
    """Extracts YYYY-MM-DD from various date formats."""
    m_iso = re.search(r"(\d{4})-(\d{2})-(\d{2})", date_str)
    if m_iso:
        return f"{m_iso.group(1)}-{m_iso.group(2)}-{m_iso.group(3)}"
    
    cleaned = re.sub(r"^(?:Mon|Tue|Wed|Thu|Thur|Fri|Sat|Sun)\.?,?\s*", "", date_str.strip())
    cleaned = re.split(r"\[|Rescheduled", cleaned)[0].strip()
    
    months = {
        "jan": "01", "feb": "02", "mar": "03", "apr": "04",
        "may": "05", "jun": "06", "jul": "07", "aug": "08",
        "sep": "09", "sept": "09", "oct": "10", "nov": "11", "dec": "12"
    }
    
    m = re.search(r"([A-Za-z]+)\.?\s*(\d{1,2})(?:st|nd|rd|th)?,?\s*(\d{4})?", cleaned)
    if m:
        mon_str = m.group(1).lower()
        month = None
        for k, v in months.items():
            if mon_str.startswith(k):
                month = v
                break
        if month:
            day = int(m.group(2))
            year = m.group(3) if m.group(3) else fallback_year
            return f"{year}-{month}-{day:02d}"
    return f"{fallback_year}-01-01"

def extract_speaker_name(speaker_raw):
    """Cleans speaker name string."""
    s = speaker_raw.replace("&amp;", "&").replace("&nbsp;", " ")
    parts = [p.strip() for p in s.split(",") if p.strip()]
    if not parts:
        return s
    name = parts[0]
    if len(parts) > 1 and any(d in parts[1] for d in ["Ph.D.", "MD", "M.D.", "DVM", "Ph.D"]):
        name += ", " + parts[1]
    return name

def get_semester(year, month):
    return f"{'Spring' if month <= 6 else 'Fall'} {year}"

def main():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    posts_dir = os.path.join(root, "blog", "_posts")
    old_talks_dir = os.path.join(root, "talks", "old")
    current_talks_file = os.path.join(root, "talks", "index.md")
    data_dir = os.path.join(root, "_data")
    
    today_str = datetime.today().strftime("%Y-%m-%d")

    # 1. Parse historical table rows from talks/old/
    table_records = {}
    for f in sorted(glob.glob(os.path.join(old_talks_dir, "talks-*.html"))):
        f_base = os.path.basename(f)
        m_sem = re.search(r"talks-(\d{4})-([a-z]+)", f_base)
        year_str = m_sem.group(1) if m_sem else "2024"
        semester_str = f"{m_sem.group(2).capitalize()} {year_str}" if m_sem else year_str
        
        content = open(f).read()
        trs = re.findall(r"<tr>(.*?)</tr>", content, re.DOTALL)
        for tr in trs:
            p = TableRowParser()
            p.feed(tr)
            if len(p.cells) >= 2 and "Date" not in p.cells[0]:
                date_str = p.cells[0]
                if "CANCELLED" in date_str or "[CANCELLED]" in p.cells[1]:
                    continue
                clean_date = parse_date_str(date_str, year_str)
                speaker_raw = p.cells[1]
                title_raw = p.cells[2] if len(p.cells) > 2 else ""
                
                table_records[clean_date] = {
                    "raw_speaker": speaker_raw,
                    "title": re.sub(r"<[^>]+>", "", title_raw).strip(),
                    "links": p.links,
                    "semester": semester_str,
                    "file": f_base
                }

    speakers_list = []
    processed_dates = set()

    # 2. Add upcoming/current semester from talks/index.md (Fall 2026)
    if os.path.exists(current_talks_file):
        idx_content = open(current_talks_file).read()
        table_rows = re.findall(r"\|\s*\*\*([^\*]+)\*\*\s*\|\s*([^\|]+)\s*\|\s*([^\|]+)\s*\|", idx_content)
        for r in table_rows:
            date_str = r[0].strip()
            speaker_info = r[1].strip()
            title_info = r[2].strip()
            
            clean_date = parse_date_str(date_str, "2026")
            speaker_name = extract_speaker_name(speaker_info)
            speaker_name = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", speaker_name).strip()
            
            inst_name = detect_institution(speaker_info)
            inst_meta = INSTITUTIONS.get(inst_name, INSTITUTIONS["Prairie View A&M University"])
            
            matched_title = re.sub(r"<[^>]+>", "", title_info).strip()
            if not matched_title or matched_title == "TBD":
                matched_title = f"Upcoming CCSB Seminar ({speaker_name})"

            processed_dates.add(clean_date)
            y = int(clean_date.split("-")[0])
            m = int(clean_date.split("-")[1])
            
            speakers_list.append({
                "id": f"talk-{clean_date}",
                "speaker": speaker_name,
                "institution": inst_name,
                "affiliation_detail": re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", speaker_info).strip(),
                "city": inst_meta["city"],
                "state": inst_meta["state"],
                "country": inst_meta["country"],
                "lat": inst_meta["lat"],
                "lng": inst_meta["lng"],
                "date": clean_date,
                "year": y,
                "semester": "Fall 2026",
                "title": matched_title,
                "url": "/talks/",
                "photo": "",
                "status": "upcoming"
            })

    # Date aliases between schedule tables and post filenames
    date_aliases = {
        '2022-01-23': '2022-01-26',
        '2024-04-24': '2024-04-17',
        '2025-11-12': '2025-11-22'
    }
    for p_date, t_date in date_aliases.items():
        if t_date in table_records and p_date not in table_records:
            table_records[p_date] = table_records[t_date]

    # 3. Process all blog seminar posts (Primary source for past seminars)
    for p in sorted(glob.glob(os.path.join(posts_dir, "*Seminar*.md")), reverse=True):
        content = open(p).read()
        base = os.path.basename(p)
        slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", base[:-3])
        url = f"/blog/talks/{slug}/"
        
        fn_m = re.search(r"^(\d{4}-\d{2}-\d{2})", base)
        fn_date = fn_m.group(1) if fn_m else ""
        dt_m = re.search(r"^date:\s*(\d{4}-\d{2}-\d{2})", content, re.M)
        fm_date = dt_m.group(1) if dt_m else ""
        spk_m = re.search(r"^speaker:\s*(.+)$", content, re.M)
        title_m = re.search(r"^title:\s*[\"']?(?:\[CCSB Seminar Series\]\s*)?([^\"'\n]+)[\"']?", content, re.M)
        photo_m = re.search(r"^photo:\s*(.+)$", content, re.M)
        inst_m = re.search(r"^institution:\s*[\"']?([^\"'\n]+)[\"']?", content, re.M)

        # Date resolution: prefer filename date if in table_records, else fm_date, else fn_date
        tbl_info = None
        date = ""
        if fn_date in table_records:
            tbl_info = table_records[fn_date]
            date = fn_date
        elif fm_date in table_records:
            tbl_info = table_records[fm_date]
            date = fm_date
        else:
            date = fn_date or fm_date or "2020-01-01"

        raw_spk = tbl_info["raw_speaker"] if tbl_info else ""

        speaker = spk_m.group(1).strip() if spk_m else ""
        title = title_m.group(1).strip() if title_m else ""
        photo = photo_m.group(1).strip() if photo_m else ""

        # Fallback speaker if empty
        if not speaker:
            if raw_spk:
                speaker = extract_speaker_name(re.split(r"\(host|\(hosted", raw_spk, flags=re.I)[0])
            elif "Choi" in base:
                speaker = "Woonyoung Choi, Ph.D."
            elif "SLewis" in base:
                speaker = "Sharon Lewis, Ph.D."
            elif "BGersey" in base:
                speaker = "Brad 'Buddy' Gersey, Ph.D."
            elif "AJoy" in base:
                speaker = "Anna Joy, Ph.D."
            elif "TKebrom" in base:
                speaker = "Tesfamichael Kebrom, Ph.D."
            elif "BDebeb" in base:
                speaker = "Bisrat G Debeb, DVM, Ph.D."
            elif "DIacobas" in base:
                speaker = "Dumitru A. Iacobas, Ph.D."
            else:
                m_name = re.search(r"CCSB-Seminar-([A-Za-z]+)-", base)
                speaker = m_name.group(1) if m_name else "Invited Speaker"

        y = int(date.split("-")[0])
        m = int(date.split("-")[1])
        semester = get_semester(y, m)

        # Affiliation & institution resolution - STRICTLY THEN-CURRENT AFFILIATION ONLY
        inst_name = None
        affiliation_detail = ""

        if inst_m:
            inst_name = inst_m.group(1).strip()

        if raw_spk:
            # Exclude host portion from institution detection and affiliation detail
            speaker_affil_clean = re.split(r"\(host|\(hosted", raw_spk, flags=re.I)[0].strip()
            speaker_affil_clean = re.sub(r"<[^>]+>", "", speaker_affil_clean).strip().rstrip(",")
            affiliation_detail = speaker_affil_clean
            if not inst_name:
                inst_name = detect_institution(speaker_affil_clean)

        if not inst_name:
            # Fallback for posts without table records (e.g. Spring 2019):
            # Check only first line of ## Speaker section if it describes current appointment
            spk_section = re.search(r"## Speaker\s*\n+(.+?)(?=\n##|\Z)", content, re.S)
            first_sentence = ""
            if spk_section:
                first_sentence = spk_section.group(1).strip().split("\n")[0]
                # If it talks about education or prior history, ignore it
                if any(w in first_sentence.lower() for w in ["received his", "received her", "received a", "earned", "alumnus"]):
                    first_sentence = ""
            if first_sentence:
                inst_name = detect_institution(first_sentence)
            else:
                inst_name = "Prairie View A&M University"

        if not affiliation_detail:
            affiliation_detail = f"{speaker}, {inst_name}"

        inst_meta = INSTITUTIONS.get(inst_name, INSTITUTIONS["Prairie View A&M University"])

        # Status: upcoming if date is today or future, and marked upcoming
        is_upcoming = date >= today_str and y == 2026

        processed_dates.add(date)
        speakers_list.append({
            "id": f"talk-{date}",
            "speaker": speaker,
            "institution": inst_name,
            "affiliation_detail": affiliation_detail,
            "city": inst_meta["city"],
            "state": inst_meta["state"],
            "country": inst_meta["country"],
            "lat": inst_meta["lat"],
            "lng": inst_meta["lng"],
            "date": date,
            "year": y,
            "semester": semester,
            "title": title,
            "url": url,
            "photo": photo,
            "status": "upcoming" if is_upcoming else "past"
        })

    # Sort descending by date
    speakers_list.sort(key=lambda x: x["date"], reverse=True)

    # Save _data/seminar_speakers.json
    speakers_json_path = os.path.join(data_dir, "seminar_speakers.json")
    with open(speakers_json_path, "w") as fp:
        json.dump(speakers_list, fp, indent=2)

    # Save _data/institutions.yml
    inst_yaml_path = os.path.join(data_dir, "institutions.yml")
    with open(inst_yaml_path, "w") as fp:
        for name, meta in sorted(INSTITUTIONS.items()):
            fp.write(f'"{name}":\n')
            fp.write(f'  city: "{meta["city"]}"\n')
            fp.write(f'  state: "{meta["state"]}"\n')
            fp.write(f'  country: "{meta["country"]}"\n')
            fp.write(f'  lat: {meta["lat"]}\n')
            fp.write(f'  lng: {meta["lng"]}\n\n')

    print(f"Generated {speakers_json_path} with {len(speakers_list)} talks.")
    upcoming_count = sum(1 for s in speakers_list if s["status"] == "upcoming")
    past_count = sum(1 for s in speakers_list if s["status"] == "past")
    print(f"Stats: {upcoming_count} Upcoming, {past_count} Past.")

if __name__ == "__main__":
    main()
