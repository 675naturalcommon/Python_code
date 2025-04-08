car = input("What kinf of car do you want to buy?")
print(f"Let me see if I can find you a {car.title()}")

party_sizy = int(input("How many people are in your party?"))
if party_sizy > 6:
    print("Sorry, we don't have that many cars available.")
else:
    print(f"Ok, I can help you find a {car.title()} for {party_sizy} people.")


#让用户输入一个数,指出这个数是否是10的整数倍

num = int(input("Enter a number: "))
if num % 10 == 0:
    print(f"{num} is a multiple of 10.")
else:
    print(f"{num} is not a multiple of 10.")


