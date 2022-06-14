# -*- coding = utf-8 -*-
# @Time : 2022/4/9 22:15
# @Author : 牧川
# @File : demo_list.py

nameList = ["张三","李四","王五"]
#常见的遍历方式：
'''
for name in nameList:
    print(name)
'''
#增加数据：
nameList.append("佐助")   #末尾新增元素
nameList.extend(nameList)   #合并列表，如果入参是字符串，会被拆成单个的字符加入
nameList.insert(3,"鸣人") #在中间插入元素，鸣人变为序列3，从3开始的序列加一
#删除数据
del nameList[0:2]
nameList.pop()  #默认删除尾部，可以加参数指定序列。返回值即为被删除的单位
nameList.pop(1)
nameList.remove("王五")
#查找数据
n = "王五"
print(n in nameList)
#反转列表
nameList.reverse()
#排序
nameList.sort(reverse=False)
#遍历值：
for name in nameList:
    print(name)
#遍历枚举：
for i,name in enumerate(nameList):
    print(i,name)