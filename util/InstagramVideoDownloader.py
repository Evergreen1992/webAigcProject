import requests
from bs4 import BeautifulSoup


def download_instagram_video(url):
    # 1. 获取Instagram页面的HTML
    response = requests.get(url)
    if response.status_code != 200:
        print("无法访问页面")
        return

    # 2. 解析HTML以找到视频链接
    soup = BeautifulSoup(response.text, 'html.parser')
    video_tag = soup.find('meta', property="og:video")

    if video_tag:
        video_url = video_tag['content']
        print(f"视频链接: {video_url}")

        # 3. 下载视频文件
        video_response = requests.get(video_url)
        if video_response.status_code == 200:
            with open("d://instagram_video.mp4", 'wb') as video_file:
                video_file.write(video_response.content)
            print("视频下载完成: instagram_video.mp4")
        else:
            print("视频下载失败")
    else:
        print("未找到视频链接")

# 示例使用
instagram_post_url = 'https://www.instagram.com/reel/CerLMjuJIsG/'  # 替换为实际的Instagram帖子URL
download_instagram_video(instagram_post_url)