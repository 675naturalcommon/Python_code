import sandwich_orders

sandwich_orders = ['BLT', 'PB&J', 'Honey Mustard', 'Grilled Cheese', 'Fries', 'Onion Rings']
sandwich_orders.append('pastrami')
sandwich_orders.append('pastrami')
sandwich_orders.append('pastrami')
sandwich_orders.append('pastrami')
sandwich_orders.append('pastrami')
print(sandwich_orders)
print("I'm sorry, we are all out of pastrami sandwiches.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("Here are the remaining sandwich orders:")
print(sandwich_orders)