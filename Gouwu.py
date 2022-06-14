# -*- coding = utf-8 -*-
# @Time : 2022/4/9 23:31
# @Author : 牧川
# @File : Gouwu.py
import random

coms = [["iphone",6888],["MacPro",14800],["小米6",2499],["coffee",31],["book",60],["nike",699]]
car = []
p = 0
#先打印商品列表
while True:
    print("-"*5,"  商品列表  ","-"*5)
    for i,com in enumerate(coms):
        print(i+1,com[0],"\t",com[1],sep=" ")
    index = input("请输入要购买商品的序号（按q退出）：")
    if index == "q":
        print("您的购物车中有：")
        for ca in car:
            print(ca[0],"、",sep="")
        print("\n总价为：%d"%p)
        break
    elif int(index) > len(coms):
        print("该序号不存在！请重新输入")
    elif int(index) < len(coms):
        p += coms[int(index)][1]
        car.append(coms[int(index)])
        del coms[int(index)]
