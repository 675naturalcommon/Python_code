class Restaurant:
    def __init__(self, name, location, cuisine_type):
        self.name = name
        self.location = location
        self.cuisine_type = cuisine_type

    def __str__(self):
        return f"Restaurant name: {self.name}, location: {self.location}, cuisine_type: {self.cuisine_type}"

    def __repr__(self):
        return f"Restaurant(name='{self.name}', location='{self.location}', cuisine_type='{self.cuisine_type}')"

class Icecreamstand(Restaurant):
    def __init__(self, name, location, flavors):
        self.name = name
        self.location = location
        self.flavors = flavors

    def __str__(self):
        return f"Icecreamstand name: {self.name}, location: {self.location}, flavors: {self.flavors}"

    def __repr__(self):
        return f"Icecreamstand(name='{self.name}', location='{self.location}', flavors={self.flavors})"

    def display_flavors(self):
        print(f"The flavors of {self.name} are: {self.flavors}")

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def remove_flavor(self, flavor):
        self.flavors.remove(flavor)

    def get_flavors(self):
        return self.flavors

#Testing the Icecreamstand class
icecream_stand = Icecreamstand("Ice Cream Stand", "123 Main St", ["vanilla", "chocolate", "strawberry"])
print(icecream_stand)
icecream_stand.display_flavors()
icecream_stand.add_flavor("mint")
icecream_stand.display_flavors()
icecream_stand.remove_flavor("chocolate")
icecream_stand.display_flavors()
print(icecream_stand.get_flavors())