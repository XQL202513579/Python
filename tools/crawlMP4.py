import requests
headers={
'User-Agent':"",
'Referer':"",
'Cookie':""
}
#视频文件里的标头有，一般这仨就够了
url=''
#视频链接，B站是"video里的"baseUrl
path=r'D:\Video'#目录+文件名，即路径
response=requests.get(url,headers=headers)
with open(path,'wb')as f:
    f.write(response.content)