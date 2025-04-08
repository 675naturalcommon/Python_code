#有时候,不知道要删除的元素在列表中的那个位置,只知道要删除哪个的元素的值,可使用remove()
motorcycles = ['honda', 'yamaha','ducati','suzuki']
print(motorcycles)

motorcycles.remove('suzuki')
print(motorcycles)

too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)

print(f'\nA {too_expensive.title()} is too expensive for me!')

#remove() ⽅法只删除第⼀个指定的值。如果要删除的值可能在列表中出现多次，就需要使⽤循环，确保将每个值都删除
