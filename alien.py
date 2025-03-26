alien_0 = {'color':'green','points':'5'}
#键和值之间用冒号分割,而键值对之间用逗号分割
print(alien_0['color'])
print(alien_0['points'])

#在python中,字典是一系列键值对,每个键都与一个值关联,可以用键来访问与之关联的值

#最简单的字典只有一个键值对
alien_0 = {'color':'green'}
print(alien_0)
print(alien_0['color'])

#字典中可包含任意数量的键值对
alien_0 = {'color':'green','points':'5'}
new_points = alien_0['points']
print(f'You just earned {new_points} points!')

#字典是一种动态名,可随时在其中添加键值对
alien_0['x_position'] = '0'
alien_0['y_position'] = '25'
print(alien_0)

#使用字典来存储用户提供的数据或者编写能自动生成大量键值对的代码,通常需要定义一个空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#修改字典中的值
alien_0 = {'color':'green'}
print(f'The alien\'s color is {alien_0['color']}')
alien_0['color'] = 'yellow'
print(f'The alien\'s color now is {alien_0['color']}')
print('\n')

alien_0 = {'x_position':'0','y_position':'25','speed':'medium'}
print(f'Original position:{alien_0['x_position']}')

#向右移动外星人,根据当前速度确定将外星人移动多远

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
    #这个外星人的移动速度肯定很快

#新位置为旧位置加上移动距离
alien_0['x_position'] = str(int(alien_0['x_position']) + x_increment)
#将字典 alien_0 中的 'x_position' 从字符串转换为整数进行计算，
# 然后再转换回字符串以便存储和输出。这是因为字典中 'x_position' 和 'y_position'
# 初始被定义为字符串，而我们需要进行数值计算。
print(f'The new position is {alien_0['x_position']}')

print('\n')
#删除时,必须指定字典名和要删除的键
alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)
#注意,删除的键值对永远消失了
