def greet_users(names):
    for name in names:
        print(f"Hello, {name.title()}!")

users = ["Alice", "Bob", "Charlie"]
greet_users(users)