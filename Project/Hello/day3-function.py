def greet():
    print('Hello')
    print('Hi Siri')

greet()


# 带参数的函数

def say_hi(first,last):
    print(f'Hi {first} {last}')

# say_hi('Henry','Jiang')

say_hi(first = "henry", last = "jiang")

# 两种参数进入方式


# 函数的嵌套使用
# 例子1,关键词 key
def mod_5(x):
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)

# 例子2
def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    return fn(arg)

def squared_call(fn, arg):
    return fn(fn(arg))

call(mult_by_five, 1),
# mult_by_five(1) => 5*1 = 5

squared_call(mult_by_five, 1), 
# mult_by_five(mult_by_five(1)) => 5*(5*1) = 25

