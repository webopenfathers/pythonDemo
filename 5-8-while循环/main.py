# 一:谈条件的while循环
# 1 基础语法
# while 条件表达式
# 2 补充语法
# while 条件表达式 ....else.....
# 3 条件表达式
# 执行单次循环后,都需要判断一次

a=5

# 1 基础语法
# current a: 5
# current a: 4
# current a: 3
# current a: 2
# current a: 1
# end a: 0
while a:
    print('current a:',a)
    a=a-1

print('end a:',a)


a=5
# 2 补充语法
# end a: 0
# current a: 5
# current a: 7
# current a: 9
# while end
# end a: 11
while a<10:
    print('current a:',a)
    a=a+2
else:
    print('while end')

print('end a:',a)


# 二: 谈条件的while循环
# 1 for循环是迭代对象,while循环是条件判断
# 2 条件循环适用递归算法,例如实现阶乘,斐波那契数列等算法
# 3 可以使用break和continue语句来控制循环的执行

