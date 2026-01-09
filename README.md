# Stock Service

A small Python service that fetches stock market data, stores it locally, and exposes it via a REST API using FastAPI.  

---

## Table of Contents
- [Overview](#overview)
- [Setup & Run Instructions](#setup--run-instructions)
- [API Endpoints](#api-endpoints)
- [Architecture & Design Decisions](#architecture--design-decisions)
- [Assumptions & Limitations](#assumptions--limitations)
- [Testing](#testing)
- [Optional Extensions](#optional-extensions)
- [License](#license)

---

## Overview

This service allows users to:

1. Fetch OHLCV (Open, High, Low, Close, Volume) data for a given stock ticker using Yahoo Finance.
2. Store the data locally in a SQLite database.
3. Access the data via API endpoints:
   - Latest data
   - Historical data
   - Trigger new fetch operations

Technologies used: Python 3, FastAPI, yfinance, SQLite, Pydantic.

---

## Setup & Run Instructions

### 1️⃣ Clone the repo
```bash
git clone https://github.com/ennichirag3/stock_service.git
cd stock_service
