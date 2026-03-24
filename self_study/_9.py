def my_decorator(func):
    def wrap(*args,**attached):
        print("在原函数之前执行")
        func(*args,**attached)
        print("在原函数之后执行")
    return wrap
@my_decorator
def greet(name):
    print(f"Hello, {name}!")
#greet=my_decorator(greet)
greet("Alice")

def repeat(num_times):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                func(*args,**kwargs)
        return wrapper
    return decorator
@repeat(4)
def say_hello():
    print("Hello!")
#say_hello=repeat(4)(say_hello)
say_hello()

list1 = ['python', 'test1', 'test2']
list2 = [word.title() if word.startswith\
('p') else word.upper() for word in list1]
print(list2)

#super(子类，self).__init__(参数1，参数2，....)
#         父类名称.__init__(self,参数1，参数2，...)

class Vector:
   def __init__(self,a,b):
      self.a=a
      self.b=b
   def __str__(self):
      return 'Vector(%d,%d)'%(self.a,self.b)
   def __add__(self,other):
      return Vector(self.a+other.a,self.b+other.b)
v1=Vector(2,10)
v2=Vector(5,-2)
print(v1+v2)

def log_class(cls):
    #类装饰器，在调用方法前后打印日志
    class Wrapper:
        def __init__(self,c,d):
            self.wrapped = cls(c,d)
            # 实例化原始类
        def __getattr__(self, name):
            #拦截未定义的属性访问，转发给原始类
            return getattr(self.wrapped, name)
        def display(self):
            print(f"调用 {cls.__name__}.display() 前")
            self.wrapped.display()
            print(f"调用 {cls.__name__}.display() 后")
    return Wrapper  # 返回包装后的类
@log_class
class MyClass:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print("这是 MyClass 的 display 方法")
    def foo(self):
        print('123456789')
#MyClass=log_class(MyClass),log_class(MyClass)返回包装后的类Wrapper
obj = MyClass(123,'456')
obj.display()
obj.foo()
print(repr(obj.a),repr(obj.b))

class SingletonDecorator:
    #类装饰器，使目标类变成单例模式
    def __init__(self, cls):
        self.cls = cls
        self.instance = None
    def __call__(self):
        #拦截实例化过程，确保只创建一个实例
        if self.instance is None:
            self.instance = self.cls()
        return self.instance
@SingletonDecorator
class Database:
    def __init__(self):
        self.a=100
        print("Database 初始化")
#Database = SingletonDecorator(Database),
#SingletonDecorator(Database)返回的是实例
db1 = Database()
db2 = Database()
db3 = Database()
print(db1 is db2 and db1 is db3)
# True，说明是同一个实例