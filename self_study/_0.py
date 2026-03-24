x = 10          # 整数
y = 3.14         # 浮点数
name = "Alice"   # 字符串
is_active = True # 布尔值
a, b, c = 1, 2, "three""123456"
print(type(b))
b="123"
print(type(b))
print(c)
print(type(x),end="")
print(type(y))
print(type(name))
print(type(is_active))
print(name[2:5:2])
print(name[2:])
jj = "koko\nokok"
print(jj.replace('\n', '\\n'))
print(jj)
print(repr(jj))
print(repr(jj).strip("'"))
ff='''yui
furyu\n
anti\\
ange\
l \
beat'''
print(ff)
t=['a','b','c','d','e']
print(t[-2:-1])
print(t[:4])
#与Python字符串不一样的是，列表中的元素是可以改变的
print(t[4::-1])
'''
常见运算符优先级（从高到低）：
() 括号
** 幂运算
+x, -x 一元运算符
*, /, //, % 乘法除法
+, - 加法减法
<<, >> 移位
& 按位与
^ 按位异或
| 按位或
==, !=, >, <, >=, <= 比较运算符
not 逻辑非
and 逻辑与
or 逻辑或
:= 海象运算符（最低）
'''

import time
for i in range(1,101):
    print('\r[','='*int(i/2),' '*(50-int(i/2)),\
          ']',i,'%',end='',sep='',flush=True)
    time.sleep(0.05)