import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("原始数组：")
print(arr)
print("-" * 40)

res1 = arr[1, 0:3]
print("1. 第2行第1~3列：", res1)

res2 = arr[:, 2]
print("2. 所有行第3列：", res2)

res3 = arr[::2, :]
print("3. 奇数行（第1、3行）：")
print(res3)