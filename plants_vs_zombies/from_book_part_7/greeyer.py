prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name?"
name = input(prompt)
print(f"hello {name}")

#上面的示例演示了一种创建多行字符串的方法，并在其中添加变量。
#当使用input()函数时,python会将用户输入的字符串作为字符串处理
#因此,如果用户输入的是数字,则会报错,需要使用int()函数将其转换为整数
#同样,如果用户输入的是浮点数,则需要使用float()函数将其转换为浮点数
#如果用户输入的是布尔值,则需要使用bool()函数将其转换为布尔值
#如果用户输入的是列表,则需要使用list()函数将其转换为列表
#如果用户输入的是元组,则需要使用tuple()函数将其转换为元组
#如果用户输入的是字典,则需要使用dict()函数将其转换为字典
#如果用户输入的是集合,则需要使用set()函数将其转换为集合
#如果用户输入的是对象,则需要使用eval()函数将其转换为对象
#如果用户输入的是函数,则需要使用exec()函数将其转换为函数
#如果用户输入的是None,则需要使用None作为输入值
#如果用户输入的是空字符串,则会返回空字符串
#如果用户输入的是空格,则会返回空格
#如果用户输入的是换行符,则会返回换行符
#如果用户输入的是制表符,则会返回制表符
#如果用户输入的是其他字符,则会返回该字符

height = input("What is your height in meters? ")
height = float(height)
if height >= 1.7:
    print("You are tall enough to ride.")
else:
    print("You are not tall enough to ride.")