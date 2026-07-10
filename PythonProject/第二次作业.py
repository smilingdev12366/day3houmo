import random
student_id="2025113928"
seed=int(student_id[-2:])
random.seed(seed)
num_list=[random.randint(1,100)for_in range(10)]
print("原始列表:",num_list)
last_digit=int(student_id[-1])
ascending=last_digit%2==1
list_sorted_inplace=num_list.copy()
list_sorted_inplace.sort(reverse=not ascending)
print("使用list.sort()排序后:",list_sorted_inplace)


