import numpy as np
import timeit
arr_c = np.random.rand(1000, 1000)
arr_f = np.array(arr_c, order="F")

print("arr_c C连续:", arr_c.flags.c_contiguous, "F连续:", arr_c.flags.f_contiguous)
print("arr_f C连续:", arr_f.flags.c_contiguous, "F连续:", arr_f.flags.f_contiguous)

time_c_row = timeit.timeit(lambda: arr_c.sum(axis=1), number=20)
time_c_col = timeit.timeit(lambda: arr_c.sum(axis=0), number=20)
time_f_row = timeit.timeit(lambda: arr_f.sum(axis=1), number=20)
time_f_col = timeit.timeit(lambda: arr_f.sum(axis=0), number=20)

print("\n=== 内存布局求和耗时 ===")
print(f"C顺序 行求和(axis=1): {time_c_row:.3f}s")
print(f"C顺序 列求和(axis=0): {time_c_col:.3f}s")
print(f"F顺序 行求和(axis=1): {time_f_row:.3f}s")
print(f"F顺序 列求和(axis=0): {time_f_col:.3f}s")