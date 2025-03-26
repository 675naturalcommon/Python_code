user_0 = {
    'username':'enrico fermi',
    'first':'enrico',
    'last':'fermi'
}
#声明了两个变量key和value,声明的两个变量名可以是任意的,例如也可以把key和value换成k和v
for key,value in user_0.items():#方法items,这个方法返回一个键值对列表,
                                # 接下来for循环依次将每个键值对赋给两个变量名key和value
    print(f"\nKey:{key}")
    print(f"Value:{value}")
print('\n')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',}
for name,language in favorite_languages.items():
    print(f"{name.title()}\'s language is {language.title()}!")
    print(f"Name:{name}")
    print(f"Language:{language.title()}\n")
print('\n')

#在不需要使用字典中值时,用keys()方法很管用,keys()是用来遍历字典中的所有键的
for name in favorite_languages.keys():
#在遍历字典时,会默认遍历字典中的所有的键,所以上一行代码等价于 for name in favorite_languages:
    print(name.title())
print('\n')

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f'Hi,{name.title()}')
    print(favorite_languages[name])
    if name in friends:
        language = favorite_languages[name].title()
        #name是键,上述代码通过name这个键找值
        print(f'{name.title()},I see you love {language}')

print('\n')

if 'eric' not in favorite_languages.keys():
    print('Eric,please take our poll!')
#keys()方法并非只能用于遍历,事实上,它会返回一个列表,其中包含字典中的所有键


#按特定顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print(f'{name.title()},thank you for taking the poll!')





















