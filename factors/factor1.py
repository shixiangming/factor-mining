import pandas as pd

def momentum_factor(price_data, window=20):
    """计算动量因子：过去 window 日涨幅"""
    return price_data.pct_change(window)
