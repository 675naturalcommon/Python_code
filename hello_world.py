#不必要的缩进
#message = 'Hello Python World!'
#   print(message)   #IndentationError: unexpected indent

magicians=['alice','david','carolina']
for magician in magicians:
    print(f'{magician.title()},that was a great trick!')
    print(f'I can\'t wait to see your next trick!{magician.title()}\n')
    print('Thank you!Everyone,that was a great magic show!')
#最后一句print也是不必要的缩进,通常不会导致语法错误,但会导致逻辑错误