import os
import pandas as pd
from pandas_datareader import data as web

def get_stock_data(ticker, start, end, data_dir="data", force_update=False):
    """下载或加载股票数据（自动缓存）"""
    os.makedirs(data_dir, exist_ok=True)
    filename = os.path.join(data_dir, f"{ticker}_stooq.csv")

    if not force_update and os.path.exists(filename):
        print(f"✅ Loading cached data for {ticker}")
        df = pd.read_csv(filename, index_col=0, parse_dates=True)
    else:
        print(f"⬇️ Downloading {ticker} from stooq...")
        df = web.DataReader(ticker, "stooq", start, end).sort_index()
        df.to_csv(filename)
        print(f"💾 Saved to {filename}")
    return df["Close"]

