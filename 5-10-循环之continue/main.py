# 一：循环控制之 continue
# 1、理解思路
# continue运行后，当前循环结束，进入下一次循环
# 2、可使用对象
# for循环、while循环
# 3、补充说明
# continue会结束本次循环，本次循环后续代码结束执行


# 输出
# 1
# 2
# 3
# 4
# 5
# for end
for i in range(1,6):
    print(i)
    if i==4:
        continue
else:
    print('for end')



# 输出
# 1
# 2
# 3
# 5
# for end
for i in range(1, 6):
    if i == 4:
        continue
    print(i)
else:
    print('for end')



b=1
# 输出
# 1
# 2
# 3
while True:
    print(b)
    if b==3:
        break
    else:
        pass
    b=b+1
else:
    pass




# 二：循环控制之 continue 补充说明
# 1、break是强行中断循环，continue是提前结束本次循环
# 2、break会导致循环的else不工作，continue不会
# 3、pass 特殊字符，用于控制代码缩进的空白关键词


