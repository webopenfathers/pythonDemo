# 逻辑运算符not
# 1、基础语法：
# not a
# 2、判断条件
# 真假值互换
# 3、and or(最低) not(最高) 可以同时连接使用，但是注意执行顺序
# 4、优先级处理：
# 长语句推荐使用小括号包裹，控制执行优先级

a=not True
print(a) # False

b=not False
print(b) # True

c=not 0
print(c) # True

d=not 1
print(d) # False


e=True and False or False and not False
print(e) # False

f=True or False and False
print(f) # True

g=(True or False) and False
print(g) # False

h=True or False and False and not False
print(h) # True

i=True or (False and (False and not False))
print(i) # True

j=(True or False) and False and not False
print(j) # False


