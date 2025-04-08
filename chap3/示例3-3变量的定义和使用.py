luck_number=6
my_name='单浩然'  #字符串类型的变量

'''
和c/c++不同的是不需要事先声明变量的类型
'''

print(luck_number,'的数据类型是',type(luck_number))  #<class 'int'>
print(my_name,'的幸运数字是',luck_number)

#Python动态修改变量的数据类型,通过赋不同类型的值就可以直接修改
luck_number=my_name=6
print(luck_number,my_name)

luck_number='北京欢迎你!'
print(luck_number,'的数据类型是',type(luck_number))

#在Python中允许多个变量同时指向同一个值
no=number=1024
print(no,number)
print(id(no))      #id查看变量在内存中的地址
print(id(number))

a=max(100,30)
print(a)
print(max(99,30))
MAX=100
print(MAX)