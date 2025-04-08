s='3.12+2' #s是字符串类型
print(s,type(s))
print(eval(s))#去掉s两边的引号,对s进行运算

#eval函数经常和input函数一起使用
age=eval(input('请输入你的年龄:'))
print(age,type(age))

input('请输入你的身高和年龄:')
height=eval(input('请输入你的身高:'))
print(height,type(height))

hello='北京欢迎你!'
print(hello,type(hello))
print(eval('hello'))
#print(eval(hello)) #SyntaxError: invalid syntax
#print(eval('北京欢迎你!')) #SyntaxError: invalid syntax