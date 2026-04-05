# 字符串的基础转换操作
# 字符串的 索引逆序 和 替换replace操作
# 字符串 分割 split 和 大小写转换 upper lower 操作
# 使用 内置函数 len 对字符串进行处理

a = '123456'
print(a)  # 123456

# 索引逆序
b=a[::-1]
print(b) # 654321

# 替换replace
c=a.replace('4','a')
print(c) # 123a56


# 分割 split
d = a.split('4')
print(d) # ['123', '56']


# 大小写转换 upper lower 操作
e='123abc456def'
f = e.upper()
print(e,f) # 123abc456def 123ABC456DEF

g=f.lower()
print(e,g) # 123abc456def 123abc456def

print(e==g) # True

print(f==e.upper()) #True



# 内置函数 len 获取字符串长度
print(len(a)) # 6
print(len(e)) # 12


# 字符串的字符 统计 count 和 内容填充 zfill(内容前面补位)
h='123456'
print(h.count('3')) # 1
print(h.count('5')) # 1

i=h*3
print(i) # 123456123456123456

print(i.count('3')) # 3
print(i.count('5')) # 3


j='3'
k='23'
l='9'
m='123'

print(j.zfill(3)) # 003
print(k.zfill(3)) # 023
print(l.zfill(3)) # 009
print(m.zfill(3)) # 123

# 字符串的 首部startswith 尾部内容检测判断 endswith
n='/users/zbw/Desktop/demo.app'
o='/users/zbw/Desktop/demo/demo.txt'

print(n.endswith('.app')) #True
print(o.endswith('.app')) #False
print(n.endswith('demo/demo.app')) # False
print(o.endswith('demo/demo.txt')) # True

p='abcdefg'
print(p.startswith('a')) # True
print(p.startswith('abc')) # True

# 字符串内容的 包含检测 in
q='abcdefg2288654440555544ujk'

print('b' in q) # True
print('m' in q) # False
print('abcf' in q) # False
print('abcf' not in q) # True
print('88' not in q) # False



