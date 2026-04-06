# 实战练习 Python实现随机生成姓名

import random

first_name='赵钱孙李周吴郑王'
last_name='伟松强丽林'

first = random.choice(first_name)
insert = random.choice(last_name)
last = random.choice(last_name)

final = first + insert + last


print(first)
print(last)
print(final)