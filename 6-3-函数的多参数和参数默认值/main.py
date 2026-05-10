# 一：函数的多参数
# 函数可以无参数，也可以定义多个
# 定义结构：
# def func_name(param1,param2,...):
# 通过函数名调用函数，通过参数或者顺序传值


def more_param_function(param1,param2,param3):
    result=param1*1+param2*2+param3*3
    return result


func_result = more_param_function(1,2,3)
print(func_result) # 14


func_result = more_param_function(param1=1,param3=2,param2=3)
print(func_result) # 13

print('---'*20)
# 二：函数参数默认值
# 参数默认是：def func_name(param=1)
# 有值参数，可以传值也可以不传
# 有值参数定义时，要放在无默认值参数后面

def add_advance(first,second,flag=False):
    if flag:
        result = 0
        for n in range(first,second+1):
            result += n
    else:
        result=first+second
    return result

# 1+1=2
# 2+4=6
# 3+9=12
# 4+16=20
for i in range(1,5):
    temp_result = add_advance(i,i*i)
    print("{}+{}={}".format(i,i*i,temp_result))


# 小需求，将add_advance函数改成，有相加功能，也支持叠加功能
# 从1到2的叠加结果是：3
# 从3到6的叠加结果是：18
# 从5到10的叠加结果是：45
# 从7到14的叠加结果是：84
# 从9到18的叠加结果是：135
for i in range(1,10,2):
    temp_result = add_advance(i, i * 2,flag=True)
    print('从{}到{}的叠加结果是：{}'.format(i,i*2,temp_result))




# 三：函数参数的补充说明
# 有默认值的参数放在最后面
# 一个参数直接传值，多个参数请使用参数名传值
# 默认值参数通常都是不需要传值的
