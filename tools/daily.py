import os
import asyncio
import subprocess
from playwright.async_api import async_playwright as ll
a=''#网站链接
b=r'D:\Video'#存的文件夹目录
e='output4.mp4'#文件名
os.makedirs(b,exist_ok=True)
async def main():
    async with ll() as p:
        c=await p.chromium.launch(headless=False)
        d=await c.new_page()
        gather=[]
        async def moniter(request):
            if'.m3u8'in request.url or'.ts'in request.url:
                if request.url not in gather:
                    gather.append(request.url)
                    print(f"捕获到视频资源: {request.url}")
        d.on('request',moniter)
        await d.goto(a)
        input('检查抓包情况，就是视频没开始就点一下播放。回车继续：')
        await c.close()
        if gather:
            m3u8=next((url for url in gather if'.m3u8'in url),None)
            if m3u8:
                path=os.path.join(b,e)
                subprocess.run(['ffmpeg','-i',m3u8,'-c','copy',path],check=True)
                print(f'视频已保存至{path}')
asyncio.run(main())