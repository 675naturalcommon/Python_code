respenses = {}
#设置一个标志,指出调查是否要继续
polling_active = True

while polling_active:
    #提示输入被调查者的名字和回答
    name = input("What is your name? ")
    respense = input("Which mountain would you like to climb someday? ")
    #将回答添加到字典中
    respenses[name] = respense
    #将用户的姓名和他们希望攀登的山脉名称作为键值对添加到字典 respenses 中。
    #询问是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

#打印出调查结果
print("--- Poll Results ---")
for name, respense in respenses.items():
    print(name + " would like to climb " + respense + ".")