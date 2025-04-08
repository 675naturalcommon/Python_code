flag = True
while flag:
    age = int(input("Enter your age: "))
    if age < 3:
        print("YOu are free to watch the movie.")
    elif age >= 3 and age < 12:
        print("You have to pay $10 for the movie.")
    elif age >= 12:
        print("You have to pay $15 for the movie.")
