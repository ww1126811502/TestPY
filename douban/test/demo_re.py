# -*- coding = utf-8 -*-
# @Time : 2022/4/11 23:11
# @Author : 牧川
# @File : demo_re.py
import re

def main():
    n = 1
    m = 1
    for i in range(0, 20):
        temp = m
        m += n
        n = temp
        say()
        print(m)


def say(myStr) -> object:
    """

    :param myStr: 输入的字符串
    :return: 无返回值
    """
    print("hello")
    print("hi")
    print(myStr)

if __name__ == "__main__":
    main()