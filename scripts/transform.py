import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.config import STOCK_NAME, DATA_PATH

def transform_data():
    df = pd.read_csv(f"{DATA_PATH}/raw_stock_data.csv")

    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df.dropna(inplace=True)

    df['Daily_Return'] = df['Close'].pct_change()
    df['Moving_Avg'] = df['Close'].rolling(3).mean()

    df.to_csv(f"{DATA_PATH}/clean_stock_data.csv", index=False)

if __name__ == "__main__":
    transform_data()