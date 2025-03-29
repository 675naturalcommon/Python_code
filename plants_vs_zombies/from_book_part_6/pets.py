#创建一个用于存储宠物的空列表
pets = []

#定义一个函数，用于创建宠物
def create_pet(name, species, age):
    #创建一个字典，用于存储宠物的相关信息
    pet = {'name': name,'species': species, 'age': age}
    #将宠物的字典添加到pets列表中
    pets.append(pet)

#定义一个函数，用于打印宠物列表
def print_pets():
    #打印宠物列表的标题
    print("List of Pets:")
    #遍历pets列表，打印每个宠物的相关信息
    for pet in pets:
        print(f"Name: {pet['name']}, Species: {pet['species']}, Age: {pet['age']}")

#调用create_pet函数创建三个宠物
create_pet('Fluffy', 'cat', 3)
create_pet('Buddy', 'dog', 5)
create_pet('Squeaky', 'hamster', 2)

#调用print_pets函数打印宠物列表
print_pets()        