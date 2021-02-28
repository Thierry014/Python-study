import functools

def titleToNum(s):
    return functools.reduce(lambda x,y: x*26+y, map(lambda x: ord(x)-ord('A')+1,s))


print(titleToNum('ABC'))

# 匿名函数, 累加器