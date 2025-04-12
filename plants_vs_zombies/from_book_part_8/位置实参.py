def describe_pet(animal_type,pet_name):
    # 打印宠物信息
    print("This is a",animal_type,"named",pet_name)

# 调用函数
describe_pet("cat","Fluffy")

#1.可根据需要调用函数任意多次
describe_pet("dog","Fido")

#2.位置实参的顺序很重要
describe_pet("fish","Nemo")
describe_pet("Nemo","fish") # 错误，位置实参顺序不正确

#3.位置实参可以省略，但必须按照顺序提供
describe_pet("bird") # 错误，缺少位置实参