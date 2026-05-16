# 随机数
# 内置的random库，random.randint()
# 循环
# 用于让程序不断的比较每次输入
# 输入函数
# input()函数等待用户输入字符串类型的数据

import random


def check_guess_number(guess, target):
    if guess == target:
        print('You guess it')
        return True
    elif guess > target:
        return False
    elif guess < target:
        return False
    return None


def main(loop_times):
    target_value = random.randint(10, 30)
    for _ in range(loop_times):
        guess = input('Please input your guess:')
        # 检测输入的是否是数字类型，不是int类型，则给出提示，跳过本次循环。
        if not guess.isdigit():
            print('please input a number')
            continue
        guess = int(guess)
        status=check_guess_number(guess, target_value)
        if status:
            print('You get it')
            return None
        else:
            print('Wrong guess')
    return None


if __name__ == '__main__':
    print('Game Start')
    loop_time = 3
    main(loop_time)
    print('Game Over')






