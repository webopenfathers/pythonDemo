# 一：函数的定义
# 关键词：def
# 定义结构：def func_name(param);
# 通过函数名调用函数，通过参数名传参

def first_function():
    print('this is a first function')


# 函数的调用
first_function() # this is a first function

# 函数本身，没有被调用，通常用于传函数
print(first_function) # <function first_function at 0x000002071D02BB00>


# 二：函数的返回值
# 关键词：return
# 返回类型：任意类型
# 默认返回值: None

# 默认返回值: None
print(first_function()) # None


def second_function(a,b):
    c=a+b
    return c


def second_function1(a,b):
    c=a+b
    return a,b,c


# 关键词：return
# 2
# 6
# 12
# 20
for i in range(1,5):
    result = second_function(i,i*i)
    print(result)


# 关键词：return
# (1, 1, 2)
# (2, 4, 6)
# (3, 9, 12)
# (4, 16, 20)
for i in range(1, 5):
    result = second_function1(i, i * i)
    print(result)


# 三: 函数的特别说明
# 函数被调用时,开始执行代码,直到return运行
# 函数return会停止函数,所以只能返回一次,但可以一次多个值






