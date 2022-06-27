# -*- coding = utf-8 -*-
# @Time : 2022/6/25 18:18
# @Author : 牧川
# @File : demo_wrap_16.py
from functools import wraps


def MyWrap(func):
    """一个没有参数的修饰器"""
    @wraps(func)
    def WarpFun():
        print(f"hi，修饰器生效了运行的函数是：{func.__name__}")
        func()
        print("hi,函数执行完了")

    return WarpFun


def MyWrap2(func):
    """函数带参数修饰器"""
    #wrap接受一个函数，使我们可以访问被修饰前的函数
    @wraps(func)
    def WarpFun(*args, **kwargs):
        print(f"hi，修饰器生效了，运行的函数是：{func.__name__}")
        func(*args, **kwargs)
        print("hi,函数执行完了")

    return WarpFun


def myArgWrap(type1 = "none"):
    def myWrap3(func):
        def warpFun(*args, **kwargs):
            print(f"hi,修饰的函数类型为：{type1},函数名：{func.__name__}")
            return func(*args, **kwargs)
        return warpFun
    return myWrap3


@MyWrap
def MyFunction():
    print("这里面是函数内容")


@MyWrap2
def FuncTest(name):
    print(f"name is {name}")


@myArgWrap(type1= "public")
def FuncTest2(name):
    print(f"name is {name}")


MyFunction()
FuncTest("张三")
FuncTest2("李四")


