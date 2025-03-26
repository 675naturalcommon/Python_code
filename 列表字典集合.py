#列表
# 创建
my_list = [1, 2, 3]

# 添加元素
my_list.append(4)        # [1, 2, 3, 4]
my_list.insert(0, 0)     # [0, 1, 2, 3, 4]

# 删除元素
my_list.pop()            # 移除末尾元素 → 4
my_list.remove(2)        # 移除第一个匹配项 → [0, 1, 3]

#字典
# 创建
my_dict = {"name": "Alice", "age": 25}

# 添加/修改键值对
my_dict["city"] = "Paris"    # {"name": "Alice", "age": 25, "city": "Paris"}
my_dict["age"] = 26          # 更新值

# 删除键值对
del my_dict["city"]          # 移除 "city" 键
value = my_dict.pop("age")   # 移除 "age" 键并返回值 26

#集合
# 创建
my_set = {1, 2, 3}

# 添加元素
my_set.add(4)            # {1, 2, 3, 4}

# 删除元素
my_set.remove(3)         # 移除元素 3（若不存在报错）
my_set.discard(5)        # 安全移除（不存在也不报错）

# 集合运算
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2      # 并集 → {1, 2, 3, 4, 5}
intersection = set1 & set2  # 交集 → {3}