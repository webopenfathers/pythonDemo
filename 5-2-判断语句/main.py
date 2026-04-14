# 一：if判断语句
# 1、基础语法
# if a: xxxx
# 2、完整语法
# if...else...
# 3、拓展语法
# if...elif...else...

a=97
if a>90:
    print('成绩优秀')


if a<60:
    print('成绩不及格')
else:
    print('成绩及格')


if a<60:
    print('成绩不及格')
elif a<70:
    print('成绩刚过及格线')
elif a<80:
    print('成绩良好')
elif a<90:
    print('成绩优秀')
elif a<100:
    print('成绩拔尖')
else:
    print('满分')


# 二：常规判断标准
# 1、数值判断：大小、等于、不等于
# 2、内容判断：等于、存在
# 3、布尔类型：True False


# 1、数值判断：大小、等于、不等于
print(1>2) # False
print(2<5) # True
print('a'!='b') # True
print(4==4) # True

# 2、内容判断：等于、存在
b='abcdefg'
print('a' in b) # True
print('abc' in b) # True
print('abd' in b) # False


# 3、布尔类型：True False
print('if block') if True else print('else block') # if block
print('if block') if False else print('else block') # else block


# 三：if判断语法补充说明
# 1、if语法不难，但是注意判断条件，情况比较多
# 2、复杂判断条件一次判断难以描述，建议拆分后写多条判断
# 3、多条判断语句，注意可读性，不要嵌套超3层


