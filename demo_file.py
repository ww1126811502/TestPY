# -*- coding = utf-8 -*-
# @Time : 2022/4/10 12:42
# @Author : 牧川
# @File : demo_file.py
import os
#写文件的函数：
def writeStr(file,str1):
    try:
        f = open(file, "w", encoding="gbk")
        try:
            f.write(str1)
            print("向文件：%s文本写入完成！"%f.name)
        finally:
            f.close()
    except Exception:
        print("文件名称填写错误！写入时")

#读文件的函数：
def readStr(file):
    try:
        f = open(file, "r", encoding="gbk")
        try:
            str2 = f.read() #read是读取指定字节的内容，不填参数则读取所有字节
            #str2 = f.readline() #readline读取一行
            # str2 = f.readlines() #readlines按行读取，读入所有行为列表
            print("文本读取完成！")
            return str2
        finally:
            f.close()
    except Exception:
        print("文件名称填写错误！读取时")

#先写古诗进去：
#str = "相见时难别亦难，东风无力百花残。\n春蚕到死丝方尽，蜡炬成灰泪始干。\n晓镜但愁云鬓改，夜吟应觉月光寒。\n蓬山此去无多路，青鸟殷勤为探看"
#writeStr("gushi.txt",str)
# str = readStr("gushi.txt")
# writeStr("copy.txt",str)
print(os.getcwd())  #返回当前工作目录
print(os.path.abspath('test.py'))   #返回目标文件的绝对路径
print(os.listdir('.'))  #返回目标目录下的所有文件/文件夹，'.'代表当前所在目录