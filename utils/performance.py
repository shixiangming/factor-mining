import numpy as np

def sharpe_ratio(returns):
    """计算年化 Sharpe 比率"""
    return np.mean(returns) / np.std(returns) * (252 ** 0.5)

