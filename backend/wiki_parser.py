"""
Parse Slovak election polling rows from Wikipedia wikitext.

Column mapping (0-indexed, after firm / date / sample-size cells are removed):
  0  Smer        → smer
  1  PS          → ps
  2  Hlas        → hlas
  3  OĽaNO       → olano
  4  ZĽ          → (ignored)
  5  KÚ          → (ignored)
  6  KDH         → kdh
  7  SaS         → sas
  8  SNS         → sns
  9  Republika   → rep
 10  MA (Hung.)  → ma
 11  Democrats   → dem
 12  We Are Fam. → sme_rodina
 13  ĽSNS        → (ignored)
"""

import re
from calendar import monthrange
from datetime import date
from typing import Optional

MONTH_MAP: dict[str, int] = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
}

FIRMS: set[str] = {"AKO", "Focus", "Ipsos", "NMS"}

COL_MAP: dict[int, Optional[str]] = {
    0: "smer",  1: "ps",   2: "hlas",      3: "olano",
    4: None,    5: None,
    6: "kdh",   7: "sas",  8: "sns",        9: "rep",
    10: "ma",   11: "dem", 12: "sme_rodina", 13: None,
}

# Regex for a 4-digit year in the range 2020-2029
_YEAR_RE = re.compile(r"\b(202[0-9])\b")
# Regex for day numbers (1-31)
_DAY_RE = re.compile(r"\b([0-9]{1,2})\b")


def clean_cell(text: str) -> str:
    """Strip all wiki markup from a raw cell string."""
    # <ref .../> and <ref>...</ref>
    text = re.sub(r"<ref\b[^>]*/\s*>", "", text)
    text = re.sub(r"<ref\b[^>]*>.*?</ref>", "", text, flags=re.DOTALL)
    # HTML comments
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    # Remaining HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # {{increase|X}}, {{decrease|X}}, {{steady|X}}, {{nowrap|X}} → X
    text = re.sub(
        r"\{\{(?:increase|decrease|steady|nowrap)\s*\|([^|{}]*)[^}]*\}\}",
        lambda m: m.group(1).strip(),
        text,
        flags=re.IGNORECASE,
    )
    # Remove remaining {{...}} templates — up to 4 passes for nesting
    for _ in range(4):
        text = re.sub(r"\{\{[^{}]*\}\}", "", text)
    # [[link|display]] → display, [[link]] → link
    text = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", r"\1", text)
    # Footnote markers: [1], [note 1], etc.
    text = re.sub(r"\[[^\]]{0,30}\]", "", text)
    # Bold / italic markup
    text = re.sub(r"'{2,}", "", text)
    return text.strip()


def _strip_cell_attrs(part: str) -> str:
    """Remove 'style=... |' or similar attribute prefix from a cell part."""
    return re.sub(
        r"^[^|]*?(?:style|align|class|bgcolor|colspan|rowspan)\s*=[^|]*\|",
        "",
        part.strip(),
    )


def extract_cells(row: str) -> list[str]:
    """
    Extract cleaned cell values from one wikitext table row chunk
    (the text that follows a '|-' separator).
    """
    cells: list[str] = []
    for line in row.split("\n"):
        line = line.strip()
        if not line or line.startswith("!"):
            # Skip empty lines and header lines
            continue
        if line.startswith("|"):
            content = line[1:]  # drop the leading |
            for part in content.split("||"):
                part = _strip_cell_attrs(part)
                cleaned = clean_cell(part)
                # Keep even empty/null-marker cells so column indices stay aligned
                cells.append(cleaned)
    return cells


def _parse_float(s: str) -> Optional[float]:
    s = s.strip().replace(",", "")  # commas are thousands-separators
    if not s or s in ("-", "\u2013", "\u2014", "N/A", "n/a"):
        return None
    try:
        v = float(s)
        return v if 0 < v <= 100 else None
    except ValueError:
        return None


def _is_null_marker(s: str) -> bool:
    return s.strip() in ("-", "\u2013", "\u2014", "")


def _is_sample_size(s: str) -> bool:
    """True if s looks like a polling sample size (integer ≥ 500)."""
    clean = re.sub(r"[\s,\xa0]", "", s.strip())
    try:
        return int(clean) >= 500
    except ValueError:
        return False


def _parse_date(date_str: str) -> Optional[date]:
    """Best-effort parse of a range string like '10–16 Sep 2024'."""
    year_m = _YEAR_RE.search(date_str)
    if not year_m:
        return None
    year = int(year_m.group(1))

    months_found: list[int] = []
    for name, num in MONTH_MAP.items():
        if re.search(r"\b" + name, date_str, re.IGNORECASE):
            months_found.append(num)
    if not months_found:
        return None

    days = [int(d) for d in _DAY_RE.findall(date_str) if 1 <= int(d) <= 31]

    if len(months_found) == 1:
        month = months_found[0]
        if len(days) >= 2:
            day = (days[0] + days[-1]) // 2
        elif days:
            day = days[0]
        else:
            day = 15
    else:
        # Cross-month range (e.g. "27 Oct–1 Nov 2024")
        m1, m2 = months_found[0], months_found[1]
        d1 = days[0] if days else 1
        d2 = days[1] if len(days) > 1 else 1
        span = (monthrange(year, m1)[1] - d1) + d2
        mid = span // 2
        day_abs = d1 + mid
        max_day_m1 = monthrange(year, m1)[1]
        if day_abs > max_day_m1:
            month = m2
            day = day_abs - max_day_m1
        else:
            month = m1
            day = day_abs

    try:
        return date(year, month, max(1, min(day, monthrange(year, month)[1])))
    except ValueError:
        return None


def parse_polls_from_wikitext(wikitext: str) -> list[dict]:
    """
    Return a list of raw poll dicts parsed from wikitext.
    Each dict has keys: firm, date_str, date, source, and all party columns.
    """
    results: list[dict] = []

    for raw_row in re.split(r"\n\s*\|-", wikitext):
        cells = extract_cells(raw_row)
        if len(cells) < 6:
            continue

        # --- identify firm ---
        firm: Optional[str] = None
        firm_idx: int = -1
        for i, cell in enumerate(cells):
            for f in FIRMS:
                if f.lower() in cell.lower():
                    firm = f
                    firm_idx = i
                    break
            if firm:
                break
        if not firm:
            continue

        # --- identify date string (contains a 4-digit year) ---
        date_str_raw: Optional[str] = None
        date_idx: int = -1
        for i, cell in enumerate(cells):
            if i == firm_idx:
                continue
            if _YEAR_RE.search(cell):
                date_str_raw = cell
                date_idx = i
                break
        if not date_str_raw:
            continue

        parsed_date = _parse_date(date_str_raw)
        if not parsed_date:
            continue

        # --- collect numeric values, skipping firm / date / sample-size ---
        sample_skipped = False
        values: list[Optional[float]] = []

        for i, cell in enumerate(cells):
            if i in (firm_idx, date_idx):
                continue
            if not sample_skipped and _is_sample_size(cell):
                sample_skipped = True
                continue
            # Accept the cell if it's numeric or an explicit null marker
            if _is_null_marker(cell) or _parse_float(cell) is not None:
                values.append(_parse_float(cell))

        if len(values) < 8:
            continue

        # --- map columns ---
        poll: dict = {
            "firm": firm,
            "date_str": date_str_raw,
            "date": parsed_date,
            "source": "wikipedia",
        }
        for col_idx, field in COL_MAP.items():
            val = values[col_idx] if col_idx < len(values) else None
            if field is not None:
                poll[field] = val

        results.append(poll)

    return results
