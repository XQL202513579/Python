from time import sleep
for _ in range(10):
    print('\r/',end='',flush=True)
    sleep(0.1)
    print('\r|',end='',flush=True)
    sleep(0.1)
    print('\r\\',end='',flush=True)
    sleep(0.1)
    print('\r—',end='',flush=True)
    sleep(0.1)

import threading
counter = 0
lock = threading.Lock()
# 创建一个锁
def increment():
    global counter
    for _ in range(100000):
        with lock:
            # 加锁保护临界区
            counter += 1
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
t1.start()
t2.start()
t1.join()
t2.join()
print(counter)
# 一定会输出 200000

import time
class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        print(self.start)
        return self  #返回对象本身，以便在with块内访问
    def __exit__(self, exc_type, exc_val, exc_tb):#traceback
        self.end = time.perf_counter()
        print(self.end)
        print(f"耗时: {self.end - self.start:.9f} 秒")
        return False  #不抑制异常
#使用示例
with Timer() as t:
    print(sum(range(10**6)))

import datetime
class TimestampFile:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename, 'a', encoding='utf-8')
        self.file.write(f"\n--- 开始: {datetime.datetime.now()} ---\n")
        return self.file         #即后面访问的f
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.write(f"--- 结束: {datetime.datetime.now()} ---\n")
        self.file.close()
        return False
# 使用示例
with TimestampFile('log.txt') as f:
    f.write("这是日志内容\n")

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    def __iter__(self):
        return self  # 返回自身作为迭代器
    def __next__(self):
        if self.current > self.end:
            raise StopIteration  # 迭代结束
        value = self.current
        self.current += 1
        return value
# 使用示例
for num in Counter(1, 5):
    print(num)  # 输出 1 2 3 4 5
a=Counter(8,16)
print(next(a))
print(next(a))
print(next(a))

from contextlib import contextmanager
@contextmanager
def tag(name):
    print(f"<{name}>")       # 1. 进入 with 块前执行
    try:
        yield
    finally:                 # 2. 暂停，进入 with 块内部
        print(f"</{name}>")  # 4. 退出 with 块后执行
# 使用示例
with tag("h1"):
    print("这是一个标题")     # 3. 执行 with 块内的代码