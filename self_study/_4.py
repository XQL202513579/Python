import random
import time
SEED = time.time()
original_list = ['list', 'elements', 'go', 'here']
random.seed(SEED)
my_list = original_list[:]
random.shuffle(my_list)
print("RUN1: ", my_list)
time.sleep(1)
SEED = time.time()
random.seed(SEED)
my_list = original_list[:]
random.shuffle(my_list)
print("RUN2: ", my_list)

print(r'123456\n{SEED}',f'123456\n{SEED}','123456\n{SEED}',sep='||||||',end='')
from random import uniform
print(uniform(16.999,13.0001))

#\a响铃
#\b退格(Backspace)
#\(在行尾时)续行
#\000空
#\t横向制表符
#\v纵向制表符\f换页
#\r回车，将 \r 后面的内容移到字符串开头，并逐一替换开头部分的字符，
#直至将 \r 后面的内容完全替换完成。
#\yyy八进制数，y 代表 0~7 的字符，例如：\012 代表换行。打印ASCII码对应字符
#\xyy	十六进制数，以 \x 开头，y 代表的字符，例如：\x0a 代表换行
#\other	\+其它的字符没有用，输出\和后面的东西

'''
import math
a=math.atan2(1,-1)#第一个参数是y，第二个是x
print(a)#弧度值
'''

'''
import time
for i in range(101): # 添加进度条图形和百分比
    bar = '[' + '=' * (i // 2) + ' ' * (50 - i // 2) + ']'
    print(f"\r{bar} {i:3}%", end='')
    time.sleep(0.05)
'''

'''
import time
for i in range(5,21,2): # 添加进度条图形和百分比
    print(i,end='|')
'''

'''
a='123456789'
print(a[:-2:2])
z,x=0,1
if z:=1 and x:#解析为z:=(1 and x)
    print('YES')
from time import sleep
for i in range(10):
    print('\a',end='',flush=True)
    sleep(1)
'''