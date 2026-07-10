import numpy as np
np.random.seed(42)
price_100d = np.cumsum(np.random.randn(100)) + 100

def moving_avg_conv(arr, window):
    kernel = np.ones(window) / window
    return np.convolve(arr, kernel, mode="valid")

ma5 = moving_avg_conv(price_100d, 5)
ma20 = moving_avg_conv(price_100d, 20)
print(f"原始价格长度:{len(price_100d)}, MA5长度:{len(ma5)}, MA20长度:{len(ma20)}")