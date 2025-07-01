#-*- coding = utf-8 -*-
#Time : 2021/1/20
#Author : 小柠檬
#File : QQ空间扫码登录模板.py
import requests
from PIL import Image
import time
import re

def bkn(pSkey):
    #计算bkn
    t,n,o = 5381,0,len(pSkey)

    while n < o:
        t += (t << 5) + ord(pSkey[n])
        n += 1

    return t & 2147483647

def ptqrToken(qrsig):
    #计算ptqrtoken
    n,i,e = len(qrsig),0,0

    while n > i:
        e += (e << 5) + ord(qrsig[i])
        i += 1

    return 2147483647 & e

def QR():
    #获取 qq空间 二维码
    url = 'https://ssl.ptlogin2.qq.com/ptqrshow?appid=549000912&e=2&l=M&s=3&d=72&v=4&t=0.8692955245720428&daid=5&pt_3rd_aid=0'

    try:
        r = requests.get(url)
        qrsig = requests.utils.dict_from_cookiejar(r.cookies).get('qrsig')

        with open(r'C:\Users\Administrator\Desktop\QR.png', 'wb') as f:
            f.write(r.content)

        im = Image.open(r'C:\Users\Administrator\Desktop\QR.png')
        im = im.resize((350, 350))
        print(time.strftime('%H:%M:%S'),'登录二维码获取成功')
        im.show()

        return qrsig

    except Exception as e:
        print(e)

def cookie():
    #获取 QQ空间 cookie
    qrsig = QR()
    ptqrtoken = ptqrToken(qrsig)

    while True:
        url = 'https://ssl.ptlogin2.qq.com/ptqrlogin?u1=https%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&ptqrtoken=' + str(ptqrtoken) + '&ptredirect=0&h=1&t=1&g=1&from_ui=1&ptlang=2052&action=0-0-' + str(time.time()) + '&js_ver=20032614&js_type=1&login_sig=&pt_uistyle=40&aid=549000912&daid=5&'
        cookies = {'qrsig': qrsig}

        try:
            r = requests.get(url, cookies=cookies)

            if '二维码未失效' in r.text:
                print(time.strftime('%H:%M:%S'),'二维码未失效')

            elif '二维码认证中' in r.text:
                print(time.strftime('%H:%M:%S'),'二维码认证中')

            elif '二维码已失效' in r.text:
                print(time.strftime('%H:%M:%S'),'二维码已失效')

            else:
                print(time.strftime('%H:%M:%S'), '登录成功')

                cookies = requests.utils.dict_from_cookiejar(r.cookies)
                uin = requests.utils.dict_from_cookiejar(r.cookies).get('uin')
                regex = re.compile(r'ptsigx=(.*?)&')
                sigx = re.findall(regex, r.text)[0]
                url = 'https://ptlogin2.qzone.qq.com/check_sig?pttype=1&uin=' + uin + '&service=ptqrlogin&nodirect=0&ptsigx=' + sigx + '&s_url=https%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&f_url=&ptlang=2052&ptredirect=100&aid=549000912&daid=5&j_later=0&low_login_hour=0&regmaster=0&pt_login_type=3&pt_aid=0&pt_aaid=16&pt_light=0&pt_3rd_aid=0'

                try:
                    r = requests.get(url, cookies=cookies, allow_redirects=False)
                    targetCookies = requests.utils.dict_from_cookiejar(r.cookies)
                    pSkey = requests.utils.dict_from_cookiejar(r.cookies).get('p_skey')
                    break

                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)

        time.sleep(3)

    return targetCookies

def test():
    url = 'https://act.iwan.qq.com/trpc.iwan.mission_system_server.MissionSystemSvr/dealSimpleMission?missionId=mZZrWSzG7&gameId=26080&sPlat=0&sArea=2&serverId=&sRoleId=1&platformId=9&platformid=9&guid=53383d1eb5b611e89d19a042d48ad00a&device=453C45EA-B7B4-40C8-AE8C-F823796AF191&token=1324739766&acctype=qq'
    cookies = cookie()
    r = requests.get(url,cookies=cookies)
    print(r.text)

if __name__ == '__main__':
    test()
