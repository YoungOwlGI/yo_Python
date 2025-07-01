import pandas as pd
import requests
from bs4 import BeautifulSoup

# 替换为你想要爬取的网址
url = 'https://order.jd.com/center/list.action'

# 使用requests库发送GET请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 获取网页源代码
    source_code = response.text
    print(source_code)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

