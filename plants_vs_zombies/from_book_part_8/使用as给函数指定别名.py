#使用as给函数指定别名
from pizza import make_pizza as mp

print(mp('large', 'pepperoni', 'cheese'))

#使用as给模块指定别名
import pizza as p

print(p.make_pizza('large', 'pepperoni', 'cheese'))

#使用*运算符可让python导入模块中的所有函数
from pizza import *

print(make_pizza('large', 'pepperoni', 'cheese'))

#一般情况下,不建议使用*运算符导入模块中的所有函数，因为可能会导致命名冲突。
#如果确实需要导入模块中的所有函数，可以将函数名用列表形式存储在一个变量中，然后使用*运算符导入。
from pizza import make_pizza, add_topping, remove_topping

pizza = make_pizza('large', 'pepperoni', 'cheese')
print("初始的pizza:", pizza)
pizza_toppings = [add_topping, remove_topping]

for topping in pizza_toppings:
    if topping ==add_topping:
        pizza = add_topping(pizza, 'bacon')
        print("添加了bacon的pizza:", pizza)
    elif topping == remove_topping:
        pizza = remove_topping(pizza, 'cheese')
        print("移除了cheese的pizza:", pizza)

print(pizza)

