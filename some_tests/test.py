# 使用循环打印7次
"""
for i in range(7):
    print("Hello World")

# 使用循环打印7次
for i in range(7):
    print("Hello World")
"""

import time
from functools import lru_cache

# 不使用缓存的斐波那契函数
def fibonacci_no_cache(n):
    if n <2:
        return n
    return fibonacci_no_cache(n-1) + fibonacci_no_cache(n-2)

# 使用lru_cache的斐波那契函数
@lru_cache(maxsize=None) # 无限缓存大小
def fibonacci_with_cache(n):
    if n < 2:
        return n
    return fibonacci_with_cache(n-1) + fibonacci_with_cache(n-2)

# 性能比较
def compare_performance(n):
# 测量未缓存版本的时间
    start = time.time()
    result1 = fibonacci_no_cache(n)
    time1 = time.time() - start

# 测量缓存版本的时间
    start = time.time()
    result2 = fibonacci_with_cache(n)
    time2 = time.time() - start
    # 打印结果
    print(f"计算斐波那契数列第{n}项:")
    print(f"无缓存版本: {time1:.6f}秒")
    print(f"有缓存版本: {time2:.6f}秒")
    print(f"性能提升: {time1/time2:.2f}倍")

# 运行比较
compare_performance(35)

