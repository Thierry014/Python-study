tuples = (1,2,3)
# .index
# .count
# 用法类似 list

# tuple面的数据是不能修改,添加的



# unpacking 特性

x,y,z = tuples
# x = tuples[0] = 1 y=2,z =3 以此类推


# dictionary( key value pair => class)

dic = {
    "name":"John",
    "age":30,
    "is_male":True
}

# 访问 dic[name]

# print(dic["age"])
# print(dic.get("job","teacher"))

# 修改
dic["name"] = 'henry'
# print(dic)


phone =  input("Phone: ")
output = ''

num_dic = {
    '0':'zero',
    '1':'one',
    '2':'two',
    '3':'three'
 }

for i, x in enumerate(phone):
    # output+= num_dic[x]+' '
    # print(i) //loop times

    output += num_dic.get(x,"?")+" "

print(output)
print(type(phone))
