#使用pop()方法删除元素

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

poped_motorcycles= motorcycles.pop()
print(motorcycles)
print(poped_motorcycles)

motorcycles=['honda', 'yamaha', 'suzuki']
last_motorcycles=motorcycles.pop()
last_owned=f'The last bicycle I own was {last_motorcycles.title()}.'
print(last_owned)

first_owned = f'The first bicycle I owned was {motorcycles.pop(0).title()}!'
print(first_owned)

#每当使用pop()时,被弹出的元素就不在列表中了
print(motorcycles)

#如果要在列表中删除一个元素,且不在以任何方式使用他,就用del
#如果要继续使用,就用pop()

