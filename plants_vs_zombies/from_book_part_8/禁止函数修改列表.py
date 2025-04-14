#切片表示法是一种访问列表元素的简便方法。但是，切片表示法并不总是创建副本，因此，如果修改了切片表示法创建的副本，则原始列表也会受到影响。

#禁止函数修改列表

#为了防止函数修改列表，可以将列表作为参数传递给函数，而不是直接修改列表。这样，函数就可以修改副本，而不会影响原始列表。

#例如，假设有一个函数，它需要修改列表中的元素，但是不希望函数修改原始列表。可以将列表作为参数传递给函数，并在函数中修改副本，然后返回修改后的副本。

#下面是一个例子：

def modify_list(lst):
    new_lst = lst[:] #创建副本
    for i in range(len(new_lst)):#遍历副本
        new_lst[i] = new_lst[i] * 2 #修改副本
    return new_lst #返回修改后的副本

#现在，可以调用这个函数来修改列表：

my_list = [1, 2, 3, 4, 5]
new_list = modify_list(my_list)
print(my_list) #输出：[1, 2, 3, 4, 5]
print(new_list) #输出：[2, 4, 6, 8, 10]

#可以看到，函数修改了副本，而原始列表没有受到影响。


unprinend_desiens = ['iphone cace', 'galaxy note 10', 'iphone x', 'iphone 11']

def modify_list(lst):
    new_lst = lst[:] #创建副本
    for i in range(len(new_lst)):#遍历副本
        new_lst[i] = new_lst[i].upper() #修改副本
        #uppper()方法将字符串转换为大写字母
        #lower()方法将字符串转换为小写字母
    return new_lst #返回修改后的副本

new_list = modify_list(unprinend_desiens)
print(unprinend_desiens)
#输出：['iphone cace', 'galaxy note 10', 'iphone x', 'iphone 11']
print(new_list) #输出：['IPHONE CACE', 'GALAXY NOTE 10', 'IPHONE X', 'IPHONE 11']