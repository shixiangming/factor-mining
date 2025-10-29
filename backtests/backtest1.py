import pandas as pd
import numpy as np
from utils.performance import sharpe_ratio
from utils.visualization import plot_cumulative

def backtest_momentum(momentum, price_data):
    """简单月度多空回测"""
    returns = price_data.pct_change()
    monthly_dates = price_data.resample("ME").last().index

    portfolio_returns = []
    for date in monthly_dates:
        if date not in momentum.index:
            continue
        m = momentum.loc[date].dropna()
        if len(m) < 2:
            continue
        top = m.nlargest(1).index
        bottom = m.nsmallest(1).index
        next_month = returns.loc[date:].iloc[1:21]
        if len(next_month) == 0:
            continue
        long_ret = next_month[top].mean(axis=1)
        short_ret = next_month[bottom].mean(axis=1)
        portfolio_ret = long_ret - short_ret
        portfolio_returns.append(portfolio_ret)

    portfolio_returns = pd.concat(portfolio_returns)
    sr = sharpe_ratio(portfolio_returns)
    print(f"Sharpe Ratio: {sr:.2f}")
    plot_cumulative(portfolio_returns)
    return portfolio_returns

