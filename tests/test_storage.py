from app.storage import insert, fetch_all, init_db

def test_db_write_read():
    init_db()
    sample = {
        "ticker": "TEST",
        "timestamp": "2025",
        "open": 1, "high": 2, "low": 1, "close": 2, "volume": 100
    }
    insert(sample)
    data = fetch_all()
    assert len(data) >= 1