'''
#设置密码环节
secret = input('请设置你的查询密码:')
print('恭喜你,密码设置成功!')
print('\n')

while True:
    password = input('请输入你的查询密码:')
    if password == secret:
        print('进入下一环节设计!')
    else:
        print('密码错误!')

    flag = input('是否继续输入:')
    if flag == 'No':
        break

#身份验证环节

while True:
    name = input('请输入你的名字:')
    if name == 'zhangfanyu':
        print('进入下一环节设计!')
    else:
        print('这不是你的密码查询系统!')

    flag = input('是否继续输入:')
    if flag == 'No':
        break
'''

# 设置查询密码
correct_password = "mima123"

# 验证密码
input_pwd = input("请输入查询密码：")
if input_pwd != correct_password:
    print("密码错误，退出系统。")
    exit()

# 验证姓名
while True:
    name = input("请输入姓名：")
    if name == "zhangtiaopi":
        break
    print("姓名错误，请重新输入。")

# 验证并输入成绩
while True:
    try:
        score = float(input("请输入成绩："))
        if 0 <= score <= 100:
            break
        else:
            print("成绩必须在0到100之间，请重新输入。")
    except ValueError:
        print("输入无效，请输入数字。")

# 判断成绩等级
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

print(f"您的成绩等级为：{grade}")