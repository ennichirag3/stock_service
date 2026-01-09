import yfinance as yf
from datetime import datetime

def fetch_stock_data(ticker: str, interval="1d"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d", interval=interval)

    if hist.empty:
        raise ValueError("Invalid ticker or no data")

    row = hist.iloc[-1]

    return {
        "ticker": ticker.upper(),
        "timestamp": datetime.utcnow().isoformat(),
        "open": float(row["Open"]),
        "high": float(row["High"]),
        "low": float(row["Low"]),
        "close": float(row["Close"]),
        "volume": int(row["Volume"])
    }