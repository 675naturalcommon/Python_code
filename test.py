
# This is a test file for the Plants vs. Zombies game.
people = []
person = {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'city': 'New York'}
people.append(person)

person = {'first_name': 'Jane', 'last_name': 'Smith', 'age': 25, 'city': 'Los Angeles'}
people.append(person)

person = {'first_name': 'Bob', 'last_name': 'Johnson', 'age': 40, 'city': 'Chicago'}
people.append(person)

person = {'first_name': 'Alice', 'last_name': 'Williams', 'age': 35, 'city': 'San Francisco'}
people.append(person)

for person in people:
    try:
        first_name = person['first_name'].title()
        last_name = person['last_name'].title()
        age = person['age']
        city = person['city'].title()
        print(f'{first_name} {last_name} is {age} years old and lives in {city}.')
    except KeyError as e:
        print("Error: Person object is missing a required key.")

