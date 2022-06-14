# -*- coding = utf-8 -*-
# @Time : 2022/4/9 14:48
# @Author : 牧川
# @File : test.py
import urllib.request
from urllib.parse import quote


def main():
    urltest()

def modif():
    a = 300
    str = '京国多年情尽改，忽听春雨忆江南'
    print(f'a的值为：{a}\n再来句诗：{str}')
    print(str[::-1])
    rs = str if a>200 else str.count()
    print(rs)

def urltest():
    # str = "你好"
    # str = quote(str)
    # url = f'https://s4w-2019.zhiyin.sogou.com/tts?language_code=zh-cmn-Hans-CN&speaker=xiyue-pro&charset=UTF-8&speaking_rate=1&volume=1&text={str}'
    #
    # url = f'https: // tts.tencentcloudapi.com /?Action = TextToVoice& Timestamp = 1& Version = 2019 - 08 - 23& Text = {str}& SessionId = session - 1234& Volume = 1& VoiceType = 101016& Speed = 1& ProjectId = 0& ModelType = 1& PrimaryLanguage = 1& SampleRate = 16000& Codec = wav'
    # header1 = {
    #     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    #     }
    # req = urllib.request.Request(url=url,headers=header1,method="POST")
    # result = urllib.request.urlopen(req)
    # print(result)
    # str1 = result.read().decode('utf-8')
    # print(str1)
    url = "https://genshin.minigg.cn/index.html"
    Udata = urllib.parse.urlencode({"characters":"神里绫华","audiid":1001,"language":"zhcn"})   #通过encode，将字典数据进行编码
    data1 = bytes(Udata,encoding = 'utf-8')
    header1 = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    }
    req = urllib.request.Request(url=url,data=data1,headers=header1,method="GET")
    result = urllib.request.urlopen(req)
    print(result.read().decode('utf-8'))


if __name__ =='__main__':
    main()