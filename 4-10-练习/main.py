# 一行代码生成奇数列表或偶数字典
# 1、列表生成式
# [i for i in 可迭代对象 if 条件]
# 2、字典生成式
# {m:n for m,n in 可迭代对象 if 条件}


a=[n for n in range(1,21) if n%2]
print(a) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


b=[n for n in range(1,21) if not n%2]
print(b) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


c={str(n):n for n in range(1,21) if n%2==0}
print(c) # {'2': 2, '4': 4, '6': 6, '8': 8, '10': 10, '12': 12, '14': 14, '16': 16, '18': 18, '20': 20}
print(type(c)) # <class 'dict'>