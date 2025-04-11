def greet_user():
    print("Welcome to Plants vs. Zombies!")

greet_user()

def greet_user(name):
    print("Welcome, " + name + " to Plants vs. Zombies!")

greet_user("John")

def greet_user(name = ""):
    if name:
        print("Welcome, " + name + " to Plants vs. Zombies!")
    else:
        print("Welcome to Plants vs. Zombies!")

greet_user()
greet_user("Jane")

