for value in range(1,6):   #range有差一化,range(1,6),输出1,2,3,4,5,不会到6
    print(value)

value = list(range(1,6))
print(value)

value = range(6)   #返回数0,1,2,3,4,5
print(value)

numbers = list(range(2,11,2))
print(numbers)   #表示打印从2开始,每次加2,直至数超过11为止

#打印1-10的平方和
squares = []
for number in range(1,11):
    squares.append(number**2)
print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)

#首先指定一个描述性的列表名(squares),






