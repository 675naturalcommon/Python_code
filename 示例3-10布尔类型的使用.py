x=True
print(x)
print(type(x))
print(x+10)
print(False+10)
print('------------')
print(bool(18)) #测试一下整数18的布尔值True
print(bool(0),bool(0.0))#False
#总结:非0数的bool值都为True
print(bool('北京欢迎你'))
print(bool(' '))
print(bool(''))
#总结:所有非空字符串的bool值都为True
print(bool(False))
print(bool(None))