# 一、列表：最简单易用的数据盒子
# 列表的常规操作
# 1、列表的定义：
# a=[]; 初始化速度更快
# b=list() 慢一点点
# 2、列表的追加 append 拼接 +
# 3、列表的 取值[index] 和 拓展extend


a=[]
b=list()
c=[1,2,3]

# 列表的追加 append
c.append('a')
print(c) # [1, 2, 3, 'a']

a.append(4)
a.append(5)
a.append(6)
print(a) # [4, 5, 6]

b.append(7)
b.append(8)
b.append(9)
print(b) # [7, 8, 9]


# 列表的追加 拼接 +

m=a+b
print(m) # [4, 5, 6, 7, 8, 9]

# 列表的 取值[index]
print(c[0]) # 1
print(c[1]) # 2
print(c[2]) # 3
print(c[3]) # a
# print(c[4]) # 报错 list index out of range
print(c[-1]) # a 最后一个值


# 拓展extend
# m的值全部拿出来放到c中
c.extend(m)
print(c) # [1, 2, 3, 'a', 4, 5, 6, 7, 8, 9]

# 把b作为一个元素追加进去
a.append(b)
print(a) # [4, 5, 6, [7, 8, 9]]

print(c[-1]) # 9
print(b[-1]) # 9
print(a[-1]) # [7, 8, 9]

# 二、列表的进阶操作
# 1、全数字列表的求和、最大值、最小值
# 2、列表的元素删除操作 remove
# 3、列表的元素弹出操作pop 也叫做出栈

o=[1,2,3,4,5,6]
p=[223,456,134,95,389]
q=max(p)
r=min(p)
# 最大值
print(q) # 456
# 最小值
print(r) # 95
s=sum(o)
# 求和
print(s) # 21

# 列表的元素删除操作 remove
o.remove(2)
print(o) # [1, 3, 4, 5, 6]
o.remove(6)
print(o) # [1, 3, 4, 5]

t=[1,2,3,1,2,3]
# 从前到后匹配要删除的，匹配到了直接删除
t.remove(1)
print(t) # [2, 3, 1, 2, 3]


# 元素弹出操作pop
u=[1,2,3,4,5,6]
v=u.pop()
print(v) # 6
print(u) # [1, 2, 3, 4, 5]
v=u.pop()
print(v) # 5
print(u) # [1, 2, 3, 4]


# 三、列表危险操作说明
# 1、列表里面的元素，不要嵌套列表本身
# 2、列表的元素内容及长度不限制，但是不建议使用太大且过多的元素
# 3、列表虽然不限制类型，推荐使用同一类型的数据对象做元素


