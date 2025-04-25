def twoSum(nums, target):
    lens = len(nums)
    j=-1
    for i in range(lens):
        if (target - nums[i]) in nums:
            #if (nums.count(target - nums[i]) == 1)&(target - nums[i] == nums[i]):#如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
            if(nums.count[nums[i]==1]) and (2*nums[i]!=target):
                continue
            else:
                j = nums.index(target - nums[i],i+1) #index(x,i+1)是从num1后的序列后找num2
                break
    if j>0:
        return [i,j]
    else:
        return []

"""
作者：老腊肉越嚼越香
链接:https://leetcode.cn/problems/two-sum/solutions/21494/xiao-bai-pythonji-chong-jie-fa-by-lao-la-rou-yue-j/
来源:力扣(LeetCode)
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

def twoSum(nums, target):
    lens = len(nums)
    j=-1
    for i in range(1,lens): #左闭右开
        temp = nums[:i]   #左闭右开
        if (target - nums[i]) in temp:
            j = temp.index(target - nums[i])
            break
    if j>=0:
        return [j,i]


#字典模拟哈希表
def twoSum(nums, target):
    hashmap={}
    for ind,num in enumerate(nums):
        hashmap[num] = ind
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i!=j:
            return [i,j]
