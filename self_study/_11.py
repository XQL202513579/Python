knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k,v,sep=':')

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

n=list(set(basket))
n.sort()    #a=sorted(set(basket))
print(n)

a=100
if __name__ == '__main__':
   print('程序自身在运行')
else:
   print(f'我来自另一模块{__name__}')
'''
import _2
print(_2.a)
'''

'''
math	    数学运算（如平方根、三角函数等）
os	        操作系统相关功能（如文件、目录操作）
sys	        系统相关的参数和函数
random	    生成随机数
datetime    处理日期和时间
json	    处理 JSON 数据
re	        提供了正则表达式处理函数，可以用于文本搜索、替换、分割等。
collections	提供额外的数据结构（如 defaultdict、deque）
itertools	提供迭代器工具
functools	高阶函数工具（如 reduce、lru_cache）
urllib      提供了访问网页和处理URL的功能，包括下载文件、发送POST请求、处理cookies等。
'''

import pickle
# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
output = open('data.pkl', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(data1, output, -1)
# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)
output.close()

import pprint, pickle
#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)
data2 = pickle.load(pkl_file)
pprint.pprint(data2)
pkl_file.close()

#windows 系统下的换行代表2个字符大小

#truncate
#isatty
#fileno
#flush
#writelines

import os
os.system('dir /l /q /t:w')
#等于Linux中的ls -l
os.chdir('D:\VScode\Code\python')
print(os.getcwd())
home_directory = os.getenv("JAVA_HOME")
#PATH,HOME,USERPROFILE,JAVA_HOME
print("SERPROFILE目录:", home_directory)
a=os.listdir()
print(a)