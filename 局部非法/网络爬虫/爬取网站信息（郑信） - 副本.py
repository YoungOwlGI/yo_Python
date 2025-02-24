import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# 爬虫主函数
def crawl_website(url):
    # 发送 HTTP 请求
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析网页内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 创建文件夹保存图片
        if not os.path.exists('images'):
            os.makedirs('images')

        # 提取文本
        print("=== 页面中的文本内容 ===")
        for paragraph in soup.find_all('p'):
            text = paragraph.get_text()
            print(text)

        # 提取并下载图片
        print("\n=== 页面中的图片 ===")
        img_tags = soup.find_all('img')
        for img in img_tags:
            img_url = img.get('src')
            img_url = urljoin(url, img_url)  # 处理相对路径

            # 下载图片并保存
            img_name = os.path.join('images', img_url.split('/')[-1])
            with open(img_name, 'wb') as f:
                img_data = requests.get(img_url).content
                f.write(img_data)
                print(f"已下载图片: {img_name}")
    else:
        print(f"无法访问 {url}, 状态码: {response.status_code}")


# 目标网址
url = 'https://blog.csdn.net/dongfuguo/article/details/130518352'

# 执行爬虫
crawl_website(url)
