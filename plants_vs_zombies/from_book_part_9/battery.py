class ElectricCar:
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f"{self.year.title()} {self.make.title()} {self.model.title()} {self.color.title()}"

    def __repr__(self):
        return f"Car('{self.make}','{self.model}','{self.year}','{self.color}')"


class Battery:
    #一次模拟电动汽车的电池
    def __init__(self,capacity,charge_rate):
        self.capacity = capacity
        self.charge_rate = charge_rate

    def __str__(self):
        return f"Battery with capacity of {self.capacity} and charge rate of {self.charge_rate}"

    def __repr__(self):
        return f"Battery({self.capacity},{self.charge_rate})"

my_car = ElectricCar("Tesla","Model S","2021","red")
my_battery = Battery(100,0.8)
print(my_car)
print(my_battery)