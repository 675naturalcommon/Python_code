from random import choice

def get_winning_ticket(possibilities):
    #摇出中奖组合
    winning_ticket = []

    #中奖组合不能包含重复的数字或字母,因此使用了while循环
    while len(winning_ticket) < 4:
        random_ticket =[choice(possibilities) for i in range(4)]
        if len(set(random_ticket)) == 4:
            winning_ticket = random_ticket

    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    #检查彩票的数字或字母,只要有一个不在中奖组合中,就返回false
    for i in range(4):
        if played_ticket[i] not in winning_ticket:
            return False
    return True
#下面是另一种实现方式for循环
#   for element in played_ticket:
#       if element not in winning_ticket:
#           return False
#   return True

def random_make_ticket(possibilities):
    #随机生成4个数字或字母组成的彩票
    random_ticket = [choice(possibilities) for i in range(4)]
    #彩票不能包含重复的数字或字母,因此使用了set函数
    if len(set(random_ticket)) == 4:
        return random_ticket
    else:
        return random_make_ticket(possibilities)
    #进行递归,使生成的彩票符合要求

possibilities = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False
#为避免程序执行时间太长,设置最多生成多少张彩票
max_tries = 1_000_000

while not won:
    new_ticket = random_make_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        print("程序执行时间太长,请重新运行程序")
        break

if won:
    print("恭喜你,你赢得了这张彩票!")
    print("你用了", plays, "次猜测, 共生成了", max_tries, "张彩票")
    print("中奖组合是:", winning_ticket)
    print("你猜测的彩票是:", new_ticket)
else:
    print("很遗憾,你没有猜中彩票!")
