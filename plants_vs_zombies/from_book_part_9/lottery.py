from random import choice

possibilities = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']

winning_ticket = []

print("Let's see what the winning ticket is!")

#中奖组合中不能包含重复的数字或字母,因此包含了while循环
while len(winning_ticket) < 4:
    #随机选择4个数字或字母
    random_ticket = [choice(possibilities) for i in range(4)]
    #choice(possibilities)函数从列表possibilities中随机选择一个元素
    #for i in range(4)表示重复这个过程次，每次选择一个元素并添加到列表random_ticket中
    #上面的代码并没有保证抽取的四个元素是不重复的

    #判断是否有重复的数字或字母
    if len(set(random_ticket)) == 4:
        winning_ticket = random_ticket
    #set(random_ticket)函数将列表random_ticket转换为一个集合,集合是一个无序且不重复的数据结构
    #如果集合的长度等于4,说明没有重复的数字或字母

print("The winning ticket is:", winning_ticket)