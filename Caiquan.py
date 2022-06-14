# -*- coding = utf-8 -*-
# @Time : 2022/4/9 16:06
# @Author : 牧川
# @File : Caiquan.py
import random

#先生成一个随机数
rob = random.randint(0,2)
#读入一个玩家的输入
p = int(input("请出拳：0-剪刀，1-石头，2-布"))
#数据验证
if p!=0 and p!=1 and p!=2:
    print("只能输入0、1、2中的一个！")
    exit()
#猜拳结果：
print("电脑出的是：%d"%rob)
r = p-rob
if r==1 or r==-2:
    print("恭喜！你赢了")
elif r==-1 or r==2:
    print("很遗憾，电脑赢了")
elif r==0:
    print("是平局呢")