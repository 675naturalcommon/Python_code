from car0 import ElectricCar

my_car = ElectricCar("Tesla", "Model S", 2021, "black", 70)
print(my_car.get_descriptive_name())
my_car.battery.describe_battery()
my_car.battery.get_range()