# 逻辑运算符and
# 1、基础语法：a and b
# 2、判断条件：两个都真则真，有假则假
# 3、多个and可以同时使用

a=True and True
print(a) # True

b=True and False
print(b) # False

c=False and False
print(c) # False

d=1 and 2
print(d) # 2

e=2 and 3
print(e) # 3

f=1 and 3
print(f) # 3

g=3 and 1
print(g) # 1

h=1 and 0
print(h) # 0

i=0 and 1
print(i) # 0

j=2 and 3 and 5 and 0 and 7 and 9
print(j) # 0

k=2 and 3 and 5 and 6 and 7 and 9
print(k) # 9