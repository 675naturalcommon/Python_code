class Dog:#在python中，类名的首字母应大写，以表示它是一个类
    #一次模拟小狗的简单尝试
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over.")

#_init_()方法是类的构造函数，它在创建对象时自动调用。它可以用来设置对象的初始属性值。
#在这里，我们定义了三个属性：name、age、breed。它们分别代表狗的名字、年龄和品种。
#然后，我们定义了两个方法：sit()和roll_over()。它们分别代表狗坐下和打滚。
#最后，我们创建了一个Dog类的对象，并给它赋值。我们可以打印出对象的属性值，并调用它的两个方法。


my_dog = Dog("Buddy", 3, "Labrador")
print(my_dog.name)
print(my_dog.age)
print(my_dog.breed)
my_dog.sit()
my_dog.roll_over()

#设置默认参数
class Dog:
    def __init__(self, name, age=3, breed="Labrador"):
        self.name = name
        self.age = age
        self.breed = breed

my_dog = Dog("Buddy")
print(my_dog.name)
print(my_dog.age)
print(my_dog.breed)

#使用类属性
class Dog:
    species = "Canis familiaris"  # 类属性

    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age  # 实例属性

    def speak(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy", 3)
print(my_dog.species)  # 访问类属性
print(my_dog.speak())  # 调用实例方法

#执行初始化逻辑
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        print(f"{owner}'s account has been created with a balance of {balance}.")

account = BankAccount("Alice")
# Output: Alice's account has been created with a balance of 0.

account = BankAccount("Bob", 1000)
# Output: Bob's account has been created with a balance of 1000.

#继承
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
#python内置raise语句用于抛出异常，这里的实现是抛出了一个NotImplementedError异常，NotImplementedError是一个特殊的异常,用于指示一个功能尚未实现。
#如果子类没有实现父类的抽象方法，调用该方法时会抛出NotImplementedError异常。
class Dog(Animal):
    def speak(self):
        return self.name + " says Woof!"

my_dog = Dog("Buddy")
print(my_dog.speak())  # Output: Buddy says Woof!

#多重继承
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Mammal(Animal):
    pass

class Dog(Mammal):
    def speak(self):
        return self.name + " says Woof!"

my_dog = Dog("Buddy")
print(my_dog.speak())  # Output: Buddy says Woof!