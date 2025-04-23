import time
import os

def main():
    arr1 = "堃堃,actually,I want to say you are sb!"
    arr2 = [' '] * len(arr1)  # 创建等长空白列表

    left = 0
    right = len(arr1) - 1

    while left <= right:
        # 更新左右字符
        arr2[left] = arr1[left]
        arr2[right] = arr1[right]

        # 清屏并打印
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(''.join(arr2))

        # 移动指针
        left += 1
        right -= 1

if __name__ == "__main__":
    main()
