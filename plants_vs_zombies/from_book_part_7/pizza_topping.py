#编写⼀个循环，提⽰⽤户输⼊⼀系列⽐萨配料，并在⽤户输⼊'quit'时结束循环
# 每当⽤户输⼊⼀种配料后，都打印⼀条消息，指出要在⽐萨中添加这种配料。

while True:
    topping = input("Enter a topping (or 'quit' to stop): ")
    if topping == 'quit':
        break
    print("Adding", topping, "to your pizza.")