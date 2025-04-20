def make_car(manufacture,model,**options):
    #创建一个用于表示汽车的字典
    car_dict = {'manufacture':manufacture.title(),
                'model':model.title()}
    #添加选项到字典中
    for key,value in options.items():
        car_dict[key] = value
    return car_dict

#测试
car = make_car('Toyota','Camry',color='red',year=2020)
print(car)

