class MyClass:
    @staticmethod
    def static_method():  #没有默认的第一个参数（如 self 或 cls）
        print("This is a static method.")
# 通过类调用
MyClass.static_method()   # 输出: This is a static method.
# 通过实例调用
obj = MyClass()
obj.static_method()       # 输出: This is a static method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2025 - birth_year
        return cls(name, age)   # 用当前类创建实例
p = Person.from_birth_year("Alice", 1990)  # 调用类方法创建对象
print(p.age)   # 35 (假设当前年份2025)

class MyClass:
    def __init__(self):
        self._name = None
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @name.deleter
    def name(self):
        print("Deleting name")
        del self._name
obj = MyClass()
obj.name = "Bob"
print(obj.name)   # Bob
del obj.name      # 输出 Deleting name

import sys
class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('创建实例')
    @staticmethod
    def static_method():
        print("This is a static method.")
    @classmethod
    def from_birth_year(self, name, birth_year):
        age = 2025 - birth_year
        yield 
        return self(name, age)
A.static_method()
a=A('hjk',1980)
a.static_method()
b=A.from_birth_year('lll',2000)
#得到一个生成器对象，此时函数体尚未执行。
next(b)
#驱动生成器执行到 yield 处，暂停并返回 None
try:
    next(b)
    #执行 return cls(name, age)。此时生成器结束，
    #抛出 StopIteration 异常，并将 cls(name, age) 作为异常的值
except StopIteration as e:
    b = e.value     # 从异常中获取 return 的值
    print(b,b.name,b.age)

from collections import deque
queue = deque()
#双向队列
queue.append('a')
queue.append('b')
queue.append('c')
print("队列状态:", queue)
# 输出: 队列状态: deque(['a', 'b', 'c'])
# 从队首移除元素
first_element = queue.popleft()
print("移除的元素:", first_element)
# 输出: 移除的元素: a
queue.appendleft('p')
print("队列状态:", queue)

matrix = [
[1, 2, 3, 4 ],
[5, 6, 7, 8 ],
[9 ,10,11,12],
]
rematrix=[[row[i] for row in matrix] for i in range(4)]
print(rematrix)