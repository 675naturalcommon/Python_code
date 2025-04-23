import random
import time
import os

# 初始化数字数组
num = [0] * 10

while True:
    output = []
    for i in range(10):
        if num[i] > 10:
            # 根据奇偶性选择文字
            text = "天天开心" if num[i] % 2 else "要永远幸福"
            output.append(text)
            num[i] -= 1
        else:
            output.append(" " * 8)  # 8个空格保持对齐
            # 数值递减并重置
            num[i] -= 1
            if num[i] < 0:
                num[i] = random.randint(0, 19)

    # 设置控制台颜色（黄色背景）
    os.system('color 6')
    # 打印输出并立即刷新
    print(''.join(output), end='', flush=True)
    # 保持50ms延迟（原Sleep(50)）
    time.sleep(0.05)

#新增退出条件,运行100次后退出
    max_cycles = 100 #可自定义运行次数

    if 'cycle_count' not in locals():
        cycle_count = 0
        cycle_count += 1
    if cycle_count >= max_cycles:
        os.system('color')
        print("程序已退出")
        break