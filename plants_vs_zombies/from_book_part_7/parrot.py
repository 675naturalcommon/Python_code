#使用while循环在用户愿意时让程序不断的运行
prompt = "Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message!= "quit":
    message = input(prompt)
    if message!= "quit":
        print(message)


#若在上面的代码中添加一个标志变量，则可以让程序在用户输入quit时退出循环，而不是一直循环下去：
prompt = "Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
flag = True
while flag:
    message = input(prompt)
    if message == "quit":
        flag = False
    else:
        print(message)