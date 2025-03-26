request_toppings = ['mushrooms','green peppers','extra cheese']

for request_topping in request_toppings:
    if request_topping == 'green peppers':
        print('Sorry,we are out of green peppers right now!')
    else:
        print(f'Adding{request_topping}')

print('\nFinished making your pizza!')


#确定列表非空
request_toppings = []
if request_toppings:
    for request_topping in request_toppings:
        print(f'Adding {request_topping}')
    print('\nFinished your pizza!')
else:
    print('Are you sure you want a plain pizza!')


#对于数值0、空值None、单引号空字符串''、双引号空字符串""、空列表[]、空元组(),空字典{},Python都会返回False


#使用多个列表

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

request_toppings = ['olives','pineapple','extra cheese', 'french fries']
for request_topping in request_toppings:
    if request_topping in available_toppings:
        print(f'Adding {request_topping}')
    else:
        print(f'Sorry,we don\'t have {request_topping}')
print('Finished making your pizza!')