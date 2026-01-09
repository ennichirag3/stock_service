from fastapi import APIRouter, HTTPException
from app.fetcher import fetch_stock_data
from app.storage import insert, fetch_all, fetch_last

router = APIRouter()

@router.post("/fetch")
def fetch(ticker: str):
    try:
        data = fetch_stock_data(ticker)
        insert(data)
        return {"status": "stored", "data": data}
    except Exception as e:
        raise HTTPException(400, str(e))

@router.get("/last")
def last():
    return {"data": fetch_last()}

@router.get("/history")
def history():
    return {"data": fetch_all()}