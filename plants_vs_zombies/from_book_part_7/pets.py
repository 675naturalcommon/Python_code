pets = ['cat', 'dog', 'fish']
print(pets)
pets.remove('fish')
print(pets)
#remove()方法用于删除列表中的元素，参数为要删除的元素值。
#如果元素不存在，则会引发ValueError异常。
#如果要删除的元素是列表中的最后一个元素，则该方法会自动将列表长度减一。

#当列表中有多个相同的值时，remove()方法只会删除第一个匹配的元素。
#如果要删除所有匹配的元素，可以使用循环来遍历列表并删除。
pets = ['cat', 'dog', 'fish', 'cat', 'dog', 'fish']
for pet in pets:
    if pet == 'fish':
        pets.remove(pet)
print(pets)

#如果要删除列表中的最后一个元素，可以使用pop()方法。
pets.pop()
print(pets)

#如果要删除列表中的指定位置的元素，可以使用pop()方法并传入索引值。
pets.pop(0)
print(pets)

print(1)
#如果要删除列表中的所有元素，可以使用clear()方法。
pets.clear()
print(pets)

#如果要删除列表中的所有元素，可以使用del语句。
del pets


#del语句和clear()方法的不同
#del语句会立即删除列表，而clear()方法只是清空列表，并不会立即删除。
#因此，如果要立即删除列表，可以使用del语句，否则可以使用clear()方法。
#del list[0]会删除列表中的第一个元素，而list.pop(0)则不会。
#del dict[key]会删除字典中的键值对，而dict.pop(key)则不会。

#clear()方法和del语句的区别
#clear()方法和del语句都可以用来删除列表或字典中的元素，但它们的区别在于：
#1. clear()方法会立即删除列表或字典中的所有元素，而del语句只是删除引用，并不会立即删除。
#2. clear()方法不会返回任何值，而del语句会返回被删除的元素的值。
#3. clear()方法和del语句都可以删除列表或字典中的元素，但它们的用法稍有不同。
#4. clear()方法和del语句都可以删除列表或字典中的所有元素，但它们的效率不同。
#5. clear()方法和del语句都可以删除列表或字典，但它们的作用范围不同。

#还可以使用while循环来删除列表中的重复元素
pets = ['cat', 'dog', 'fish', 'cat', 'dog', 'fish']
i = 0
#对于列表中的每一个元素pets[i]，代码会检查该元素是否存在于当前元素之前的部分pets[:i]，或者是否存在于当前元素之后的部分pets[i+1:]
while i < len(pets):
    if pets[i] in pets[:i] or pets[i] in pets[i+1:]:
        pets.remove(pets[i])
    else:
        i += 1
print(pets)
print(len(pets))