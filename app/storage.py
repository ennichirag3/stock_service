import sqlite3
from app.config import settings

def get_conn():
    return sqlite3.connect(settings.DB_PATH)

def init_db():
    with get_conn() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            ticker TEXT,
            timestamp TEXT,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume INTEGER,
            PRIMARY KEY (ticker, timestamp)
        )
        """)

def insert(data: dict):
    with get_conn() as conn:
        conn.execute("""
        INSERT OR IGNORE INTO prices VALUES (?,?,?,?,?,?,?)
        """, tuple(data.values()))

def fetch_all():
    with get_conn() as conn:
        rows = conn.execute("SELECT * FROM prices ORDER BY timestamp").fetchall()
    return rows

def fetch_last():
    with get_conn() as conn:
        return conn.execute("SELECT * FROM prices ORDER BY timestamp DESC LIMIT 1").fetchone()