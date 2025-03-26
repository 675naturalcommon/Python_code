players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #0,1,2
print(players[1:4]) #1,2,3
print(players[:4])#没有指定索引,python自动从列表头开始
print(players[0:])#没有指定结束,python到末尾结束

print('Here are the first three players on my team:')
for player in  players[:3]:
    print(player.title())

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print('My favorite foods are:')
print(my_foods)

print('\nMy friend\'s favorite foods are:')
print(friend_foods)

my_foods.append('cannoli')
print('My favorite foods are:')
print(my_foods)
print('\nMy friend\'s favorite foods are:')
friend_foods.append('ice cream')
print(friend_foods)