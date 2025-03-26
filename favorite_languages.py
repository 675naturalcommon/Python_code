#在alien中,字典存储的是一个对象的众多信息,字典也可以存储众多对象的同一种信息
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',}#在最后一个键值对后面也加上括号,为以后添加键值对做好准备
language = favorite_languages['sarah'].title()
print(f'Sarah\'s favorite language is {language}')

alien_0 = {'color':'green','speed':'slow'}
#在键值对不存在的情况下,应考虑使用get,get()方法的第一个参数用于指定键,是必不可少的
# 第二个键如果不存在,将返回None
point_value = alien_0.get('points','No point value assigned!')
print(point_value)

point_value = alien_0.get('points')
print(point_value)