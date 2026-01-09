import pytest
from app.fetcher import fetch_stock_data

def test_invalid_ticker():
    with pytest.raises(ValueError):
        fetch_stock_data("INVALIDTICKER123")