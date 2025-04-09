#编写⼀个程序，调查⽤户梦想中的度假胜地。
# 使⽤类似于“If you could visit one place in the world, where would you go?”的提⽰，并编写⼀个打印调查结果的代码块

print("Hello! Welcome to the Plants vs. Zombies survey!")
print("If you didn't have a favorite place, you can say 'quit' to end the survey.")

favorite_place = input("What is your favorite place to visit? ")

while favorite_place!= "quit":
    print("I would also like to visit " + favorite_place + "!")
    favorite_place = input("What is your favorite place to visit? ")

print("Thank you for your input!")