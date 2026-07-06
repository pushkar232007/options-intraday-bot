"""
Parses NSE F&O Bhavcopy ZIPs (downloaded by fetch_bhavcopy.py) and stores
the option data in a SQLite database for fast querying by the backtest.

Schema (table: options):
  trade_date   TEXT  'YYYY-MM-DD'
  symbol       TEXT  e.g. 'RELIANCE', 'NIFTY'
  expiry       TEXT  'YYYY-MM-DD'
  option_type  TEXT  'CE' or 'PE'
  strike       REAL
  settle_pr    REAL  end-of-day settlement price (the authoritative daily price)
  open_int     INTEGER  open interest in number of contracts
  contracts    INTEGER  number of contracts traded that day

Primary key: (trade_date, symbol, expiry, option_type, strike)
Indexes: (trade_date, symbol) for fast day+symbol lookups,
         (symbol, expiry) for finding all available expiries.

Usage:
  python3 bhavcopy_db.py                     # build/update db from all downloaded ZIPs
  python3 bhavcopy_db.py --force             # drop and rebuild from scratch
  python3 bhavcopy_db.py --stats             # show what's in the db
"""
import csv
import io
import os
import sqlite3
import sys

sys.path.insert(0, os.path.dirname(__file__))
from fetch_bhavcopy import cached_dates, read_zip

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "bhavcopy", "bhavcopy.db")

MONTHS_SHORT = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
                "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
_MON_NUM = {m: i + 1 for i, m in enumerate(MONTHS_SHORT)}


def _parse_nse_date(s: str) -> str:
    """Converts NSE date formats to 'YYYY-MM-DD'.
    Handles: '25-JAN-2024', '2024-01-25', '25-Jan-2024'."""
    s = s.strip()
    if len(s) == 11 and s[2] == "-" and s[6] == "-":
        d, m, y = s.split("-")
        mon = _MON_NUM.get(m.upper())
        if mon:
            return f"{y}-{mon:02d}-{int(d):02d}"
    return s  # assume already YYYY-MM-DD


def _open_db(path: str) -> sqlite3.Connection:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS options (
            trade_date   TEXT NOT NULL,
            symbol       TEXT NOT NULL,
            expiry       TEXT NOT NULL,
            option_type  TEXT NOT NULL,
            strike       REAL NOT NULL,
            settle_pr    REAL,
            open_int     INTEGER,
            contracts    INTEGER,
            PRIMARY KEY (trade_date, symbol, expiry, option_type, strike)
        )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_date_sym ON options(trade_date, symbol)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_sym_exp  ON options(symbol, expiry)")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS _meta (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)
    conn.commit()
    return conn


def _already_loaded(conn: sqlite3.Connection, date_str: str) -> bool:
    row = conn.execute(
        "SELECT 1 FROM options WHERE trade_date=? LIMIT 1", (date_str,)
    ).fetchone()
    return row is not None


def _load_zip_into_db(conn: sqlite3.Connection, d, instruments=("OPTSTK",)) -> int:
    """Parses one Bhavcopy ZIP and inserts rows into the db. Returns row count inserted."""
    csv_text = read_zip(d)
    if csv_text is None:
        return 0

    date_str = d.strftime("%Y-%m-%d")
    rows = []
    reader = csv.DictReader(io.StringIO(csv_text))
    for row in reader:
        instr = row.get("INSTRUMENT", "").strip()
        if instr not in instruments:
            continue
        opt_type = row.get("OPTION_TYP", "").strip()
        if opt_type not in ("CE", "PE"):
            continue
        try:
            symbol = row["SYMBOL"].strip()
            expiry = _parse_nse_date(row["EXPIRY_DT"])
            strike = float(row["STRIKE_PR"])
            settle_pr = float(row["SETTLE_PR"])
            open_int = int(float(row.get("OPEN_INT") or 0))
            contracts = int(float(row.get("CONTRACTS") or 0))
        except (ValueError, KeyError):
            continue
        rows.append((date_str, symbol, expiry, opt_type, strike,
                     settle_pr, open_int, contracts))

    if rows:
        conn.executemany(
            "INSERT OR REPLACE INTO options "
            "(trade_date,symbol,expiry,option_type,strike,settle_pr,open_int,contracts) "
            "VALUES (?,?,?,?,?,?,?,?)",
            rows,
        )
        conn.commit()
    return len(rows)


def build(force: bool = False, instruments=("OPTSTK",), verbose: bool = True):
    """Builds or updates the SQLite database from all downloaded Bhavcopy ZIPs."""
    if force and os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        if verbose:
            print("Dropped existing database.")

    conn = _open_db(DB_PATH)
    dates = cached_dates()
    if not dates:
        print("No Bhavcopy ZIPs found. Run fetch_bhavcopy.py first.")
        conn.close()
        return

    total_rows = 0
    loaded = 0
    skipped = 0
    for d in dates:
        date_str = d.strftime("%Y-%m-%d")
        if not force and _already_loaded(conn, date_str):
            skipped += 1
            continue
        n = _load_zip_into_db(conn, d, instruments=instruments)
        total_rows += n
        loaded += 1
        if verbose and loaded % 50 == 0:
            print(f"  {loaded}/{len(dates) - skipped} days processed...")

    conn.close()
    if verbose:
        print(f"Done — {loaded} days loaded ({total_rows:,} rows), "
              f"{skipped} already in db.")


# ── Query helpers (used by backtest_stocks.py) ──────────────────────────────

def connect() -> sqlite3.Connection:
    """Opens (read-only) connection to the database."""
    if not os.path.exists(DB_PATH):
        sys.exit(f"Database not found at {DB_PATH}. "
                 "Run: python3 fetch_bhavcopy.py && python3 bhavcopy_db.py")
    conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def trading_dates(conn: sqlite3.Connection) -> list:
    """Returns sorted list of all unique trade_date strings in the db."""
    rows = conn.execute(
        "SELECT DISTINCT trade_date FROM options ORDER BY trade_date"
    ).fetchall()
    return [r[0] for r in rows]


def available_expiries(conn: sqlite3.Connection, symbol: str, trade_date: str) -> list:
    """Returns sorted list of expiry dates available for symbol on trade_date."""
    rows = conn.execute(
        "SELECT DISTINCT expiry FROM options "
        "WHERE trade_date=? AND symbol=? ORDER BY expiry",
        (trade_date, symbol),
    ).fetchall()
    return [r[0] for r in rows]


def available_strikes(conn: sqlite3.Connection, symbol: str, trade_date: str,
                      expiry: str, option_type: str) -> list:
    """Returns sorted list of strikes for (symbol, trade_date, expiry, option_type)."""
    rows = conn.execute(
        "SELECT DISTINCT strike FROM options "
        "WHERE trade_date=? AND symbol=? AND expiry=? AND option_type=? "
        "ORDER BY strike",
        (trade_date, symbol, expiry, option_type),
    ).fetchall()
    return [r[0] for r in rows]


def get_settle(conn: sqlite3.Connection, symbol: str, trade_date: str,
               expiry: str, option_type: str, strike: float):
    row = conn.execute(
        "SELECT settle_pr FROM options "
        "WHERE trade_date=? AND symbol=? AND expiry=? AND option_type=? AND strike=?",
        (trade_date, symbol, expiry, option_type, strike),
    ).fetchone()
    return row[0] if row else None


def get_open_interest(conn: sqlite3.Connection, symbol: str, trade_date: str,
                      expiry: str, option_type: str, strike: float) -> int:
    row = conn.execute(
        "SELECT open_int FROM options "
        "WHERE trade_date=? AND symbol=? AND expiry=? AND option_type=? AND strike=?",
        (trade_date, symbol, expiry, option_type, strike),
    ).fetchone()
    return int(row[0]) if row else 0


def symbols_on_date(conn: sqlite3.Connection, trade_date: str) -> list:
    """Returns all symbols that have option data on trade_date."""
    rows = conn.execute(
        "SELECT DISTINCT symbol FROM options WHERE trade_date=?", (trade_date,)
    ).fetchall()
    return [r[0] for r in rows]


def stats(conn: sqlite3.Connection):
    total = conn.execute("SELECT COUNT(*) FROM options").fetchone()[0]
    syms = conn.execute("SELECT COUNT(DISTINCT symbol) FROM options").fetchone()[0]
    dates = conn.execute("SELECT COUNT(DISTINCT trade_date) FROM options").fetchone()[0]
    first = conn.execute("SELECT MIN(trade_date) FROM options").fetchone()[0]
    last = conn.execute("SELECT MAX(trade_date) FROM options").fetchone()[0]
    print(f"Rows:       {total:,}")
    print(f"Symbols:    {syms}")
    print(f"Trade days: {dates}  ({first} → {last})")


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Build SQLite index from Bhavcopy ZIPs")
    ap.add_argument("--force", action="store_true", help="Drop and rebuild from scratch")
    ap.add_argument("--stats", action="store_true", help="Show database stats and exit")
    ap.add_argument("--include-index", action="store_true",
                    help="Also include OPTIDX (index options) in addition to OPTSTK")
    args = ap.parse_args()

    if args.stats:
        conn = connect()
        stats(conn)
        conn.close()
    else:
        instruments = ("OPTSTK", "OPTIDX") if args.include_index else ("OPTSTK",)
        build(force=args.force, instruments=instruments)
