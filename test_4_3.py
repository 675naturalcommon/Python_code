numbers = []
for number in range(1,21):
    numbers.append(number)
print(numbers)

numbers = [num for num in range(1,21)]
print(numbers)

#nums = [num for num in range(1,1000001)]
#print(nums)
#print(min(nums))
#print(max(nums))
#print(sum(nums))

nums = [num for num in range(1,20,2) ]
print(nums)

#创建一个能被3整除的列表
nums = [num for num in range(3,31,3)]
print(nums)

#创建一个列表,包含前10个整数的立方
nums = [num**3 for num in range(1,11)]
print(nums)

nums = []
for num in range(1,11):
    nums.append(num**3)
print(nums)




