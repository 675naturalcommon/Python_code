#使用coutinue语句来实现循环的条件判断

count = 0
while count < 5:
    print("The count is:", count)
    count += 1
    if count == 3:
        continue  # 跳过当前循环的剩余部分，直接开始下一次循环
    print("This is inside the loop")
print("The loop is over")
# 输出结果：
# The count is: 0
# This is inside the loop
# The count is: 1
# This is inside the loop
# The count is: 2
# This is inside the loop
# The count is: 4
# This is inside the loop
# The loop is over

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue  # 跳过当前循环的剩余部分，直接开始下一次循环
    print(current_number)
print("The loop is over")
# 输出结果：
# 1 3 5 7 9
# The loop is over      