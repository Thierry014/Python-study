# Number
from os import O_NDELAY, strerror


round(number, digits)


# condition
print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")
return A if 判断条件 else B


# 三选 (逻辑运算)
三都要
return A and B and C

三都不要
return not (A or B or C)

三选要A不要B,要B不要A
return (A or B) and not (A and B)

三选一
return(A+B+C == 1)


#List
num = ['a','b','c']
num[:2] => a,b => 含头不含尾
num[1] => b,c 
# 总结 数字都是含头不含尾的 只有:是带尾巴的

对应通用方法常用
len(num) => 数组长度 => 有多少元素就是多少
sorted(num) => 更具文字或者数字排列
sum(num) => 求和  max()=> 找大

list专用函数
num.append(122) => 尾巴添加 [a,b,c,122]
num.pop() => 删最后一个
num.index('a') => 0 找位置
'a' in num => True  是否包含

# List表达式
d = [1, 2, 3][1:]  =>  [2,3]


# List 结合 Loop 生成一个新的list
item = ['bar','tv','coffee','bed','coke']
big_item = [item for item in items if len(item)>3]  => ['coffee',"coke"]
 


# String
str1 = '"Pluto is a planet!"
str1.split() => ['Pluto', 'is', 'a', 'planet!']
a,b,c,d = str1.split()
join_test = '/'.join([a, b, c,d]) =>  join_test: Pluto/is/a/planet!
# 切割字符串,去掉参数
str.strip('arg') 
str.rstrip('arg') 

# 查看是不是数字组成的str
str.isnumeric() => True/False
str.isdigit() => True/False


#Dict
numbers = {'one':1, 'two':2, 'three':3}
# 添加/修改元素
numbers['eleven'] = 11 
# 是否包含键值
'key' in dict_name => return bool
# 遍历
for k in numbers: => k = key name (One,two,three)
for k,v in numbers => k = key name / v = 对应value
 
# print
for planet in planets:
    print(planet, end=' ') #print all on same line 用空格隔开每一个
