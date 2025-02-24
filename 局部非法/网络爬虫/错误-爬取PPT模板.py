# 导入请求模块
import re

import requests
# 忽略警告
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

page = 1  # 页数, 从第一页开始
while True:
    if page == 1:
        # 第一页
        url = 'https://www.ypppt.com/moban/'
    else:
        # 从第二页开始
        url = f'https://www.ypppt.com/moban/list-{page}.html'
    # 请求网址获得响应
    res = requests.get(url, headers=headers, verify=False)
    # 提取数据
    res.encoding = 'utf-8'  # 编码改成utf-8
    # print(res.text)
    ppt_info = re.findall('href="/article/.*?/(.*?).html" class="p-title" target="_blank">(.*?)</a>', res.text)
    for i, title in ppt_info:
        # 构造新的链接
        url1 = 'https://www.ypppt.com/p/d.php?aid=' + i
        res1 = requests.get(url1, headers=headers, verify=False)
        # print(res1.text)
        # 提取数据
        down_url = re.findall('href="(.*?)">下载地址1</a>', res1.text)[0]
        if 'pan.baidu' in down_url:  # 百度网盘下载
            continue
        else:
            suffix = down_url.split('.')[-1]  # 获取后缀名
        res2 = requests.get(down_url, headers=headers, verify=False)
        open(f'PPT模版/{title}-{i}.{suffix}', 'wb').write(res2.content)
        print(f'已成功下载{title}-{i}.{suffix}')
    page += 1  # 爬完之后页数+1
