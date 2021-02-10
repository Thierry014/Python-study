# 字符串拷贝,切割

course = 'My first python course'

# 切割 []
print(course[0:5]) 
# 含头不含尾

# 拷贝
print(course[:])

# 倒过来取
print(course[-1])

#template literal

first='thierry'
last='henry'
print(f'{first} {last} is my name')

# 字符串方法
# 计算长度
course = 'My first python course'

# 通用函数 function
len(course) 

# .方法 method =>操作自己
course.upper()
course.lower()
course.find('p')  
# 返回p的位置
print(course.replace('first', 'second')) 
# 不修改原字符串, 而是拷贝一个新的

print('course' in course)
# 检查是否包含 in 函数 返回bool值

course.title()
print(course)


# 切割字符串
spilt()