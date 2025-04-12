#当你写入函数的实参与函数里的形参数目不匹配时，Python会报错。
# 为了避免这种错误，你可以在函数定义时，指定形参数目的数量和类型。
# 这样，当你调用函数时，Python会检查实参的数量和类型是否与函数定义的一致。

def greet(name: str, age: int) -> str:
#    -> str:这是函数的返回类型注释,表示这个函数返回的值应该是一个字符串,这不是强制性的
#    但是强烈建议你加上这个注释，因为它可以让其他程序员更容易理解你的函数的用途。
    return f"Hello, {name}! You are {age} years old."

# 调用函数时，必须传入两个参数，一个是字符串，一个是整数。
print(greet("Alice", 25))  # Output: Hello, Alice! You are 25 years old.

# 调用函数时，传入一个参数，Python会报错。
# print(greet("Alice"))  # TypeError: greet() missing 1 required positional argument: 'age'

