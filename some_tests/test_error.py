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
alien_0['x_position'] = str(int(alien_0['x_position']) + x_increment) #需要将字符串转换为整数进行计算，然后再转回字符串

print(f'The new position is {alien_0['x_position']}')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',}
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f'Hi,{name.title()}')

    if name in friends:
        #此代码片段用于从字典中获取指定名字的最喜欢的语言，并将其首字母大写。
        language = favorite_languages[name].title()
        print(f'{name.title()},I see you love {language}')   #这里的title()方法用于将字符串的首字母大写
