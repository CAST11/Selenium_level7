# utils/csv_utils.py
import csv
import io
import os

def _try_open_bytes(path):
    """Return raw bytes of file or raise."""
    with open(path, "rb") as f:
        return f.read()

def load_csv_data(file_path):
    """
    Robust CSV loader:
    - tries common encodings (utf-8-sig, utf-8, cp1252)
    - tries to detect delimiter with csv.Sniffer
    - if a row has a single field that itself contains commas,
      it will split into 3 parts (username,password,expected)
    - returns list of dicts: [{'username':..., 'password':..., 'expected':...}, ...]
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"CSV not found: {file_path}")

    raw = _try_open_bytes(file_path)

    # Try encodings in order
    encodings = ["utf-8-sig", "utf-8", "cp1252", "latin1"]
    text = None
    used_encoding = None
    for enc in encodings:
        try:
            text = raw.decode(enc)
            used_encoding = enc
            break
        except Exception:
            continue
    if text is None:
        # fallback: replace unknown chars
        text = raw.decode("utf-8", errors="replace")
        used_encoding = "utf-8(replace)"

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Use a small sample to detect dialect
    sample = "\n".join(text.splitlines()[:10]) or text

    # Default delimiter
    delimiter = ","
    try:
        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(sample)
        delimiter = dialect.delimiter
    except Exception:
        # fallback to common delimiters if sniffing fails
        for d in [",", ";", "\t"]:
            if d in sample:
                delimiter = d
                break

    # Parse using csv.reader to be robust with quotes
    reader = csv.reader(io.StringIO(text), delimiter=delimiter)
    rows = list(reader)

    cleaned = []
    for i, row in enumerate(rows):
        # Skip empty lines
        if not row or all((cell is None or str(cell).strip() == "") for cell in row):
            continue

        # Header detection (first non-empty row)
        if i == 0:
            header = [c.strip().lower().strip('"').strip("'") for c in row]
            # Normalize header names to expected keys if possible
            # If header contains utf-8 BOM marker, strip it
            header = [h.lstrip("\ufeff") for h in header]
            # Check if header already correct
            if any("username" in h for h in header) and any("password" in h for h in header):
                # we'll map by header later
                continue
            else:
                # If header looks like data (no username/password), treat it as data line
                # fallthrough to process it as data below
                pass

        # If row has exactly 3 columns -> good
        if len(row) == 3:
            u, p, e = row
        else:
            # If row is one column but contains commas, try splitting by comma
            if len(row) == 1 and "," in row[0]:
                parts = [p.strip() for p in row[0].split(",")]
                if len(parts) >= 3:
                    u, p, e = parts[0], parts[1], ",".join(parts[2:])
                else:
                    # can't fix this row reliably -> skip
                    continue
            else:
                # If row has more than 3 columns and delimiter was wrong, try joining extras into expected
                if len(row) > 3:
                    u = row[0].strip()
                    p = row[1].strip()
                    e = ",".join([c.strip() for c in row[2:]])
                else:
                    # unknown format -> skip
                    continue

        cleaned.append({
            "username": (u or "").strip().lstrip('\ufeff').strip('"').strip("'"),
            "password": (p or "").strip().strip('"').strip("'"),
            "expected": (e or "").strip().strip('"').strip("'")
        })

    return cleaned
