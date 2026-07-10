import numpy as np
A = np.random.rand(2000, 2000)
res_opt = np.empty_like(A)
temp = np.empty_like(A)

np.multiply(A, A, out=temp)

np.add(temp, np.multiply(2, A, out=temp), out=res_opt)
np.add(res_opt, 1, out=res_opt)