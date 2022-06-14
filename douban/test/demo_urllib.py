# -*- coding = utf-8 -*-
# @Time : 2022/4/10 20:18
# @Author : 牧川
# @File : demo_urllib.py
import json
import urllib.request
import urllib.parse

#request方法访问，获取的是get请求：
# result = urllib.request.urlopen("http://httpbin.org/get")
# str1 = result.read().decode('utf-8')
# print(str1)

#获取一个post请求
#进行post请求时，需要先封装数据
# Udata = urllib.parse.urlencode({"name":"ww"})   #通过encode，将字典数据进行编码
# data1 = bytes(Udata,encoding = 'utf-8')  #编码后的数据，以一定的encode方式，转化为bytes格式
# result = urllib.request.urlopen("http://httpbin.org/post",data= data1)
# print(result.read().decode('utf-8'))

# #网页返回值的一些内置方法：
# result = urllib.request.urlopen("http://httpbin.org/get")
# #获取完整的headers
# print(result.getheaders())
# #获取某条header属性
# print(result.getheader('Server'))

#对于防御爬虫的网站，需要包装一下自己的UA
# url = "https://www.arealme.com/how-long-would-you-survive-a-zombie-apocalypse/cn/"
# Udata = urllib.parse.urlencode({"name":"ww"})   #通过encode，将字典数据进行编码
# data1 = bytes(Udata,encoding = 'utf-8')
# header1 = {
# "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
# }
# req = urllib.request.Request(url=url,data=data1,headers=header1,method="POST")
# result = urllib.request.urlopen(req)
# print(result.read().decode('utf-8'))

#request方法访问，获取的是get请求：
import pic as pic
from bs4 import BeautifulSoup

#获取一个post请求
#进行post请求时，需要先封装数据
url = "https://www.yiyandingzhen.top/"
url1 = url + "getpic.php"
Udata = urllib.parse.urlencode({"name":"ww"})   #通过encode，将字典数据进行编码
data1 = bytes(Udata,encoding = 'utf-8')
header1 = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}
req = urllib.request.Request(url=url1,data=data1,headers=header1,method="GET")
result = urllib.request.urlopen(req)
str1 = result.read().decode('utf-8')
json1 = json.loads(str1)
json1 = json1[0]
print(json1)
print(json1['fore']['0'])
print(json1['mid']['0'])
print(json1['suffix']['0'])
pic = url + json1['picpath']['0']
print(pic)

# bs = BeautifulSoup(str1,"html.parser")
# print(bs.select('#rand-pic'))
