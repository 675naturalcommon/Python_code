print(eval(input('请输入数字:')))

alien_0 = {'color':'green'}
print(f'The alien\'s color is {alien_0['color']}')
alien_0['color'] = 'yellow'
print(f'The alien\'s color now is {alien_0['color']}')
try:
    number = float(input('请输入数字:'))
    print(number)
except ValueError:
    print('输入无效，请输入一个数字。')

alien_0 = {'color': 'green'}
print(f"The alien's color is {alien_0['color']}")
alien_0['color'] = 'yellow'
print(f"The alien's color now is {alien_0['color']}")



