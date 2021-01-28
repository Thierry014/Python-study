# 大写开头定义 CamelCase
class Point:
    # x = 10

    # 用构造函数constructor来定义属性
    def __init__(self,x=1,y=10):
        self.x = x
        self.y = y


    def move(self):
        print('move')



# 实例化
pt1 = Point()
pt1.move()
# pt1.x = 30
print(pt1.x,pt1.y)


pt2 = Point()
print(pt2.x)


class Person:
    # constructor构造函数
    def __init__(self,name):
        self.name = name
    
    def talk(self,content):
        # self.content = content
        print(f'{content}, my name is {self.name}')


henry = Person('Henry')
henry.talk('hello buddy')

# 继承

class Robot(Person):
    # 继承talk

    def __init__(self,name):
        self.name = name


# 使用pass 来避免空类

jason = Robot('jason')
jason.talk('Hi')