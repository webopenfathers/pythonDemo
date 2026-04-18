# 一：循环控制之break
# 1 理解思路
# break执行时,当前的循环直接结束
# 2 可结合对象:
# for循环 while循环
# 3 补充说明
# break执行, 则循环的else部分不会被执行

a=[1,2,3,4,5]
# 输出
# 1
# 2

# for循环的else部分不会被执行因为被break---即 print('for end') 不会被打印
for i in a:
    if i==3:
        break
    else:
        print(i)
else:
    print('for end')

print('-'*20)

b=5
# 输出
# 5
# 6
# 7

# while循环的else部分不会被执行因为被break---即 print('for end') 不会被打印
while b<10:
    print(b)
    b=b+1
    if b==8:
        break
else:
    print('while end')


# 二：循环控制之break的补充说明
# 1、break是强行中断循环，else的前提是循环正常执行结束
# 2、break只能退出当前循环，也就是break所在的这个循环