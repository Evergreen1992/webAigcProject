import requests
from bs4 import BeautifulSoup


#下载抖音视频
def download_video(url, filename):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Referer': url,
        'Upgrade-Insecure-Requests': '1'
    }

    # 下载视频
    response = requests.get(url, stream=True, headers=headers)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f"Video downloaded successfully as {filename}")
    else:
        print(f"Failed to download the video, status code: {response.status_code}")


if __name__ == "__main__":
    url = "https://v3-cold.douyinvod.com/0bf23b056e87e9712a41faf20e9b5391/6717f6e6/video/tos/cn/tos-cn-ve-15/owQQEIvZAA5jBrfC7LegbOGC98Lf6IBYytBFat/?a=1128&ch=0&cr=0&dr=0&er=0&lr=unwatermarked&cd=0|0|0|0&cv=1&br=794&bt=794&cs=0&ds=3&ft=K.3PX5DDhNvjVQpG6G47usJ39ApzXzf9VcnztGxL&mime_type=video_mp4&qs=0&rc=ZTxnZWY3ODU2OThlNjQ3NUBpM3g4c285cmZndjMzNDlpM0AvMV5iYmM0NmIxYWE0Xy4uYSNxam1zMmRjc19gLS1kMC9zcw==&btag=c0010e00088000&cquery=100g&dy_q=1729580574&feature_id=aa7df520beeae8e397df15f38df0454c&l=2024102215025489209820249FA7FADBDE"
    download_video(url, "d://output.mp4")