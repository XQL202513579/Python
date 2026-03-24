print([1, 2, 3] < [9, 2])#True

list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list2 = list1.copy()
print ("list2 列表: ", list2)
print(list1 == list2)

def takeSecond(elem):
    return elem[1]
vowels = ['er', 'ag', 'as', 'on', 'is']
vowels.sort(reverse=True,key=takeSecond,)
print ( '降序输出:', vowels )

class AssignValue(object):
    def __init__(self,value,哈子):
        self.value = value
        self.哈子=哈子
my_value = AssignValue(6,9)
print(my_value.哈子)
'''
1	list.append(obj)
在列表末尾添加新的对象
2	list.count(obj)
统计某个元素在列表中出现的次数
3	list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)
从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)
将对象插入列表
6	list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)
移除列表中某个值的第一个匹配项
8	list.reverse()
反向列表中元素
9	list.sort( key=None, reverse=False)
对原列表进行排序
10	list.clear()
清空列表
11	list.copy()
复制列表
'''

tup = ('r', 'u', 'n', 'o', 'o', 'b')
print(id(tup))
tup = (1,2,3)
print(id(tup))
b=('r', 'u', 'n', 'o', 'o', 'b')
print(id(b))
print(id(('r', 'u', 'n', 'o', 'o', 'b')))
print(id((1,2,3,4)))

seq = ('name', 'age', 'sex')
tinydict = dict.fromkeys(seq,10)
print ("新的字典为 : %s" %  str(tinydict))

'''
items()
keys()
values()
dict.copy()
dict.clear()
dict.update(dict2)
dict.fromkeys(seq[, value])
dict.get(key, default=None)
dict.setdefault(key, default=None)
dict.pop(key[,default=KeyError])
dict.popitem([default=KeyError])
'''