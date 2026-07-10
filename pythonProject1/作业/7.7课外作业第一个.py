
student_dict = {}

def main_menu():
    print("\n====== 学生成绩管理系统 ======")
    print("1. 录入学生成绩")
    print("2. 根据学号查询学生信息")
    print("3. 全班成绩统计")
    print("4. 退出系统")

def add_student():
    sid = input("请输入学生学号：").strip()
    if sid in student_dict:
        print("该学号已存在，无法重复录入！")
        return
    name = input("请输入学生姓名：").strip()
    try:
        chinese = float(input("语文成绩："))
        math = float(input("数学成绩："))
        english = float(input("英语成绩："))
    except ValueError:
        print("成绩必须输入数字，录入失败！")
        return
    student_dict[sid] = {
        "姓名": name,
        "语文": chinese,
        "数学": math,
        "英语": english
    }
    print(f"学生 {name} 信息录入成功！")

def search_student():
    sid = input("请输入要查询的学号：").strip()
    if sid not in student_dict:
        print("未查询到该学号学生！")
        return
    info = student_dict[sid]
    total = info["语文"] + info["数学"] + info["英语"]
    avg = total / 3
    print("-" * 30)
    print(f"学号：{sid}")
    print(f"姓名：{info['姓名']}")
    print(f"语文：{info['语文']}  数学：{info['数学']}  英语：{info['英语']}")
    print(f"总分：{total:.2f}  平均分：{avg:.2f}")
    print("-" * 30)

def class_statistic():
    if len(student_dict) == 0:
        print("暂无任何学生数据！")
        return
    all_scores = []
    for s in student_dict.values():
        all_scores.append(s["语文"])
        all_scores.append(s["数学"])
        all_scores.append(s["英语"])
    max_score = max(all_scores)
    min_score = min(all_scores)
    avg_score = sum(all_scores) / len(all_scores)
    print("===== 全班成绩总统计 =====")
    print(f"所有科目最高分：{max_score:.2f}")
    print(f"所有科目最低分：{min_score:.2f}")
    print(f"所有科目平均分：{avg_score:.2f}")

while True:
    main_menu()
    choice = input("请输入功能序号(1-4)：").strip()
    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        class_statistic()
    elif choice == "4":
        print("系统退出，感谢使用！")
        break
    else:
        print("输入无效，请输入1~4之间的数字！")