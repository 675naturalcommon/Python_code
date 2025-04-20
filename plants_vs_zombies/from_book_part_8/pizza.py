def make_pizza(size, *toppings):
    #概述要制作的披萨
    pizza = {'size': size, 'toppings': list(toppings)}
    return pizza


def add_topping(pizza, topping):
    #给披萨添加配料
    pizza['toppings'].append(topping)
    return pizza
def remove_topping(pizza, topping):
    #从披萨中移除配料
    if topping in pizza['toppings']:
        pizza['toppings'].remove(topping)
    return pizza