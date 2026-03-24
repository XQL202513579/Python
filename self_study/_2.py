a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

hjk={x: x**2 for x in (2, 4, 6,8)}
print(hjk)

x = b"hello"
if x[0] == ord("h"):
    print("The first element is 'h'")   #ord() 函数用于将字符转换为相应的整数值

#eval() 函数执行的代码具有潜在的安全风险。
#如果使用不受信任的字符串作为表达式，则可能导致代码注入漏洞，
#因此，应谨慎使用 eval() 函数，并确保仅执行可信任的字符串表达式。

#int(x [,base])带(决定x解析的进制的)参数base，x一定要是字符串
'''
int(x [,base])
将x转换为一个整数
float(x)
将x转换到一个浮点数
complex(real [,imag])
创建一个复数
str(x)
将对象 x 转换为字符串
repr(x)
将对象 x 转换为表达式字符串
eval(str)
用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)
将序列 s 转换为一个元组
list(s)
将序列 s 转换为一个列表
set(s)
转换为可变集合
dict(d)
创建一个字典。d 必须是一个 (key, value)元组序列。
frozenset(s)
转换为不可变集合
chr(x)
将一个整数转换为一个字符
ord(x)
将一个字符转换为它的整数值
hex(x)
将一个整数转换为一个十六进制字符串
oct(x)
将一个整数转换为一个八进制字符串
'''

'''
>>>a = [1, 2, 3]
>>> b = a
>>> b is a 
True
>>> b == a
True
>>> b = a[:]
>>> b is a
False
>>> b == a
True
'''
#海象运算符优先级最低（比lambda还低），所以一定要配合()使用
'''
not>and>or
'''