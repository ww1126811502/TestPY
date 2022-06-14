# -*- coding = utf-8 -*-
# @Time : 2022/4/30 18:19
# @Author : 牧川
# @File : demo_class.py
class Person:
    def __init__(self,name,age=18):
        self.name = name
        self.age = age
        print('构建Person成功')

    def wakeUp(self,level):
        if level>5:
            self.name = 'super.'+self.name
    def grow(self):
        self.age += 1
ps = Person('鸣人')
ps.wakeUp(8)
ps.grow()
print(ps.age)
print(ps.name)