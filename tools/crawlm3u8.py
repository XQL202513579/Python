import asyncio
import os
import subprocess
from playwright.async_api import async_playwright

# 配置
TARGET_URL = "https://skr.skr1.cc:666/vodplay/216813-2-6/"  # 替换为目标视频页面
SAVE_DIR = r"D:\Video"
os.makedirs(SAVE_DIR, exist_ok=True)

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # 非无头模式便于观察
        page = await browser.new_page()
        
        video_urls = []
        
        # 监听网络请求
        async def handle_request(request):
            if ".m3u8" in request.url or ".ts" in request.url:
                if request.url not in video_urls:
                    video_urls.append(request.url)
                    print(f"捕获到视频资源: {request.url}")
        
        page.on("request", handle_request)
        
        # 打开页面并等待视频加载
        await page.goto(TARGET_URL)
        print("请手动播放视频，按回车键继续...")
        input()  # 等待用户手动触发视频播放
        
        await browser.close()
        
        # 这里仅演示捕获逻辑，实际下载和合并需根据视频类型处理：
        # 1. 如果是 m3u8 地址，可直接用 FFmpeg 下载合并
        if video_urls:
            m3u8_url = next((url for url in video_urls if ".m3u8" in url), None)
            if m3u8_url:
                output_path = os.path.join(SAVE_DIR, "output.mp4")
                subprocess.run(
                    ['ffmpeg', '-i', m3u8_url, '-c', 'copy', output_path],
                    check=True
                )
                print(f"视频已保存至: {output_path}")

asyncio.run(main())