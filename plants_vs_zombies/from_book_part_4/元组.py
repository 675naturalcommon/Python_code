#Python将不能修改的值称为不可变的,不可变的列表称为元组
#列表用方括号来标识,而元组用圆括号标识

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#如果你要定义只包含一个元素的元组,那么在这一个元素后面一定要加逗号
#通常只有一个元素的元组没有意义,但自动生成的元组通常只包含一个元素
nums = (2,)
print(nums)

#给元组变量重新赋值是合法的,但修改元组变量中的元素是不合法的
dimensions = (100,50)
print(dimensions)
#dimensions[0] = 100
#TypeError: 'tuple' object does not support item assignment


animals = ('chicken','dog','cat','elephant','tiger')
for animal in animals:
    print(animal)

new_animals = animals[:]
print(new_animals)