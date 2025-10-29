import datetime
from utils.data_loader import get_stock_data
from factors.factor1 import momentum_factor
from backtests.backtest1 import backtest_momentum

if __name__ == "__main__":
    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime(2024, 12, 31)
    tickers = ["AAPL", "MSFT", "GOOG"]

    # 1. 加载数据
    price_data = {t: get_stock_data(t, start, end) for t in tickers}
    import pandas as pd
    price_data = pd.DataFrame(price_data)

    # 2. 计算因子
    momentum = momentum_factor(price_data, window=20)

    # 3. 回测
    backtest_momentum(momentum, price_data)
