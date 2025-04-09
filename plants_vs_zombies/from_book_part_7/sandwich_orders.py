sandwich_orders = ['BLT', 'PB&J', 'Honey Mustard', 'Grilled Cheese', 'Fries', 'Onion Rings']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("I finished all your sandwiches!")
print("The following sandwiches were made:")
for sandwich in finished_sandwiches:
    print(sandwich)