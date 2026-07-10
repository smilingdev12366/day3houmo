import numpy as np
np.random.seed(42)

ret_matrix = np.random.normal(loc=0.0005, scale=0.015, size=(1000, 252))


daily_std = np.std(ret_matrix, axis=1, ddof=1)
annual_vol = daily_std * np.sqrt(252)
print("前5支股票年化波动率：", np.round(annual_vol[:5], 3))

corr_mat = np.corrcoef(ret_matrix)
print("相关系数矩阵形状：", corr_mat.shape)
print("前3×3相关系数：\n", np.round(corr_mat[:3,:3], 2))