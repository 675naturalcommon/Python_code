class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name}.")
        print(f"The cuisine type of the restaurant is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

    def __str__(self):
        return f"The {self.cuisine_type} restaurant {self.name} has served {self.number_served} people."
#_str_()方法是一个特殊方法，用于定义对象的字符串表示形式。当我们使用print()函数打印对象时，Python会自动调用这个方法。
#在这个例子中，我们定义了一个Restaurant类，包含了餐厅的名称、菜系类型和已服务人数等属性。我们还定义了一些方法来描述餐厅、开餐厅、设置已服务人数和增加已服务人数。最后，我们重写了__str__()方法，以便在打印对象时输出餐厅的名称、菜系类型和已服务人数等信息。

restaurant = Restaurant("The Grill", "American")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(10)
print(restaurant) #output: The American restaurant The Grill has served 10 people.
restaurant.increment_number_served(5)
print(restaurant) #output: The American restaurant The Grill has served 15 people.
