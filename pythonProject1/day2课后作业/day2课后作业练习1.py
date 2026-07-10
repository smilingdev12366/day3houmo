
import numpy as np

print("====================== 1. 创建不同维度数组 ======================")

arr_1d = np.array([1, 2, 3, 4, 5])
print("一维数组 arr_1d：", arr_1d)
print(f"一维数组 维度ndim={arr_1d.ndim}，形状shape={arr_1d.shape}\n")

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("二维数组 arr_2d：")
print(arr_2d)
print(f"二维数组 维度ndim={arr_2d.ndim}，形状shape={arr_2d.shape}\n")

arr_3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("三维数组 arr_3d：")
print(arr_3d)
print(f"三维数组 维度ndim={arr_3d.ndim}，形状shape={arr_3d.shape}\n")

zero_arr = np.zeros((2, 3))
ones_arr = np.ones((3, 2))
print("全零矩阵 zeros((2,3))：\n", zero_arr)
print("全一矩阵 ones((3,2))：\n", ones_arr)

print("\n====================== 2. 数组索引与切片 ======================")

print("【一维数组操作】")
print(f"取第3个元素 arr_1d[2] = {arr_1d[2]}")
print(f"切片前3个元素 arr_1d[:3] = {arr_1d[:3]}")
print(f"倒序切片 arr_1d[::-1] = {arr_1d[::-1]}")
print(f"步长2取值 arr_1d[::2] = {arr_1d[::2]}\n")

print("【二维数组操作】")
print(f"第二行第三列元素 arr_2d[1,2] = {arr_2d[1,2]}")
print("前两行 arr_2d[:2]：")
print(arr_2d[:2])
print("所有行，前两列 arr_2d[:, :2]：")
print(arr_2d[:, :2])
print("隔一行取全部列 arr_2d[::2, :]：")
print(arr_2d[::2, :], "\n")

print("【三维数组操作】")
print(f"第0块、第1行、第0列 arr_3d[0,1,0] = {arr_3d[0,1,0]}")
print("所有块，第0行 arr_3d[:, 0, :]：")
print(arr_3d[:, 0, :])

print("\n====================== 3. 数组形状变换 ======================")
origin_arr = np.array([1, 2, 3, 4, 5, 6])
print(f"原始一维数组：{origin_arr}，shape={origin_arr.shape}")

reshape_2d = origin_arr.reshape(2, 3)
print("reshape(2,3) 转为二维：")
print(reshape_2d)

flat_arr = reshape_2d.flatten()
print(f"展平flatten：{flat_arr}")

trans_test = np.array([[1,2],[3,4],[5,6]])
print("待转置矩阵：")
print(trans_test)
print("转置 .T：")
print(trans_test.T)

print(f"原三维数组shape：{arr_3d.shape}")
swap_3d = arr_3d.transpose(2, 0, 1)
print(f"三维数组置换维度后shape：{swap_3d.shape}")

print("\n====================== 4. 自定义矩阵运算函数 ======================")
def mat_add(a, b):
    """矩阵加法：要求两个矩阵形状完全一致"""
    if a.shape != b.shape:
        raise ValueError("错误：两个矩阵维度不一致，无法相加！")
    return a + b

def mat_mul(a, b):
    """标准数学矩阵乘法：第一个矩阵列数 = 第二个矩阵行数"""
    if a.shape[1] != b.shape[0]:
        raise ValueError("错误：矩阵不满足乘法维度规则，A列数需等于B行数！")
    return a @ b

def mat_transpose(a):
    """矩阵转置"""
    return a.T

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
add_result = mat_add(m1, m2)
mul_result = mat_mul(m1, m2)
trans_result = mat_transpose(m1)

print("矩阵 m1：\n", m1)
print("矩阵 m2：\n", m2)
print("矩阵相加 m1+m2：\n", add_result)
print("标准矩阵乘法 m1@m2：\n", mul_result)
print("m1矩阵转置：\n", trans_result)

print("\n====================== 5. 随机数组生成与统计分析 ======================")

rand_data = np.random.normal(loc=0, scale=1, size=(10, 10))
print(f"随机数组尺寸 shape={rand_data.shape}")

print(f"全局平均值 mean = {rand_data.mean():.3f}")
print(f"全局标准差 std = {rand_data.std():.3f}")
print(f"全局最大值 max = {rand_data.max():.3f}")
print(f"全局最小值 min = {rand_data.min():.3f}")
print(f"中位数(50%分位数) = {np.percentile(rand_data, 50):.3f}")

row_avg = rand_data.mean(axis=1)
col_total = rand_data.sum(axis=0) 
print(f"每行平均值（前5个）：{np.round(row_avg[:5], 3)}")
print(f"每列总和（前5个）：{np.round(col_total[:5], 3)}")