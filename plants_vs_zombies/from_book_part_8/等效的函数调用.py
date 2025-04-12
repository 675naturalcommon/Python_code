#关键字实参,默认值实参和位置实参的使用

def greet(name, greeting="Hello", punctuation="!"):
    print(greeting, name, punctuation)

greet("Alice") # Hello Alice!
greet("Bob", "Hi") # Hi Bob!
greet("Charlie", punctuation=".") # Hello Charlie.
greet("David", "Howdy", ",") # Howdy David,
greet("Eve", punctuation="?") # Hello Eve?
