import yfinance as yf
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.config import STOCK_NAME, DATA_PATH

def fetch_data():
    df = yf.download(STOCK_NAME, period="7d", interval="1d")
    df.reset_index(inplace=True)
    df.to_csv(f"{DATA_PATH}/raw_stock_data.csv", index=False)

if __name__ == "__main__":
    fetch_data()