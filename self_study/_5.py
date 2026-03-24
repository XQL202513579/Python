a=1.123456
b=-123.12
print('% f\n% f'%(a,b))

print("%#o %#x %#X" % (10, 10, 10))

my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0}, 地址 {1}".format(*my_list))

site = {'name': "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{0[name]}, 地址 {0[url]}".format(site))
#format用法键名可以不加引号，f用法键名包含特殊字符（如空格、点号）或与
#Python 关键字冲突，此时必须加引号，例如 f'{site['my-key']}'。
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print(f"网站名：{site['name']}, 地址 {site['url']}")

data = {'name': 'Alice', 'age': 20}
print("%(name)s今年%(age)d岁"%data)

text = "123ABC"
print(text.capitalize())

text = "1 hello World"
print(text.capitalize())

text = " hello world"
print(text.capitalize())

text = "Hello"
print(text.center(15, '*'))

text = "aaaaa"
print(text.count("aa"))

text = "abcaabbcc"
print(text.count("a", 2, 7))

b = b'Hello World'
print(b,b.decode(),b'\xc4\xe3\xba\xc3'.decode('gbk'),\
      b'\xc4\xe3\xba\xc3'.decode('GbK'),sep='|||')

b = b'Hello\x80World'
try:
  print(b.decode('utf-8'))
except UnicodeDecodeError as k:
      print(f"解码错误:{k}")
      print(b.decode('utf-8','ignore'))

x = 1
print(f'{x+1=}')

str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
print(str_utf8,str_utf8.decode('UTF-8','strict'),\
      str_utf8.decode('gBk','strict'))
print(str_gbk.decode('UTF-8','strict'))

# 示例1: 默认移除空白
text = "   Hello World"
print(text.lstrip())

# 示例2: 使用第三个参数指定要删除的字符
table = str.maketrans("abc", "123", "xyz")
text = "a x b y c z"
print(text.translate(table))

# 示例2: 指定替换次数
text = "aa aa aa"
print(text.replace("aa", "bb", 2))

table = str.maketrans("", "", "aeiou")
text = "Hello World"
print(text.translate(table))  # 输出: 'Hll Wrld'

print("\t\n ".isspace())  # 输出: True
print("一二三".isnumeric())  # 输出: True

#split(str="", num=string.count(str))
#splitlines([keepends])
text = "line1\nline2\n"
print(text.splitlines(True))
# 输出: ['line1\n', 'line2\n']

#startswith(substr, beg=0, end=len(string))
#endswith(suffix, beg=0, end=len(string))
#expandtabs(tabsize=8)

#zfill(width)
num = "-42"
print(num.zfill(5))  # 输出: '-0042' (负号保留在开头)

# 示例3: 全角数字
print("１２３".isdecimal())
# 输出: True (全角数字也是十进制字符)
print("½".isdecimal())
# 输出: False (½不是十进制字符)