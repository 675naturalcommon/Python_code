#创建一个用于存储宠物的空列表
pets = []

#定义各个宠物,并将其存储在列表中
pet = {'animal_type': 'cat','owner': 'Alice', 'name': 'Fluffy', 'age': 3, 'hunger': 10}
pets.append(pet)

pet = {'animal_type': 'dog','owner': 'Bob', 'name': 'Rufus', 'age': 5, 'hunger': 8}
pets.append(pet)

pet = {'animal_type': 'fish','owner': 'Charlie', 'name': 'Nemo', 'age': 1, 'hunger': 0}
pets.append(pet)

#打印宠物列表
print(pets)

#显示每个宠物的信息
for pet in pets:
    print(f"Here is what I know about {pet['name'].title()}:")
    print(f"Animal type: {pet['animal_type'].title()}")
    print(f"Owner: {pet['owner'].title()}")
    print(f"Age: {pet['age']}")
    print(f"Hunger level: {pet['hunger']}")
    print() #打印一个空行