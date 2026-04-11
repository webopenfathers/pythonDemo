# 一：set集合常规操作
# 1、set的定义：
# a={'a'}; b=set()
from rope.base import prefs

# 2、set集合新增元素
# a.add('x')

# 3、set集合删除元素：
# a.remove('a')

# 1、set的定义：
a={'a'}


print(type(a)) # <class 'set'>
# 1、set的定义：
b=set()

# 2、set集合新增元素
b.add(1)
print(b) # {1}

# 2、set集合新增元素
b.add(2)
b.add(3)
print(b) # {1, 2, 3}

# 3、set集合删除元素：
b.remove(2)
print(b) # {1, 3}

b.remove(1)
print(b) # {3}

# 4、set集合没有顺序：
c=set()
c.add(3)
c.add(2)
print(c) # {2, 3}
c.add(1)
print(c) # {1, 2, 3}
c.add(4)
print(c) # {1, 2, 3, 4}

# 二：set集合进阶操作
# 1、set集合的拷贝操作
# a.copy()

# 2、set集合的清空操作
# a.clear()

d={1,2,3,4}
e=d  # 表示e和d的引用地址相同，d改变e也会改变
# 1、set集合的拷贝操作
f=d.copy() # copy表示 f的数据地址是新的地址和d的地址不同

print(d) # {1, 2, 3, 4}
print(e) # {1, 2, 3, 4}
print(f) # {1, 2, 3, 4}

d.add(5)
print(d) # {1, 2, 3, 4, 5}
print(e) # {1, 2, 3, 4, 5}
print(f) # {1, 2, 3, 4}

# 查看内存地址
print(id(d)) # 2506352060096
print(id(e)) # 2506352060096
print(id(f)) # 2506352061664


d.add(6)
print(d) # {1, 2, 3, 4, 5, 6}
print(e) # {1, 2, 3, 4, 5, 6}
print(f) # {1, 2, 3, 4}

d.remove(1)
print(d) # {2, 3, 4, 5, 6}
print(e) # {2, 3, 4, 5, 6}
print(f) # {1, 2, 3, 4}

f.remove(3)
print(d) # {2, 3, 4, 5, 6}
print(e) # {2, 3, 4, 5, 6}
print(f) # {1, 2, 4}

e.add(7)
print(d) # {2, 3, 4, 5, 6, 7}
print(e) # {2, 3, 4, 5, 6, 7}
print(f) # {1, 2, 4}

# 2、set集合的清空操作
d.clear()
print(d) # set()
print(e) # set()
print(f) # {1, 2, 4}


# 三：set集合补充操作说明
# 1、set集合内置的copy函数，是深度拷贝，重新开辟一个内存
# 2、set集合内置的clear函数，是清空，但是源内存地址没变
# 3、set集合虽然是可迭代对象，但是是无序的，不要使用循环【迭代】

