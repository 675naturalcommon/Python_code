#enumerate()方法是python的内置函数,用于在遍历可迭代对象(如列表,元组,字符串等)时,同时获取元素值及其对应的索引

#语法规则

#enumerate(iterable, start=0)

#参数说明:
#iterable(必填): 可迭代对象,如列表,元组,字符串等
#start(可选): 起始索引值,默认为0,可以设置为任意整数(如start=2,则索引值从2开始)

#返回值:
#返回一个enumerate对象,生成由(index, value)组成的元组
#包含两个属性:
#index: 元素的索引值
#value: 元素的值

my_list = ['apple', 'banana', 'orange']
print(list(enumerate(my_list)))
#输出:[(0, 'apple'), (1, 'banana'), (2, 'orange')]

#默认索引(从0开始)

fruits = ['apple', 'banana', 'orange']
for index, fruit in enumerate(fruits):
    print(index, fruit)
    print(f"索引{index}对应的水果是{fruit}")

#自定义起始索引(如从1开始)
for index, fruit in enumerate(fruits, start=1):
    print(f"第{index}个水果是{fruit}")

#结合字典遍历键值对
my_dict = {"name":"Alice","age":30,"city":"Beijing"}
for index, (key, value) in enumerate(my_dict.items()):
    print(f"第{index+1}个键值对是{key}:{value}")

#处理嵌套数据结构
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row_index, row in enumerate(matrix):
    for col_index, col in enumerate(row):
        print(f"第{row_index+1}行第{col_index+1}列元素为{col}")