from car0 import Car

my_car = Car("Toyota", "Corolla", 2015, "silver")
print(my_car.get_descriptive_name())
my_car.update_odometer(23_000)
my_car.read_odometer()
my_car.increment_odometer(100)
my_car.read_odometer()