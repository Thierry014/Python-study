# if else 

# score = input("enter your score ")
score = True

if score:
    print("Pass")
else: 
    print("Fail")

# 逻辑运算符 and, or, not
# 大小运算 >,<,<=,>=,==,!=  (=不能用应为在python中等号是用来赋值的)

temp = 50

if temp >= 30:
    print("hot")
else:
    print("not hot")


# name = input("enter ur name ")
# name_lenth = len(name)

# if name_lenth <= 3 :
#     print(f"your name length is {name_lenth} and it should be no shorter than 3 cha")
# elif name_lenth > 50:
#     print(f"your name's lenth is {name_lenth} too long")
# else:
#     print('looks good')


weight = input('ENTER UR Weight (L)bs or (K)g ')
x = input('kg or lbs ').lower()

if x == 'l':
    print(f'your weight is {float(weight) * 1.45} lbs ')
else:
    print(f'your weight is {weight}kg')