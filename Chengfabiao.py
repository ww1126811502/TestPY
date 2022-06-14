# -*- coding = utf-8 -*-
# @Time : 2022/4/9 17:36
# @Author : 牧川
# @File : Chengfabiao.py
'''
row = 1
col = 1
for i in range(1,10):
    for n in range(0,i):
        print(row,"x",col,"=",row*col,sep="",end=" ")
        col+=1
    print("")
    col = 1
    row+=1
'''
for n in range(1,10):
    for m in range(1,n+1):
        print("%dx%d=%d"%(n,m,n*m),end=" ")
    print("")