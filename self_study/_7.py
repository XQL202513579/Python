'''
add()	为集合添加元素
clear()	移除集合中的所有元素
copy()	拷贝一个集合
difference()	返回多个集合的差集
difference_update()	移除集合中的元素，该元素在指定的集合也存在。
discard()	删除集合中指定的元素
intersection()	返回集合的交集
intersection_update()	返回集合的交集。
isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	判断指定集合是否为该方法参数集合的子集。
issuperset()	判断该方法的参数集合是否为指定集合的子集
pop()	随机移除元素
remove()	移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	返回两个集合的并集
update()	给集合添加元素
len()	计算集合元素个数
'''

age = int(input("请输入你家狗狗的年龄: "))
print('\'\'\'')
input("点击 enter 键退出")

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401|403|404:
            return "Not allowed"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
print(http_error(int(input())))
input()

class Circle:
    def __init__(self, radius):
        self.radius = radius
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
def match_shape(shape):
    match shape:
        case Circle(radius=1):
            print("匹配到半径为1的圆")
        case Rectangle(width=1, height=2):
            print("匹配到宽度为1，高度为2的矩形")
        case _:
            print("匹配到其他形状")
match_shape(Circle(1))
match_shape(Rectangle(1,2))
match_shape("other")
'''
import sys
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
'''
a=[1,2,3]
b=[4,5,6,7,8]
c=list(map(lambda x,y:x+y,a,b))
print(c)
from functools import reduce
d=reduce(lambda x,y:x+y,b)
print(d)

with open('0-6.py', 'r',encoding='utf-8') as infile,\
    open('1.txt', 'w',encoding='utf-8') as outfile:
    content = infile.read()
    pass;pass;outfile.write(content.upper())

import decimal
with decimal.localcontext() as ctx:
    ctx.prec = 60
    # 将数字转为 Decimal（用字符串初始化，避免二进制浮点误差）
    a = decimal.Decimal('1234567891.23456789123456789123456789123456789')
    b = decimal.Decimal('9876543219.87654321987654321987654321987654321')
    # Decimal 运算，受精度限制
    print(a + b)
    print(a * decimal.Decimal('123456789'))
    print(round(a+b))
    print(f'{a*123456789:-^+99.42}')