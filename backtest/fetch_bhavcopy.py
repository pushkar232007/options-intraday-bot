"""
Downloads NSE F&O Bhavcopy files (daily option settlement data) for a date range.
Files are stored as raw ZIPs in data/bhavcopy/raw/ and parsed CSVs are not kept on
disk — bhavcopy_db.py reads directly from the ZIPs and builds a SQLite index.

NSE URL: https://nsearchives.nseindia.com/content/historical/DERIVATIVES/
         {YEAR}/{MON}/fo{DD}{MON}{YYYY}bhav.csv.zip
Returns 404 on weekends and market holidays — those are silently skipped.

Usage:
  python3 fetch_bhavcopy.py                        # last 2 years to today
  python3 fetch_bhavcopy.py --start 2023-01-01     # custom start
  python3 fetch_bhavcopy.py --start 2024-01-01 --end 2024-12-31
"""
import io
import os
import time
import urllib.error
import urllib.request
import zipfile
from datetime import date, datetime, timedelta

RAW_DIR = os.path.join(os.path.dirname(__file__), "data", "bhavcopy", "raw")
MONTHS = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
          "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

_HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/120.0.0.0 Safari/537.36"),
    "Accept": "*/*",
    "Referer": "https://www.nseindia.com/",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
}


def bhavcopy_url(d: date) -> str:
    mon = MONTHS[d.month - 1]
    return (f"https://nsearchives.nseindia.com/content/historical/DERIVATIVES/"
            f"{d.year}/{mon}/fo{d.day:02d}{mon}{d.year}bhav.csv.zip")


def zip_path(d: date) -> str:
    mon = MONTHS[d.month - 1]
    return os.path.join(RAW_DIR, str(d.year),
                        f"fo{d.day:02d}{mon}{d.year}bhav.csv.zip")


def download_day(d: date, verbose: bool = True) -> bool:
    """Downloads and saves the Bhavcopy ZIP for date d. Returns True if saved/cached."""
    zp = zip_path(d)
    if os.path.exists(zp):
        return True

    os.makedirs(os.path.dirname(zp), exist_ok=True)
    url = bhavcopy_url(d)
    req = urllib.request.Request(url, headers=_HEADERS)

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read()
        # Validate it's actually a ZIP before saving
        zipfile.ZipFile(io.BytesIO(raw))  # raises BadZipFile if not a real ZIP
        with open(zp, "wb") as f:
            f.write(raw)
        if verbose:
            print(f"  {d} ✓")
        return True
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False  # weekend or market holiday — normal
        if verbose:
            print(f"  {d} HTTP {e.code}: {e.reason}")
        return False
    except zipfile.BadZipFile:
        if verbose:
            print(f"  {d} bad ZIP (NSE may have blocked the request)")
        return False
    except Exception as e:
        if verbose:
            print(f"  {d} error: {e}")
        return False


def read_zip(d: date):
    """Reads a cached ZIP and returns the CSV content as a string, or None."""
    zp = zip_path(d)
    if not os.path.exists(zp):
        return None
    try:
        with zipfile.ZipFile(zp) as zf:
            names = zf.namelist()
            csv_name = next((n for n in names if n.lower().endswith(".csv")), names[0])
            return zf.read(csv_name).decode("utf-8", errors="replace")
    except Exception:
        return None


def cached_dates() -> list:
    """Returns sorted list of dates for which ZIPs are already downloaded."""
    dates = []
    if not os.path.exists(RAW_DIR):
        return dates
    for year_dir in os.listdir(RAW_DIR):
        year_path = os.path.join(RAW_DIR, year_dir)
        if not os.path.isdir(year_path):
            continue
        for fname in os.listdir(year_path):
            if not fname.endswith(".zip"):
                continue
            try:
                # filename: fo01JAN2024bhav.csv.zip
                day = int(fname[2:4])
                mon_str = fname[4:7]
                year = int(fname[7:11])
                mon = MONTHS.index(mon_str) + 1
                dates.append(date(year, mon, day))
            except (ValueError, IndexError):
                continue
    return sorted(dates)


def fetch_range(start: date, end: date, delay: float = 0.4, verbose: bool = True):
    """Downloads all weekday Bhavcopy files between start and end (inclusive)."""
    current = start
    downloaded, skipped, cached = 0, 0, 0
    while current <= end:
        if current.weekday() < 5:  # Mon–Fri only
            zp = zip_path(current)
            if os.path.exists(zp):
                cached += 1
            else:
                ok = download_day(current, verbose=verbose)
                if ok:
                    downloaded += 1
                else:
                    skipped += 1
                time.sleep(delay)
        current += timedelta(days=1)
    if verbose:
        print(f"\nDone — {downloaded} downloaded, {cached} already cached, "
              f"{skipped} skipped (holidays/errors)")


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Download NSE F&O Bhavcopy files")
    ap.add_argument("--start", default=str((date.today() - timedelta(days=730))))
    ap.add_argument("--end", default=str(date.today()))
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    start = datetime.strptime(args.start, "%Y-%m-%d").date()
    end = datetime.strptime(args.end, "%Y-%m-%d").date()
    print(f"Downloading NSE F&O Bhavcopy: {start} → {end}")
    fetch_range(start, end, verbose=not args.quiet)
