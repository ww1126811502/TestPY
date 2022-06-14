# -*- coding = utf-8 -*-
# @Time : 2022/5/4 18:13
# @Author : 牧川
# @File : demo_dingzhen.py
import json
import urllib.request
import urllib.parse

def main():
    #设置一个最大的uid
    max = 1200
    for id in range(max):
        picurl = getPic(id)
        if picurl:
            savePic(picurl, id)
        else:
            pass

    # https://www.yiyandingzhen.top/pic/350_yiyandingzhen.gif
    #savePic("https://www.yiyandingzhen.top/pic/350_yiyandingzhen.gif", id)

def getPic(id):
    url = "https://www.yiyandingzhen.top/"
    phpurl = url + "getpic.php"

    Udata = urllib.parse.urlencode({"id":"%d"%id})   #通过encode，将字典数据进行编码
    data1 = bytes(Udata,encoding = 'utf-8')
    header1 = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    }
    req = urllib.request.Request(url=phpurl,data=data1,headers=header1,method="POST")

    result = urllib.request.urlopen(req)
    str1 = result.read().decode('utf-8')
    picjson = json.loads(str1)
    picjson = picjson[0]
    if picjson['picpath']['0'] == "pic/daishenhe.png":
        print(f'id:{id}没有对应的图片')
        return False
    else:
        picpath = url + picjson['picpath']['0']
        print(picpath)
        return picpath

def savePic(picurl,id):
    import requests
    r = requests.get(picurl, stream=True)

    image = requests.get(picurl).content
    print(str(id) + '.jpg 正在保存...')
    with open('./img/' + str(f"dingzhen_{id}") + '.jpg', 'wb') as fp:
        fp.write(image)

    # with open(f'/dingzhen/dingzhen_{id}.jpg', 'wb') as fd:
    #     for chunk in r.iter_content():
    #         fd.write(chunk)


if __name__ == "__main__":
    main()