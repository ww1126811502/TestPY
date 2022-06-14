# -*- coding = utf-8 -*-
# @Time : 2022/4/16 11:03
# @Author : 牧川
# @File : demo_SQLite.py
import sqlite3

#打开或创建数据库文件
connet = sqlite3.connect("test.db")
#获取游标
c = connet.cursor()
#编写sql语句
    #建表
# sql = '''
#     create table compony
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         adress char(50),
#         salary real);
# '''
    #插入数据：
# sql = '''
#     insert into compony(id,name,age,adress,salary)
#      values (1,'张三',32,'成都',8000)
# '''
    #查询数据
sql = "select id,name,age,adress,salary from compony"

#执行sql语句，根据命令有无返回值，两种执行方法
    #直接执行：
#c.execute(sql)
    #用游标接收返回值：
cursor = c.execute(sql)
#遍历查询的数据：
for row in cursor:
    print("id=",row[0])
    print("name=", row[1])
    print("age=", row[2])
#提交并关闭
#connet.commit()
connet.close()



print("成功")