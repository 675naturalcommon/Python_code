favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',}

#values()方法只获得字典中的值 ,并不考虑字典中的值是否重复,为剔除重复项,可使用集合set()
for language in favorite_languages.values():
    print(language.title())

print('\n')

for language in set(favorite_languages.values()):
    print(language.title())

#通过将包含重复元素的列表传入set,可让python在列表中找出独一无二的元素,并使用这些元素来创建一个集合