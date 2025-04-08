username = ['eric', 'willie', 'admin', 'erin', 'ever']
for user in username:
    if user == 'eric':
        print(f'{user.title()}, would you like to see a status report?')
    else:
        print(f'{user.title()} thank you for logging in again')

print('\n')
"""
按照下面的说明编写一个程序，模拟网站如何确保每个用户的用户名都独一无二。 
创建一个至少包含5个用户名的列表，并将其命名为current_users。 
再创建一个包含5个用户名的列表，将其命名为new_users，并确保其中有一两个用户
名也在列表current_users中。 
遍历列表new_users，检查其中的每个用户名是否已被使用。如果是，就打印一条消息，
指出需要输入别的用户名；否则，打印一条消息，指出这个用户名未被使用。 
确保比较时不区分大小写。换句话说，如果用户名'John'已被使用，应拒绝用户名
'JOHN'。（为此，需要创建列表current_users的副本，其中包含当前所有用户名的全小写
版本。）
"""

current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

current_users_low = [user.lower()for user in current_users]  #列表解析
print(current_users_low)
for new_user in new_users:
    if new_user.lower() in current_users_low:
        print(f'Sorry,{new_user},that name is taken!')
    else:
        print(f'Great,{new_user} is still available!')

#循环生成列表current_users_low
print('\n')
current_users_low = []
for user in current_users:
    current_users_low.append(user.lower())

print(current_users_low)

print('\n')
"""
序数表示顺序位置，如1st和2nd。序数大多以th结尾，只有1st、2nd、3rd例外。 
在一个列表中存储数字1～9。 
遍历这个列表。 
在循环中使用一个if-elif-else结构，打印每个数字对应的序数。输出内容应为"1st 
2nd 3rd 4th 5th 6th 7th 8th 9th"，每个序数都独占一行。
"""

num = list[range(1,9)]
print(num)
print(list)

nums = list(range(1,9))
print(nums)
for num in nums:
    if num == 1:
        print('1st')
    elif num == 2:
        print('2nd')
    elif num == 3:
        print('3rd')
    else:
        print(f'{num}th')






