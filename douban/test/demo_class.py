# -*- coding = utf-8 -*-
# @Time : 2022/6/11 17:55
# @Author : 牧川
# @File : demo_class.py


class Data:

    instance = None

    def __init__(self):
        print("一个无入参的Data被创建")

    def __new__(cls, *args, **kwargs):
        print("调用new函数")
        #如果单例尚未初始化，使用super.new；否则直接返回instance
        if cls.instance is None:
            cls.instance = super.__new__(cls)

        return cls.instance


data = Data()
