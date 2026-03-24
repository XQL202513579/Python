#要是用heads加User-Agent基本够用了
#要是只有一行就用bs4
#BeautifulSoup 的解析和美化功能（prettify()）
#必须基于字符串（str） 工作，而 response.content
#是二进制字节流（bytes），无法直接被解析。
#先看响应头（Content-Type）里是否声明编码（比如 charset=gbk），
#如果有，就用这个编码解码；如果响应头没声明，
#requests 会默认用 ISO-8859-1（一种西文编码）解码，
#而 GBK 是中文编码，用 ISO-8859-1 解码必然乱码。
from bs4 import BeautifulSoup
import requests
'''headers={
    'user-agent':"",
    'referer':"",
    'cookie':""
}'''
url=''
path=r'D:\Webpage\4.html'
#response=requests.get(url,headers=headers)
response=requests.get(url)
'''
#自动识别并设置网页编码
#apparent_encoding 会分析网页内容，得出真实编码
response.encoding=response.apparent_encoding
'''
#soup=BeautifulSoup(response.text,'html.parser')
#format=soup.prettify()
with open(path,'wb')as f:
    f.write(response.content)
    #f.write(format.encode('utf-8'))