from random import randint

class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        #返回一个位于1和筛子面数之间的随机数
        return randint(1, self.sides)

#创建一个6面的筛子,在掷10并显示结果
my_die = Die(6)
results = []
for i in range(10):
    results.append(my_die.roll_die())
print("10-rolls of a 6-sided die:")
print(results)

#创建一个10面的筛子,在掷10并显示结果
my_die = Die(10)
results = []
for i in range(10):
    results.append(my_die.roll_die())
print("\n10-rolls of a 10-sided die:")
print(results)

#创建一个20面的筛子,在掷10并显示结果
my_die = Die(20)
results = []
for i in range(10):
    result = my_die.roll_die()
    results.append(result)
print("\n10-rolls of a 20-sided die:")
print(results)
