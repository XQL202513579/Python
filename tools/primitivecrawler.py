from urllib import request
from bs4 import BeautifulSoup
# 需要先装：pip install beautifulsoup4
response = request.urlopen("https://skr.skr1.cc:666/")
page_content = response.read().decode('utf-8')
# 格式化HTML源码
soup = BeautifulSoup(page_content, 'html.parser')
formatted_content = soup.prettify()
# 写入文件
with open("project.txt", 'w', encoding='utf-8') as fi:
    fi.write(formatted_content)
print(formatted_content)


from urllib import request
# 1. 打开网站并读取内容
response = request.urlopen("http://www.baidu.com/")
# 2. 把字节串解码为正常字符串（指定编码，解决乱码+恢复换行）
page_content = response.read().decode('utf-8')
# 3. 写入文件（用with自动关闭文件，更规范）
with open("project.txt", 'w', encoding='utf-8') as fi:
    fi.write(page_content)  # 直接写入解码后的字符串，保留换行
# 4. 打印内容（可选，验证效果）
print(page_content)


from urllib import request
response = request.urlopen("http://www.baidu.com/")  # 打开网站
fi = open("project.txt", 'w')                        # open一个txt文件
page = fi.write(str(response.read()))                # 网站代码写入
fi.close()                                           # 关闭txt文件