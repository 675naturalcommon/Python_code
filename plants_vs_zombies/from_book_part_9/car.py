class Car:
    def __init__(self, make, model, year, color):
       #初始化描述汽车的属性
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
#speed属性是在__init__()方法内部直接赋值的,初始值为0
#它是一个默认属性,所有Car对象在创建时都会自动拥有这个属性,而不需要外部传递值
    def accelerate(self, amount):
        #增加汽车的速度
        self.speed += amount

    def brake(self, amount):
        #减少汽车的速度
        self.speed -= amount

#__str__()是一个特殊方法,当我们使用print(对象)或str(对象)时,会自动调用这个方法
    def __str__(self):
        #返回汽车的描述信息
        return f"{self.color} {self.year} {self.make} {self.model} with speed {self.speed} mph"
#__repr__()是一个特殊方法,它返回一个对象的字符串形式,可以用eval()方法重新创建对象
#这个方法的作用是方便开发者调试代码,可以看到对象的所有属性和它们的值
#当我们使用repr(对象)时,会自动调用这个方法
    def __repr__(self):
        #返回汽车的详细信息
        return f"Car(make='{self.make}', model='{self.model}', year={self.year}, color='{self.color}')"
    #测试代码
    def test(self):
        print("test")

car1 = Car("Toyota", "Corolla", 2021, "red")
print(car1)
print(repr(car1))
car1.accelerate(10)
print(car1)
car1.brake(5)
print(car1)
car1.test()