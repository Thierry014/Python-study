# list = array

name = ['lee','dickson','henry','tracy']

print(name[2:])
# [henry,tracy]

# 修改
name[0] = 'Lee'
# print(name)


# find largest
num = [3,6,7,668,22,33,158,66,21]
max_num = num[0]

for x in num:
    if x > max_num:
        max_num = x
print(max_num)


# 2D list
matrix = [
    [1,2,3],
    [5,7,9],
    [6,0,6]
]

print(matrix[1][1]) 

# 遍历element

for row in matrix:
    for item in row:
        print(item)

# list method
num = [3,6,7,668,22,33,158,66,21]

# num.clear()
# # 清空

# num.pop(index)
# # 如果不加参数则删除最后一个

# num.append(item)
# # 尾部添加

# num.insert(index,item)
# # 指定位置添加

# 寻找指定item
# num.index(item)
# # 返回位置

# item in num
# # 返回 bool值

# num.count(item)
# 返回找到的个数

# num.sort()
# num.reverse()
# # 根据数字大小重新正序倒序排列

# num2 = num.copy()

arr = [1,3,4,5,6,7,2,3,4,51,2,1,3,45,9]

# 返回一个新的数组
arr_new = []

for item in arr:
    if item not in arr_new:
        arr_new.append(item)
print(arr_new)


# 修改整个数组
# for item in arr:
#     if arr.count(item) >1 :
#         # find item index
#         index = arr.index(item)

#         # remove item based on index
#         arr.pop(index)

#         # delete directly
#         # arr.remove(item)

# print(arr)