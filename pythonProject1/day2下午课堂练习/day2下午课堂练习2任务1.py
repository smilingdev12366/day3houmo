import numpy as np
prices = np.array([100, 102, 105, 103, 107])

log_returns = np.log(prices[1:] / prices[:-1])
print("股价序列：", prices)
print("对数收益率：", np.round(log_returns, 4))