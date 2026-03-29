import yfinance as yf
import pandas as pd

def fetch_data():
    df = yf.download("AAPL", period="7d", interval="1d")
    df.reset_index(inplace=True)
    df.to_csv("data/raw_stock_data.csv", index=False)

fetch_data()