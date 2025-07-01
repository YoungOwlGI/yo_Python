import requests
import re

# 请求URL
url = '<http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html>'
# 请求头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}


# 解析页面函数
def parse_html(html):
    pattern = re.compile(
        '<tr class="alt">.*?<td>(.*?)</td>.*?<td><div align="left">.*?<a href="(.*?)" target="_blank">(.*?)</a></div></td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?</tr>',
        re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            '排名': item[0],
            '学校名称': item[2],
            '省市': item[3],
            '总分': item[4]
        }


# 保存数据函数
def save_data():
    f = open('university_top100.txt', 'w', encoding='utf-8')
    response = requests.get(url, headers=headers)
    for item in parse_html(response.text):
        f.write(str(item) + '\\\\n')
    f.close()


if __name__ == '__main__':
    save_data()
