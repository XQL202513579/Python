a=1.123
a=complex(a)
print(a)
a=0
print(not a and not a)
a=(1+2j)*(5+9j)
print(a)
a=3.54689456199
print(round(a,8))
for i in range(0, 10, 2):
    print(i,end=" ")

import random
# 从列表中随机选一个
fruits = ['apple', 'banana', 'cherry', 'date']
print(random.choice(fruits))   # 可能输出: cherry
# 从字符串中随机选一个字符
print(random.choice('Python'))   # 可能输出: t
# 从range中随机选一个数
print(random.choice(range(10)))   # 可能输出: 7
# 从元组中随机选一个
colors = ('red', 'green', 'blue')
print(random.choice(colors))   # 可能输出: green

import random
# 0到9之间随机选一个（等价于choice(range(10))）
print(random.randrange(10))   # 可能输出: 3
# 5到15之间随机选一个
print(random.randrange(5, 16))   # 可能输出: 12
# 0到20之间，只选偶数
print(random.randrange(0, 21, 2))   # 可能输出: 14
# 10到0倒序（注意：stop必须大于start，step正数）
# random.randrange(10, 0, -1)   # 这样会报错！
# 正确实现倒序区间：先正序再映射，或者用choice(range(10,0,-1))
print(random.choice(range(10, 0, -1)))   # 可能输出: 5

import random
# 基本用法
print(random.random())      # 可能输出: 0.37444887175646646
# 生成0-10之间的随机浮点数
print(random.random() * 10)   # 可能输出: 5.823491204712354
# 生成5-15之间的随机浮点数
print(random.random() * 10 + 5)   # 可能输出: 12.361894573102987

import random
# 打乱列表
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
random.shuffle(cards)
print(cards)   # 可能输出: ['3', 'K', '7', 'A', '5', '9', '4', 'Q', '10', 'J', '6', '8', '2']
# 字符串不能直接shuffle，需要先转列表
word = 'hello'
word_list = list(word)
random.shuffle(word_list)
shuffled_word = ''.join(word_list)
print(shuffled_word)   # 可能输出: 'lelho'

import random
# 1到10之间的随机浮点数
print(random.uniform(1, 10))    # 可能输出: 7.832591684972316
# 参数顺序不重要，会自动调整
print(random.uniform(10, 1))    # 可能输出: 4.671324582103459
# 实际应用：模拟身高
height = round(random.uniform(150, 190), 1)
print(f'随机身高: {height}cm')   # 可能输出: 随机身高: 172.3cm