def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#形参名*toppings表示接收任意数量的实参，并将它们组成一个元组。


#结合使用位置实参和任意数量实参时，位置实参必须出现在任意数量实参之前。

def make_pizza(size, *toppings):
    print(f"Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('large', 'pepperoni')
make_pizza('medium', 'pepperoni', 'mushrooms', 'green peppers', 'extra cheese')

#使用任意数量的关键字实参时，必须在最后一个位置实参之后。

def make_pizza(size, *toppings, **kwargs):
    print(f"Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

make_pizza('large', 'pepperoni', cheese='mozzarella')
make_pizza('medium', 'pepperoni', 'mushrooms', 'green peppers', 'extra cheese', sauce='marinara')

#形参名**kwargs表示接收任意数量的关键字实参，并将它们组成一个字典。