# 一:有序的for循环
# 1 基础语法
# for 变量 in 可迭代对象
# 2 补充语法
# for 变量 in 可迭代对象.....else......
# 3 enumerate
# 在循环中同时获取元素索引和值

a=['a','b','c','d','e','f']

# a
# b
# c
# d
# e
# f
for i in a:
    print(i)

print('-'*20)

# else 是在循环结束之后就会执行
# a
# b
# c
# d
# e
# f
# end~
for i in a:
    print(i)
else:
    print('end~')

print('*'*20)

# 3 enumerate 在循环中同时获取元素索引和值
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e
# 5 f
# end!
for index,item in enumerate(a):
    print(index,item)
else:
    print('end!')


print('!'*20)

# 3 enumerate 在循环中同时获取元素索引和值
# 元组
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')
# (5, 'f')
# end!
for i in enumerate(a):
    print(i)
else:
    print('end!')




# 二:有序的for循环的补充说明
# 1 for后面加上else语句,当循环正常结束时执行else
# 2 使用break和continue语句,来控制循环的执行
# 3 可迭代对象
# 字符串 列表 字典 set集合 range()函数 等等






