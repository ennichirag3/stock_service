# app/main.py
from fastapi import FastAPI, HTTPException, Query
import yfinance as yf

app = FastAPI()

@app.get("/fetch")
def fetch_stock(ticker: str = Query(..., description="Stock ticker symbol, e.g., AAPL")):
    """
    Fetch stock info for the given ticker.
    Example: /fetch?ticker=AAPL
    """
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1mo")  # last 1 month data
        if data.empty:
            raise HTTPException(status_code=404, detail="No data found for this ticker")
        
        # return only last row as example
        latest = data.iloc[-1].to_dict()
        result = {
            "ticker": ticker.upper(),
            "latest_data": latest
        }
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))