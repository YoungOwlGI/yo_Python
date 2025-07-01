import re  # 导入re模块

import requests  # 导入requests库


# 定义一个getHtml()函数，根据填写的url参数获取数据
def getHtml(url):
    # 异常处理
    try:
        r = requests.get(url)  # 使用get函数打开指定的url
        r.raise_for_status()  # 如果状态不是200，则引发异常
        r.encoding = 'utf-8'  # 更改编码方式
        return r.text  # 返回页面内容
    except:
        return ""  # 发生异常返回空字符


# 定义一个getImg()函数，根据填写的html参数获取图片并存储
def getImg(html):
    reg = r'src="(.+?\.jpg)"'  # 定义正则表达式
    imglist = re.findall(reg, html)  # 查找页面中所有符合条件的字符串
    print(imglist)  # 输出列表结果
    i = 0  # 定义i用于给下载的图片命名
    for url in imglist:  # 遍历
        with open("D:\猫头鹰的文件\计算机专题\Python\局部非法\网络爬虫" + str(i) + ".jpg", "jpeg") as fd:  # 以写入方式打开二进制文件
            # 路径前加上“http://www.bjjqe.com”
            response = requests.get(
                "https://cn.bing.com/images/search?q=%e5%8e%9f%e7%a5%9e&form=HDRSC2&first=1/" + url)  # 获取内容
            fd.write(response.content)  # 写入文件
            print('图片', i, "保存成功\n")  # 输出提示信息
            i += 1  # i加1


html = getHtml("https://cn.bing.com/images/search?q=%e5%8e%9f%e7%a5%9e&form=HDRSC2&first=1/")  # 调用获取页面内容函数
getImg(html)  # 调用获取图片并存储函数
