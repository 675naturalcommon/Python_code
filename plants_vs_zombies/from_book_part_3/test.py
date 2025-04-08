"""
names=['Bill','Bob','Eric','Franc','Alice']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

message = f'{names[0]},How are you?'
print(message)
"""

#如果你可以邀请任何⼈⼀起共进晚餐（⽆论是在世的还是故去的）你会邀请哪些⼈?
# 请创建⼀个列表，其中包含⾄少三个你想邀请的⼈，然后使⽤这个列表打印消息，邀请这些⼈都来与你共进晚餐

'''
guests=['guido van rossum','jack turner','lynn hill']

names=guests[0].title()
print(f'{names},please come to dinner!')
names=guests[1].title()
print(f'{names},please come to dinner!')
names=guests[2].title()
print(f'{names},please come to dinner!')

"""
你刚得知有位嘉宾⽆法赴约，因此需要另外邀请⼀位嘉宾.以完成上面练习时编写的程序为基础,
在程序末尾添加函数调⽤print(),指出哪位嘉宾⽆法赴约
修改嘉宾名单，将⽆法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名.再次打印⼀系列消息，向名单中的每位嘉宾发出邀请。
"""
removed_guests=guests.pop(1)
print(f'Sorry,{removed_guests.title()}can\'t come to dinner!')

print(guests)
guests.insert(1,'linda')
print(guests)
print(f'{guests[1].title()},please come to dinner!')
"""

"""
你刚找到了一张更大的餐桌，可容纳更多的嘉宾就座。请想想你还想邀请哪三位嘉宾。 
以上面练习时编写的程序为基础，在程序末尾添加函数调用print()，指出你找到了一张更大的餐桌。 
使用insert()将一位新嘉宾添加到名单开头。 
使用insert()将另一位新嘉宾添加到名单中间。 
使用append()将最后一位新嘉宾添加到名单末尾。 
打印一系列消息，向名单中的每位嘉宾发出邀请
'''

'''
guests=['guido van rossum','jack turner','lynn hill']

names=guests[0].title()
print(f'{names},please come to dinner!')
names=guests[1].title()
print(f'{names},please come to dinner!')
names=guests[2].title()
print(f'{names},please come to dinner!')

#jack无法赴约
names=guests[1].title()
print(f'Sorry,{names} can\'t come to dinner!')

#删除Jack
del guests[1]
guests.insert(1,'linda snyder')

#打印新的邀请函
names=guests[0].title()
print(f'\n{names},please come to dinner!')
names=guests[1].title()
print(f'{names},please come to dinner!')
names=guests[2].title()
print(f'{names},please come to dinner!')

#找到了更大的餐桌,再邀请一些嘉宾
print('\nWe got a bigger table!')
guests.insert(0,'frida kahlo')
guests.insert(2,'reinhold messner')
guests.append('elizabeth peratrovich')

print(f'{guests[0].title()},please come to dinner!')
print(f'{guests[1].title()},please come to dinner!')
print(f'{guests[2].title()},please come to dinner!')
print(f'{guests[3].title()},please come to dinner!')
print(f'{guests[4].title()},please come to dinner!')
print(f'{guests[5].title()},please come to dinner!')

'''
'''
你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。 
以完成上面练习时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两
位嘉宾共进晚餐的消息。 
使用pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位
嘉宾时，都打印一条消息，让该嘉宾知道你很抱歉，无法邀请他来共进晚餐。 
对于余下两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀之列。 
使用del将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实名单在程
序结束时确实是空的。

'''
'''
print('\nSorry,The table can\'t reach on time!So I can only invite two guests more!')

#删除名单上的客人,只剩下两位
guests.pop()
guests.pop()
guests.pop()
guests.pop()

#检查剩余名单上的客人
print()
print(guests)

#邀请剩余名单上的客人
print(f'\n{guests[0].title()},please come to dinner!')
print(f'{guests[1].title()},please come to dinner!')

#删除名单
del guests[0]
del guests[0]
#检查名单
print(guests)
'''

cities=['yunnan','shanghai','xinjiang','xizang','beijing']
print(cities)

#使⽤sorted()按字⺟顺序打印这个列表,不要修改它
print(sorted(cities))

#再次打印该列表,核实排列顺序未变
print(cities)

#使⽤sorted()按与字⺟顺序相反的顺序打印这个列表,不要修改它
print(sorted(cities,reverse=True))

#再次打印该列表,核实排列顺序未变
print(cities)

#使⽤reverse()修改列表元素的排列顺序.打印该列表,核实排列顺序确实变了
cities.reverse()
print(cities)

#使⽤reverse()再次修改列表元素的排列顺序.打印该列表,核实已恢复到原来的排列顺序.
cities.reverse()
print(cities)

#使⽤sort()修改该列表,使其元素按字⺟顺序排列.打印该列表,核实排列顺序确实变了
cities.sort()
print(cities)

#使⽤sort()修改该列表,使其元素按与字⺟顺序相反的顺序排列.打印该列表,核实排列顺序确实变了
cities.sort(reverse=True)
print(cities)