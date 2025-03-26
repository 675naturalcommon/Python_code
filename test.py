person = {
    'first_name':'三',
    'last_name':'张',
    'age':'22',
    'city':'北京',
}
print(person)
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
print(person['last_name']+person['first_name'])

favorite_numbers = {
    'mandy': 42,
    'micah': 23,
    'gus': 7,
    'hank': 1_000_000,
    'maggie': 0,
}

num = favorite_numbers['mandy']
print(f'Mandy\'s favorite num is {num}')

num = favorite_numbers['micah']
print(f'Micah\'s favorite num is {num}')

num = favorite_numbers['gus']
print(f'Gus\'s favorite num is {num}')

num = favorite_numbers['hank']
print(f'Hank\'s favorite num is {num}')

num = favorite_numbers['maggie']
print(f'Maggie\'s favorite num is {num}')

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
}

word = 'string'
print(f"\n{word.title()}:{glossary['string']}")

word = 'comment'
print(f"\n{word.title()}:{glossary['comment']}")

word = 'list'
print(f"\n{word.title()}:{glossary['list']}")

word = 'loop'
print(f"\n{word.title()}:{glossary['loop']}")

word = 'dictionary'
print(f"\n{word.title()}:{glossary['dictionary']}")

glossary = {
'string': 'A series of characters.',
'comment': 'A note in a program that the Python interpreter ignores.',
'list': 'A collection of items in a particular order.',
'loop': 'Work through a collection of items, one at a time.',
'dictionary': "A collection of key-value pairs.",
'key': 'The first item in a key-value pair in a dictionary.',
'value': 'An item associated with a key in a dictionary.',
'conditional test': 'A comparison between two values.',
'float': 'A numerical value with a decimal component.',
'boolean expression': 'An expression that evaluates to True or False.',
}

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")
