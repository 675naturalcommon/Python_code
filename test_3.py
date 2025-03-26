import os

# 密码文件路径
PASSWORD_FILE = "password.txt"


def set_password():
    """设置并确认新密码"""
    while True:
        pwd1 = input("请设置查询密码（首次使用）: ").strip()
        if not pwd1:
            print("密码不能为空！")
            continue
        pwd2 = input("请再次确认密码: ").strip()
        if pwd1 == pwd2:
            with open(PASSWORD_FILE, "w") as f:
                f.write(pwd1)
            print("密码设置成功！")
            return pwd1
        print("两次输入不一致，请重新设置")


def get_password():
    """获取存储的密码"""
    try:
        with open(PASSWORD_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"读取密码失败: {str(e)}")
        exit()


# 主程序逻辑
def main():
    # 检查是否已有密码
    stored_pwd = get_password()

    # 首次使用需要设置密码
    if not stored_pwd:
        print("欢迎首次使用成绩查询系统")
        stored_pwd = set_password()

    # 密码验证
    input_pwd = input("请输入查询密码: ")
    if input_pwd != stored_pwd:
        print("密码错误，退出系统")
        exit()

    # 姓名验证
    while True:
        name = input("请输入姓名: ").strip()
        if name == "zhangtiaopi":
            break
        print("姓名错误，请重新输入")

    # 成绩输入
    while True:
        try:
            score = float(input("请输入成绩: "))
            if 0 <= score <= 100:
                break
            print("成绩需在0-100之间")
        except ValueError:
            print("请输入有效数字")

    # 等级判定
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = '不及格'

    print(f"\n姓名: {name}\n成绩: {score}\n等级: {grade}")


if __name__ == "__main__":
    main()