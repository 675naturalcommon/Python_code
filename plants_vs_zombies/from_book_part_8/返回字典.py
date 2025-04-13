#函数可返回字典，并将其打印出来。

def get_dict():
    my_dict = {'apple': 5, 'banana': 7, 'orange': 3}
    return my_dict

my_dict = get_dict()
print(my_dict)

def buile_dict(fruit, quantity):
    my_dict = {}
    my_dict[fruit] = quantity
    return my_dict

fruit = input("Enter a fruit: ")
quantity = int(input("Enter the quantity: "))
my_dict = buile_dict(fruit, quantity)
print(my_dict)

def build_person(first_name, last_name, age, city):
    person = {}  #创建一个空字典,可以添加键值对
    person['first_name'] = first_name  #添加键值对'first_name': first_name
    person['last_name'] = last_name  #添加键值对'last_name': last_name
    person['age'] = age  #添加键值对'age': age
    person['city'] = city  #添加键值对'city': city
    return person

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
person = build_person(first_name, last_name, age, city)
print(person)