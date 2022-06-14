# -*- coding = utf-8 -*-
# @Time : 2022/4/11 21:43
# @Author : 牧川
# @File : demo_bs4.py
from bs4 import BeautifulSoup
import re

with open("douban.html","rb") as file:
    html = file.read()
#使用bs的解析器解析html，保存结果
bs = BeautifulSoup(html,"html.parser")
#基础使用：
#1、bs.+标签名，会直接返回html中，第一个匹配的标签
#print(bs.title)
#2、bs.+标签名+.string，会直接返回html中，第一个匹配的标签中的str内容，如果内容为注释，会自动去掉注释符号
#print(bs.title.string)
#bs.+标签名+.attrs，返回该标签的所有属性值，返回内容为dict
#print(bs.a.attrs)
#3、保存后的结果，可以直接调用各种函数，或者直接整体打印
#print(bs)

#文档的遍历：
#有多种遍历方式，举例contents一种
#contents，将标签中的内容以list的形式全部返回
# print(bs.head.contents)
# print(bs.head.contents[3])

#find_all()文档的搜索（重要！）：
#字符串过滤：查找所有与字符串完全匹配的标签，返回值为列表，添加limit关键字可以限制最大数量
# t_list = bs.find_all("span")
# print(t_list)
#正则表达式：参数可以填写正则
# t_list = bs.find_all(re.compile('an'))
# print(t_list)
#传入一个函数：
# def name_is_exists(tag):
#     return tag.has_attr("content")
# t_list = bs.find_all(name_is_exists)
# print(t_list)
#kwords：对关键词进行匹配，使用class时，记得加“_”；
# t_list = bs.find_all(class_="title")
# print(t_list)
#text：同对文本进行检索，且text可以是列表或正则
# t_list = bs.find_all(text=["龙猫","指环王"])
# print(t_list)
# t_list2 = bs.find_all(text=re.compile('\d'))
# print(t_list2)

#select()：css选择器，直接通过标签或属性定位，返回列表
#指定标签：
#print(bs.select('title'))
#指定class,用“.”来指代class：
#print(bs.select(".global-nav"))
#指定id：用“#”来指代id
#print(bs.select("#db-global-nav"))
#指定属性：标签名[属性=属性值]
#print(bs.select("script[type='text/javascript']"))
#查找子标签层层查找
#print(bs.select("div > a > span"))
#查找兄弟标签
# bs.select(".pic ~ .info")   #这里用的是同层级的class来查找，同样也可以用属性或标签
# for i in bs.select(".pic ~ .info"):
#     print(i.getText())