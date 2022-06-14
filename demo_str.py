# -*- coding = utf-8 -*-
# @Time : 2022/4/30 11:39
# @Author : 牧川
# @File : demo_str.py

a = 300
str = '京国多年情尽改，忽听春雨忆江南'
print(f'a的值为：{a}\n再来句诗：{str}')
#步长为负数就是倒着来
print(str[::-1])
#字符串的查找、判断、修改：

#find方法中，第一个参数为要查找的对象，外加两个范围参数。返回值为匹配的第一个位置的index。没找到返回-1
print(str.find('江南'))
print(str.find('杏花',0,-1))
#index方法用法与find相同，但是找不到会抛出异常
print(str.index('江南'))
#count入参同上，但是返回结果为匹配到的数量
print(str.count('春雨'))

#大小写切换用upper、lower
info = "Hi,do you have a Pen?"
print(info.upper())
print(info.lower())
print(info.title()) #每个单词的首字母大写
#replace方法替换时，如果不输入参数默认为全替换，输入参数可以指定替换几次
print(info.replace('a',''))
print(info.replace('a','',1))
#split方法，依据入参字符串，将字符串分割（且入参字符串本身会被去掉）.不填参数会以空格分割
temp = info.split('a')
print(temp)
print(type(temp))
#join拼接：
print('a'.join(temp)) #拼接temp这个list为str，每个成员之间以'a'连接

#判断：startwith、endwith
print(str.startswith('京'))
print(str.endswith('江南'))