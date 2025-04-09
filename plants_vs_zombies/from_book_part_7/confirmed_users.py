#while循环和列表的使用
#首先,创建一个待验证用户列表
#然后,创建一个空列表来存储已验证用户
unconfirmed_users = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
confirmed_users = []

#使用while循环来验证用户,直到所有用户都被验证完毕
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    # 在 print() 中强制刷新
    print(f"Verifying user: {current_user}", flush=True)
    confirmed_users.append(current_user)

#打印已验证用户的列表
print(confirmed_users)

import sys
print("当前 Python 路径:", sys.executable)
print("当前环境路径:", sys.prefix)