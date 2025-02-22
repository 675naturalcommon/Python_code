x=10
y=3
z=x/y   #将x/y的结果赋值给z
print(z,type(z))  #运算结果隐式转换

#float类型转换为int类型
print('float类型转换成int类型:',int(3.14))
print('float类型转换成int类型:',int(3.9))
print('float类型转换成int类型:',int(-3.14))
print('float类型转换成int类型:',int(-3.9))

#结论:float类型转换成int类型只保留整数部分,不会四舍五入

#int类型转换成float类型
print('将int类型转换成float类型:',float(10))
#将str转换成int类型
print(int('100')+int('200'))
#将字符串转成int或float时报错的情况
#print(int('10a'))  ValueError: invalid literal for int() with base 10: '10a'
print(int(10))

#chr()和ord()是一对
print(ord('单'))#单在Unicode对应的整数值
print(chr(21333))#21333整数在Unicode对应的字符串是什么


#进制之间的转换,10进制与其他进制之间的转换
print('十进制转换为十六进制:',hex(21333))
print('十进制转换为八进制:',oct(21333))
print('十进制转换为二进制:',bin(21333))