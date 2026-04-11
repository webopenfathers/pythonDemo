# 字典：成对数据组合而成的高级盒子

# 一：字典常规操作
# 1、字典的定义：
# a={'a': 1,'b': 2}; b=dict()

# 2、字典元素的赋值
# a['c']=3

# 3、字典的元素取值
# a['c'] 或 a.get('a')


# 1、字典的定义：
a={}
print(type(a)) # <class 'dict'>

b=dict()
print(type(b)) # <class 'dict'>

# 2、字典元素的赋值
a['a']=1
print(a) # {'a': 1}

a['b']=2
print(a) # {'a': 1, 'b': 2}

# 3、字典的元素取值
c=a['a']
print(c) # 1
d=a.get('b')
print(d) # 2

# 4、字典的删除操作
del a['a']
print(a) # {'b': 2}

# 5、字典的容错读取 get 方法
e=a.get('a',0) # 没找到返回第二个参数
print(e) # 0
f=a.get('b',0) # b可以找到，返回b值
print(f) # 2


# 二、字典的进阶操作
# 1、字典取出所有的键和值：a.keys() a.values()
# 2、字典取出所有的键值对：a.items()
# 3、字典导出json：json.dumps(a)

g={}
g['a']=1
g['b']=2
g['c']=3
g['d']=4
print(g) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 1、典取出所有的键
h=g.keys()
print(h) # dict_keys(['a', 'b', 'c', 'd'])

# 2、字典取出所有的值
i=g.values()
print(i) # dict_values([1, 2, 3, 4])

# 3、字典取出所有的键值对
j=g.items()
print(j) # dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# 4、字典导出json
import json
k=json.dumps(g)
print(k) # {"a": 1, "b": 2, "c": 3, "d": 4}


# 字典补充操作说明
# 1、少用a[],多用a.get(),容错率更好
# 2、给字典的键进行重复赋值，只保留最后一次的值
# 3、字典键值对中，键：字符串，值：字符串、数字、列表、元组等

