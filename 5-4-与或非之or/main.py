# 逻辑运算符 or
# 1、基础语法
# a or b
# 2、判断条件
# 有真则真，无真则假
# 3、多个and以及or可以同时使用

a=1 or 2
print(a) # 1

b=1 or 3
print(b)  # 1

c=2 or 1
print(c) # 2

d=0 or 1
print(d) # 1

e=True or False
print(e) # True

f=True or True
print(f) # True

g=False or False
print(g) # False


h=True and True or False
print(h) # True

i=True or False and True
print(i) # True

j=False or True and False
print(j) # False

k=False or False and True
print(k) # False

