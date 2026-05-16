# 随机数
# 内置的random库，random.randint()
# 循环
# 用于让程序不断的比较每次输入
# 输入函数
# input()函数等待用户输入字符串类型的数据

import random

target_value = random.randint(10, 30)

for _ in range(3):
    guess = input('Please input your guess:')
    # 检测输入的是否是数字类型，不是int类型，则给出提示，跳过本次循环。
    if not guess.isdigit():
        print('please input a number')
        continue
    guess = int(guess)
    if guess == target_value:
        print('You guess it')
        break
    elif guess > target_value:
        print('too high')
    elif guess < target_value:
        print('too low')
else:
    print('Game Over')




