import numpy as np

# 全局存储学生数据：两个列表分别存姓名、成绩，后续转numpy数组计算
student_names = []
student_scores = np.array([], dtype=int)


def show_menu():
    """打印系统主菜单"""
    print("============================")
    print("     成绩分析系统")
    print("============================")
    print("1. 输入成绩数据")
    print("2. 查看成绩统计")
    print("3. 查看成绩排名")
    print("4. 查看成绩分布")
    print("5. 查询学生成绩")
    print("6. 退出系统")
    print("============================")


def input_scores():
    """功能1：录入学生姓名与成绩"""
    global student_names, student_scores
    # 清空原有数据，重新录入
    student_names.clear()
    student_scores = np.array([], dtype=int)

    while True:
        try:
            stu_count = int(input("请输入学生人数："))
            if stu_count <= 0:
                print("人数必须是大于0的整数，请重新输入！")
                continue
            break
        except ValueError:
            print("输入格式错误，请输入数字！")

    temp_scores = []
    for i in range(1, stu_count + 1):
        name = input(f"请输入第{i}个学生姓名：")
        while True:
            try:
                score = int(input("请输入成绩："))
                if 0 <= score <= 100:
                    break
                else:
                    print("成绩范围必须在0-100之间，请重新输入！")
            except ValueError:
                print("成绩必须为数字，请重新输入！")
        student_names.append(name)
        temp_scores.append(score)
    # 转为numpy数组
    student_scores = np.array(temp_scores)
    print(f"\n成功录入{stu_count}名学生成绩！")


def stat_analysis():
    """功能2：成绩统计（均值、最值、中位数、方差等，numpy计算）"""
    if len(student_names) == 0:
        print("暂无成绩数据，请先录入！")
        return
    print("\n==========成绩统计分析==========")
    print(f"学生总人数：{student_scores.size}")
    print(f"最高分：{np.max(student_scores)}")
    print(f"最低分：{np.min(student_scores)}")
    print(f"平均分：{np.round(np.mean(student_scores), 2)}")
    print(f"中位数：{np.median(student_scores)}")
    print(f"成绩方差：{np.round(np.var(student_scores), 2)}")
    print(f"成绩标准差：{np.round(np.std(student_scores), 2)}")


def rank_analysis():
    """功能3：成绩排名，从高到低排序"""
    if len(student_names) == 0:
        print("暂无成绩数据，请先录入！")
        return
    print("\n==========成绩排名（由高到低）==========")
    # numpy获取排序索引
    sort_index = np.argsort(-student_scores)
    for rank, idx in enumerate(sort_index, start=1):
        name = student_names[idx]
        score = student_scores[idx]
        print(f"第{rank}名：{name}，分数：{score}")


def dist_analysis():
    """功能4：成绩分布等级划分（优90-100、良80-89、中60-79、差0-59）"""
    if len(student_names) == 0:
        print("暂无成绩数据，请先录入！")
        return
    total = student_scores.size
    # numpy布尔索引筛选各等级人数
    excellent = np.sum((student_scores >= 90) & (student_scores <= 100))
    good = np.sum((student_scores >= 80) & (student_scores < 90))
    middle = np.sum((student_scores >= 60) & (student_scores < 80))
    bad = np.sum((student_scores >= 0) & (student_scores < 60))

    print("\n==========成绩分布分析==========")
    print(f"优秀(90~100分)：{excellent}人，占比{np.round(excellent / total * 100, 2)}%")
    print(f"良好(80~89分)：{good}人，占比{np.round(good / total * 100, 2)}%")
    print(f"中等(60~79分)：{middle}人，占比{np.round(middle / total * 100, 2)}%")
    print(f"不及格(0~59分)：{bad}人，占比{np.round(bad / total * 100, 2)}%")


def query_student():
    """功能5：根据姓名查询学生成绩"""
    if len(student_names) == 0:
        print("暂无成绩数据，请先录入！")
        return
    search_name = input("请输入要查询的学生姓名：")
    if search_name in student_names:
        idx = student_names.index(search_name)
        score = student_scores[idx]
        # 计算排名
        sort_index = np.argsort(-student_scores)
        rank = list(sort_index).index(idx) + 1
        print(f"\n查询结果：{search_name}，成绩：{score}，全班排名：第{rank}名")
    else:
        print(f"未找到名为【{search_name}】的学生！")


def main():
    """程序主循环"""
    while True:
        show_menu()
        select = input("请选择：")
        if select == "1":
            input_scores()
        elif select == "2":
            stat_analysis()
        elif select == "3":
            rank_analysis()
        elif select == "4":
            dist_analysis()
        elif select == "5":
            query_student()
        elif select == "6":
            print("程序已退出，再见！")
            break
        else:
            print("输入错误，请选择1-6之间的数字！")
        # 暂停，回车返回菜单
        input("\n按回车键返回主菜单...")
        print("\n")


if __name__ == "__main__":
    main()