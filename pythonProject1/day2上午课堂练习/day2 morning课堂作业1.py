import numpy as np
arr = np.random.randint(low=0, high=10, size=(3, 4))
print("原始数组 arr (3,4)：")
print(arr)
print("arr 形状：", arr.shape)
print("-" * 40)

reshaped_arr = arr.reshape(4, 3).T
print("重塑+转置后的数组：")
print(reshaped_arr)
print("重塑转置后形状：", reshaped_arr.shape)
print("-" * 40)

filtered_arr = arr[arr > 5]
print("大于5的元素组成的新数组：")
print(filtered_arr)