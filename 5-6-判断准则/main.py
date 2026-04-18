# 一：真假的判断标准
# 1、特殊类型
# True为真，False为假，None为假
# 2、数值类型
# 0为假，非0都是真
# 3、结构类型
# 空内容为假，有内容为真

print(not 1) # False
print(not True) # False
print(not False) # True
print(not None) # True
print(not 1) # False
print(not 0) # True
print(not -1) # False
print(not -1.1) # False


# 3、结构类型
print(not '') # True
print(not '0') # False
print(not []) # True
print(not {}) # True
print(not set()) # True
print(not ()) # True
print(not [0]) # False



# 一：真假的判断标准的补充
# 通常判断，都是针对某某语句和布尔类型
# 条件个数：
# 一次一个，最多一行三个条件
# 写法推荐
# 逻辑运算符 > 代码快嵌套

