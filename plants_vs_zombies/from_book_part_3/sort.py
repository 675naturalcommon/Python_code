cars = ['bmw','audi','toyoda','subaru']
print(cars)

#sort()按字母顺序排列,sort()永久修改列表中的排列顺序
cars.sort()      #等价于cars=cars.sorted(cars)
print(cars)

#还可以按字母表相反顺序排列列表,添加reverse=True即可,同样对列表修改也是永久的
cars.sort(reverse=True)
print(cars)

#要保留列表元素原来的排列顺序,并以特定的顺序呈现他们,使用sorted()函数
#sorted()可让你用特定顺序显示列表元素,且不改变原来列表中元素的排列顺序

cars = ['bmw','audi','toyoda','subaru']
print('\nHere is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)