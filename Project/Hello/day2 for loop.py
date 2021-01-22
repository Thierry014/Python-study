# for loop 

# for i in '123456':
#     print(i)


# for x in ['a','b','c']:
#     print(x)

# 0-4
# for z in range(5):
#     print(z)

# 含头不含尾 // 1-9
# for y in range(5,10):
#     print(y)

# 第三个变量为等差数 //1,4,7
# for a in range(1,10,3):
#     print(a)


# cart sum
# cart = [10,20,30]
# total = 0

# for price in cart:
#     total = total + price
# print(total)


# nest loop 循环嵌套
star = [5,2,5,2,2]

for x in star:
    # x = 5,2,5,2,2
    # 循环5次
    output = ''
    for y in range(x):
        # y = 循环次数, 每循环一次 +星星
        output+='*'
    print(output)



 