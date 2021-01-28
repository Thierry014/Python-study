# python自带的标准库
# https://docs.python.org/3/py-modindex.html

import random

for i in range(3):
    print(random.random()) 
    # 0-1的随机数

    print(random.randint(10,20))
    # 范围内的随机数



members = ['John','Henry','Lee','Dickson']

leader = random.choice(members)
# 随机选择list中的item
print(leader)


