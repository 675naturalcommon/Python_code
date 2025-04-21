class Car:
    def __init__(self,make,model,year,color,):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.odometer_reading = 0
        self.speed = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model} ({self.color})"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def accelerate(self,speed):
        self.speed += speed

    def brake(self,brake_pressure):
        self.speed -= brake_pressure

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self,make,model,year,color,battery_type):
        super().__init__(make,model,year,color)
        self.battery_type = battery_type

    def fill_gas_tank(self):
        print("Filling up the gas tank...")

    def charge_battery(self):
        print("Charging the battery...")

    def test(self):
        print("Testing the electric car...")

    def __str__(self):
        return f"{self.get_descriptive_name()} with a {self.battery_type} battery with speed {self.speed} mph and {self.odometer_reading} miles on it."

    def __repr__(self):
        return f"ElectricCar('make' = '{self.make}','model' = '{self.model}', 'year' = {self.year}, 'color' = '{self.color}', 'battery_type' = '{self.battery_type}')"

car1 = ElectricCar("Tesla","Model S",2021,"black","Li-ion")
print(car1)
print(repr(car1))
car1.accelerate(10)
print(car1)
car1.brake(5)
print(car1)
car1.test()
car1.fill_gas_tank()
car1.charge_battery()
car1.read_odometer()
car1.update_odometer(20)
car1.read_odometer()
car1.increment_odometer(10)