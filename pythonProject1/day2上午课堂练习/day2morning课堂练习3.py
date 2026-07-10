import numpy as np
A = np.random.randint(1, 10, size=(2, 3))
B = np.random.randint(1, 10, size=(2, 3))
print("数组A：")
print(A)
print("数组B：")
print(B)

elem_mul = A * B
print("\n逐元素乘法 A * B：")
print(elem_mul)

mat_mul = A @ B.T
print("\n矩阵乘法 A @ B.T：")
print(mat_mul)
print("-" * 50)

arr_sum = np.array([[1, 2], [3, 4]])
print("待求和数组：")
print(arr_sum)

sum_col = np.sum(arr_sum, axis=0)
print("\n按列求和 axis=0：", sum_col)

sum_row = np.sum(arr_sum, axis=1)
print("按行求和 axis=1：", sum_row)
print("-" * 50)

arr_stat = np.array([1.2, 3.5, 2.8])
print("统计数组：", arr_stat)

mean_val = np.mean(arr_stat)
std_val = np.std(arr_stat)
round_val = np.round(arr_stat)

print("均值 np.mean：", mean_val)
print("标准差 np.std：", std_val)
print("四舍五入 np.round：", round_val)