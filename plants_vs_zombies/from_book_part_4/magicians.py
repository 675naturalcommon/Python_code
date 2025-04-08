'''
magicians=['alice','david','carolina']
for magician in magicians:
    #print(magician)
    print(f'{magician.title()},that was a great trick!')
    print(f'I can\'t wait to see your next trick!{magician.title()}\n')
print('Thank you!Everyone,that was a great magic show!')
#在此看到,print没有在缩进,于是for循环不再执行
'''

#下面展示缩进错误会出现的问题
#magicians=['alice','david','carolina']
#for magician in magicians:
#print(magician)   #IndentationError: expected an indented block after 'for'
                   # statement on line 13

#未缩进时产生逻辑错误
magicians=['alice','david','carolina']
for magician in magicians:
    print(f'{magician.title()},that was a great trick!')
print(f'I can\'t wait to see your next trick!{magician.title()}\n')
#这句不会报错,因为Python发现for语句后面的第一个print缩进了,所以Python不会报错
#但是当for循环执行完毕后,magician对应的是carolina,所以print最后一句是
                       # I can't wait to see your next trick!Carolina