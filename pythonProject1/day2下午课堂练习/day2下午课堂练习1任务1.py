import numpy as np
import timeit
A = np.random.rand(1000, 2000)
B = np.random.rand(2000, 3000)

t_dot = timeit.timeit(lambda: np.dot(A, B), number=3)

t_at = timeit.timeit(lambda: A @ B, number=3)

t_matmul = timeit.timeit(lambda: np.matmul(A, B), number=3)

print("=== 矩阵乘法耗时(3次平均) ===")
print(f"np.dot(A,B):    {t_dot:.2f} s")
print(f"A @ B:          {t_at:.2f} s")
print(f"np.matmul(A,B): {t_matmul:.2f} s")