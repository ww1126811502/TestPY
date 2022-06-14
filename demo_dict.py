# -*- coding = utf-8 -*-
# @Time : 2022/4/10 9:55
# @Author : 牧川
# @File : demo_dict.py

info ={"name":"牧川","age":"24","job":"designer"}
info["game"] = "eve"
#访问数据的两种方法：
print(info["name"]) #直接用key访问，如果key不存在，抛出异常
print(info.get("name")) #get方法访问时，如果key不存在，会返回none

keys = list(info.keys())
values = list(info.values())
items = list(info.items())
#返回的items是一个列表，每个要素是键值对
print(items)
for key,value in info.items():
    print(key,value)

