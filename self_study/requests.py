'''
urlopen：response.read() → 还要自己 decode
requests：response.text 直接字符串，response.content 直接二进制（下视频用这个！）

from urllib.request import Request
req = Request(url, headers={'User-Agent': '...'})
response = urlopen(req)

import requets
requests.get(url, headers={...})

请求头：
- User-Agent（最重要）：伪装成浏览器
告诉网站：你是什么设备、什么浏览器。不带这个，很多网站直接拒绝、返回空、403。
- Referer（防盗链必备！视频必带）
告诉网站：你是从哪个页面点进来的。视频网站、图片站全靠这个防盗链。
- Origin
和 Referer 类似，只写域名，不写路径。多用于跨域请求、API、视频接口。
- Cookie
你的登录状态、身份。带 Cookie = 你已登录，能看会员内容。
- Authorization
登录 /token 验证，API 常用。
- Accept / Accept-Encoding / Accept-Language
告诉服务器你能接受什么格式、编码、语言。可带可不带，但带上更像真人。
'''
import requests
import os
def download_video(video_url, save_folder, file_name):
    """
    下载视频到指定文件夹
    :param video_url: 视频的直接访问URL（关键！需替换为实际有效链接）
    :param save_folder: 保存文件夹路径（D盘）
    :param file_name: 保存的视频文件名（含后缀，如test.mp4）
    """
    # 1. 创建D盘的目标文件夹（不存在则创建）
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
        print(f"文件夹 {save_folder} 创建成功")
    else:
        print(f"文件夹 {save_folder} 已存在")
    # 2. 拼接完整的保存路径
    save_path = os.path.join(save_folder, file_name)
    # 3. 发送请求下载视频（添加请求头，模拟浏览器访问）
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        # 分块请求（stream=True），避免一次性加载大文件到内存
        response = requests.get(video_url, headers=headers, stream=True, timeout=30)
        response.raise_for_status()  # 抛出HTTP请求错误（如404、500）
        # 4. 写入文件（分块写入）
        chunk_size = 1024 * 1024  # 每次写入1MB
        total_size = int(response.headers.get("Content-Length",0))  # 视频总大小
        downloaded_size = 0
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:     #!=NULL
                    f.write(chunk)
                    downloaded_size += len(chunk)
                    # 打印下载进度
                    progress = (downloaded_size / total_size) * 100 if total_size > 0 else 0
                    print(f"下载进度: {progress:.2f}% ({downloaded_size/1024/1024:.2f}MB/{total_size/1024/1024:.2f}MB)", end="\r")
        print(f"\n视频下载完成！保存路径：{save_path}")
    except requests.exceptions.RequestException as e:
        print(f"下载失败：{e}")
    except Exception as e:
        print(f"未知错误：{e}")
# ===================== 配置参数（需根据实际情况修改） =====================
if __name__ == "__main__":
    # 替换为实际的视频直链（关键！示例为测试链接，仅用于演示）
    target_video_url = "https://skr.skr1.cc:666/vodplay/203209-1-136/"
    # D盘创建的文件夹（示例：D:\downloaded_videos）
    target_folder = r"D:\downloaded_videos"
    # 保存的文件名
    video_file_name = "test_video.mp4"
    # 执行下载
    download_video(target_video_url, target_folder, video_file_name)

import requests
# 必须先导入requests库
# 基本用法：向指定URL发GET请求
response = requests.get(
    url="目标网址",  # 必传：要请求的地址
    headers=None,   # 可选：请求头,模拟浏览器标识,避免被服务器识别为爬虫
    stream=False,   # 可选：是否分块接收数据（大文件用True）
    timeout=None    # 可选：超时时间（防止一直等待）
)
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
#最核心的字段是 User-Agent：不同浏览器的 User-Agent 不同，网上搜「User-Agent 大全」可找到最新值；
#不加 headers 的风险：很多网站会把无 User-Agent 的请求判定为爬虫，返回 403（禁止访问）或 503 错误。
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"  # 可选：表示接受的内容类型
}
#高速请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Referer": "这里填视频网页的地址",  # 必须填！
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
    #Connection: "keep-alive" 让客户端和服务器的 TCP 连接不立即关闭
    #若你后续还有对该网站的其他请求（比如爬多个视频），
    #可以复用同一个连接，避免每次请求都重新建立 TCP 连接（TCP 握手需要时间）
}
#你下载视频时，服务器会告诉浏览器「这个文件有多大（Content-Length）」
#「这是个 MP4 文件（Content-Type）」
# —— 这些信息都存在响应头里，headers.get() 就是提取这些信息。
#用 get() 而不是直接取:有些服务器可能不返回 Content-Length，
#直接写 response.headers["Content-Length"] 会报「KeyError」，
#而 get() 只会返回 None，程序不会崩溃；
'''
Content-Length：文件总大小（字节）
Content-Type：内容类型（如 video/mp4、text/html）
User-Agent：（请求头里用）浏览器标识
Cookie：用户登录信息

response.iter_content(chunk_size=数值) 是
「分块读取响应内容」的方法，返回一个迭代器，每次读取指定大小的字节数据（适合大文件下载）。

F12 抓包
打开目标视频页，按 F12 打开开发者工具，切换到 Network（网络） 面板。
勾选 Preserve log（防止页面刷新清空日志），过滤栏输入 media、mp4、m3u8 快速定位。
刷新页面并播放视频，在请求列表中找到体积最大、类型为 media 或后缀为 .mp4/.m3u8 的条目。
选中该条目，在右侧 Headers 中复制 Request URL（这就是直链）。
'''
#you-get -o D:\VIDEOpy https://skr.skr1.cc:666/vodplay/203209-1-136/

import subprocess
# 1. 替换为你抓到的m3u8链接
m3u8_url = "https://m3u8xx.sgzm.net:2087/https://s1.fengbao9.com/video/mowangdenvertaiwenroule/6254f770833f/index.m3u8"
# 2. 保存到D盘的视频路径
save_path = r"D:\downloaded_videos"
# 3. ffmpeg的完整路径（根据你解压的位置修改）
ffmpeg_path = r"D:\ffmpeg\ffmpeg-2026-03-09-git-9b7439c31b-full_build\bin\ffmpeg.exe"
# 执行合并命令（修改后）
try:
    result = subprocess.run([
        ffmpeg_path,  # 用完整路径代替直接写ffmpeg
        "-i", m3u8_url,
        "-c", "copy",  # 快速复制，不重新编码
        "-bsf:a", "aac_adtstoasc",  # 解决部分MP4无法播放的问题
        save_path
    ], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"视频合并成功！保存路径：{save_path}")
    else:
        print(f"合并失败，错误信息：{result.stderr}")
except Exception as e:
    print(f"程序出错：{e}")


import requests,os
response=requests.get('url',headers={},stream=True,timeout=30)
response.headers.get('Content-Type''Contet-Length')
response.iter_content(chunk_size=1024)
response.raise_for_status()
requests.exceptions.RequestException
os.path.exists()
os.path.join()

from urllib import request
from bs4 import BeautifulSoup as pp
a=request.urlopen('https://cn.bing.com/')
#import requests
#a=requests.get('https://cn.bing.com/')
#a.encoding = 'utf-8'
#if a.status_code == 200:
#或者 a.raise_for_status()
b=a.read().decode('utf-8')
c=pp(b,'html.parser')
d=c.prettify()
f=c.find('title')#.get_text()用于提取标签中的文本内容
g=f.get('href')#<a class="mnav" href="http://news.baidu.com" name="tj_trnews">新闻</a>
h=c.find_all('a')# 查找所有 <a> 标签
# 查找所有 class="example-class" 的 <div> 标签
i= c.find_all('div', class_='example-class')
'''
# 获取当前标签的父标签
parent_tag = first_link.parent
# 获取当前标签的所有子标签
children = first_link.children
'''
with open('file.txt','w+',encoding='utf-8') as e:
    e.write(d)
print(f)
print(g)
print(h)

# 使用 CSS 选择器查找所有 class 为 'example' 的 <div> 标签
example_divs = c.select('div.example')
# 查找所有 <a> 标签中的 href 属性
links = c.select('a[href]')
# 修改第一个 <a> 标签的 href 属性
f['href'] = 'http://new-url.com'
# 修改第一个 <p> 标签的文本内容
j= c.find('p')
j.string = 'Updated content'
# 删除某个标签
f.decompose()