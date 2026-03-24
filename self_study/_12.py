Exception

TypeError
NameError
ZeroDivisionError
StopIteration
RuntimeError
ValueError
AssertionError
KeyboardInterrupt

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num) 
    num = 123
    print(num)
fun1()
print(num)

def istype(data):
    if isinstance(data,str):
        print(f"字符串: {data}")
    elif isinstance(data, int):
        print(f"整数: {data}")
    elif isinstance(data, list):
        print(f"列表: {data}")
istype(456)

try:
    a=1/0
except Exception as s:
    print(s)