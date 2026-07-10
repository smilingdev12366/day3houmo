import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('Agg')
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

np.random.seed(42)
n_trade_days = 252
n_stocks = 3
S0 = np.array([100, 120, 95])

mu = np.array([0.08, 0.06, 0.10])
sigma = np.array([0.18, 0.22, 0.25])
dt = 1 / n_trade_days

Z = np.random.normal(0, 1, (n_trade_days, n_stocks))
drift = (mu - 0.5 * sigma ** 2) * dt
shock = sigma * np.sqrt(dt) * Z

daily_log_ret = drift + shock

cum_log = np.cumsum(daily_log_ret, axis=0)
price_series = S0 * np.exp(cum_log)
price_series = np.vstack([S0, price_series])

stock1_price = price_series[:, 0]

log_returns = np.log(price_series[1:] / price_series[:-1])

daily_std = np.std(log_returns, axis=0, ddof=1)
annual_vol = daily_std * np.sqrt(n_trade_days)
print("===== 单只股票年化波动率 =====")
for i, vol in enumerate(annual_vol):
    print(f"股票{i+1} 年化波动率: {vol:.2%}")

def calc_ma(price_arr, window):
    """计算移动平均线"""
    cumsum_p = np.cumsum(price_arr)
    window_sum = cumsum_p[window-1:] - np.pad(cumsum_p[:-window], (1,0), mode="constant")
    return window_sum / window

ma5 = calc_ma(stock1_price, window=5)
ma20 = calc_ma(stock1_price, window=20)

cov_matrix = np.cov(log_returns.T, ddof=1)
print("\n===== 收益率协方差矩阵 =====")
print(np.round(cov_matrix, 6))

corr_matrix = np.corrcoef(log_returns.T)
print("\n===== 收益率相关系数矩阵 =====")
print(np.round(corr_matrix, 2))

weight = np.array([1/n_stocks, 1/n_stocks, 1/n_stocks])

port_variance = weight @ cov_matrix @ weight
port_volatility = np.sqrt(port_variance)
port_annual_vol = port_volatility * np.sqrt(n_trade_days)
print(f"\n等权重组合年化波动率: {port_annual_vol:.2%}")

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

ax1 = axes[0,0]
ax1.plot(stock1_price, label="股票1价格", color="#2E86AB", linewidth=1.5)
ax1.plot(np.arange(4, len(ma5)+4), ma5, label="MA5", color="#A23B72", linewidth=2)
ax1.plot(np.arange(19, len(ma20)+19), ma20, label="MA20", color="#F18F01", linewidth=2)
ax1.set_title("股票价格与移动平均线", fontsize=12)
ax1.set_xlabel("交易日")
ax1.set_ylabel("股价")
ax1.legend()
ax1.grid(alpha=0.3)

ax2 = axes[0,1]
ax2.hist(log_returns[:,0], bins=30, color="#C73E1D", alpha=0.7)
ax2.set_title("股票1日对数收益率分布", fontsize=12)
ax2.set_xlabel("日收益率")
ax2.set_ylabel("频次")
ax2.grid(alpha=0.3)

ax3 = axes[1,0]
stock_name = ["股票1","股票2","股票3"]
colors = ["#2E86AB","#A23B72","#F18F01"]
for idx in range(n_stocks):
    ax3.plot(price_series[:,idx], label=stock_name[idx], color=colors[idx])
ax3.set_title("三只股票价格走势对比", fontsize=12)
ax3.set_xlabel("交易日")
ax3.set_ylabel("股价")
ax3.legend()
ax3.grid(alpha=0.3)

ax4 = axes[1,1]
im = ax4.imshow(corr_matrix, cmap="coolwarm", vmin=-1, vmax=1)
ax4.set_xticks([0,1,2])
ax4.set_yticks([0,1,2])
ax4.set_xticklabels(stock_name)
ax4.set_yticklabels(stock_name)
ax4.set_title("股票收益相关系数热力图", fontsize=12)

for i in range(n_stocks):
    for j in range(n_stocks):
        ax4.text(j, i, f"{corr_matrix[i,j]:.2f}", ha="center", va="center", color="black")
fig.colorbar(im, ax=ax4)

plt.tight_layout()
