#input函数让程序暂停运行，等待用户输入一些文本。
#input函数返回用户输入的字符串。
#input函数的参数是提示信息，显示在用户输入时。

message = input("Tell me something,and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"Hello,{name.title()}!")