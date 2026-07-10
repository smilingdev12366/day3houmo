import math
LOG_FILE = "calc_log.txt"

def add_calc(a, b):
    return a + b

# 2 减法
def sub_calc(a, b):
    return a - b

def mul_calc(a, b):
    return a * b

def div_calc(a, b):
    if b == 0:
        raise ZeroDivisionError("除数不能为0")
    return a / b

def power_calc(a, b):
    return a ** b

def sqrt_calc(num):
    if num < 0:
        raise ValueError("负数无法开平方")
    return math.sqrt(num)

def write_log(content):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(content + "\n")
    except Exception as e:
        print(f"日志写入失败：{e}")

def read_log():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if not lines:
            print("暂无历史计算记录")
            return
        print("\n===== 历史计算记录 =====")
        for line in lines:
            print(line.strip())
    except FileNotFoundError:
        print("日志文件不存在，还没有计算记录")
    except Exception as e:
        print(f"读取文件异常：{e}")

def calc_menu():
    print("\n===== 多功能计算器 =====")
    print("1.加法  2.减法  3.乘法  4.除法")
    print("5.幂运算  6.开平方  7.查看历史记录  0.退出")

def main():
    while True:
        calc_menu()
        try:
            op = int(input("请输入功能编号："))
        except ValueError:
            print("输入必须是数字！")
            continue

        if op == 0:
            print("计算器退出")
            break
        elif op == 7:
            read_log()
            continue

        if op in (1,2,3,4,5):
            try:
                n1 = float(input("输入第一个数："))
                n2 = float(input("输入第二个数："))
            except ValueError:
                print("请输入合法数字！")
                continue

            res = None
            expr = ""
            if op == 1:
                res = add_calc(n1, n2)
                expr = f"{n1} + {n2} = {res}"
            elif op == 2:
                res = sub_calc(n1, n2)
                expr = f"{n1} - {n2} = {res}"
            elif op == 3:
                res = mul_calc(n1, n2)
                expr = f"{n1} * {n2} = {res}"
            elif op == 4:
                res = div_calc(n1, n2)
                expr = f"{n1} / {n2} = {res}"
            elif op == 5:
                res = power_calc(n1, n2)
                expr = f"{n1} ** {n2} = {res}"

            print("计算结果：", expr)
            write_log(expr)

        elif op == 6:
            try:
                num = float(input("输入需要开平方的数字："))
                res = sqrt_calc(num)
                expr = f"sqrt({num}) = {res}"
                print("计算结果：", expr)
                write_log(expr)
            except (ValueError, Exception) as e:
                print("计算出错：", e)
        else:
            print("编号超出范围，请重新选择！")

if __name__ == "__main__":
    main()