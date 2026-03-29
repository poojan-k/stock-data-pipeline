import pandas as pd

def transform_data():
    df = pd.read_csv("data/raw_stock_data.csv")

    df.dropna(inplace=True)

    # FIX: convert to numeric
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

    df['Daily_Return'] = df['Close'].pct_change()
    df['Moving_Avg'] = df['Close'].rolling(3).mean()

    df.to_csv("data/clean_stock_data.csv", index=False)

transform_data()