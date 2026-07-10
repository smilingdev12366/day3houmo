import numpy as np

arr = np.random.rand(10)
print("原始0~1随机浮点数组：")
print(arr)

arr_min = arr.min()
arr_max = arr.max()

norm_arr = (arr - arr_min) / (arr_max - arr_min) * 100
print("\n归一化到[0,100]后的数组：")
print(norm_arr)

cumsum_arr = np.cumsum(norm_arr)
cummax_arr = np.maximum.accumulate(norm_arr)

print("\n累计和 np.cumsum：")
print(cumsum_arr)
print("\n累计最大值 np.maximum.accumulate：")
print(cummax_arr)