# 外层循环
# 使用for循环,循环1至9
# 内层循环
# 循环内套循环,用于控制每层的范围
# 代码优化
# 将两层循环优化成一行 列表生成式 代码

# format() 函数是 Python 2.6 版本引入的一种强大的字符串格式化方法
# print('Hello, {0}. I am {1}.'.format('Alice', 'Bob'))
# 输出: Hello, Alice. I am Bob.
# print('The {animal} is {0} years old.'.format(5, animal='dog'))
# 输出: The dog is 5 years old.

# 双层for循环方法
loop=9
# 输出
# 1*1=1
# 1*2=2 2*2=4
# 1*3=3 2*3=6 3*3=9
# 1*4=4 2*4=8 3*4=12 4*4=16
# 1*5=5 2*5=10 3*5=15 4*5=20 5*5=25
# 1*6=6 2*6=12 3*6=18 4*6=24 5*6=30 6*6=36
# 1*7=7 2*7=14 3*7=21 4*7=28 5*7=35 6*7=42 7*7=49
# 1*8=8 2*8=16 3*8=24 4*8=32 5*8=40 6*8=48 7*8=56 8*8=64
# 1*9=9 2*9=18 3*9=27 4*9=36 5*9=45 6*9=54 7*9=63 8*9=72 9*9=81
for m in range(1,loop+1):
    for n in range(1,m+1):
        print('{}*{}={}'.format(n,m,n*m),end=' ')
    print(end='\n')



print('-'*30)



# 列表生成式方法
print(["{}*{}={}\n".format(n,m,n*m) if m==n else "{}*{}={} ".format(n,m,n*m) for m in range(1,loop+1) for n in range(1,m+1)])
print("".join(["{}*{}={}\n".format(n,m,n*m) if m==n else "{}*{}={} ".format(n,m,n*m) for m in range(1,loop+1) for n in range(1,m+1)]))

