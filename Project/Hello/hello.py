# /*输出结果print 函数*/
print('Henry014')
print('#'*5)

# /用=号定义变量/
name ='John Smith'
age = 26
isNew = True

# 用input函数 用户输出
name = input("What's ur name? ")
color = input('favourite color? ')

print(name+' like '+color)

#数据转换的函数
int()
float()
bool()

#查看数据类型
type()


# 区别 function, method, magic-method
x = 'banana'
len(x) => function => 通用方法适合一切变量

x.lower() => method => 特定方法, 适用于本身(这里是字符串)

