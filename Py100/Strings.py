# -*- coding = utf-8 -*-
# @Time : 2022/6/15 0:42
# @Author : 牧川
# @File : Strings.py
import sys

def Mygenexpr():
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567'] #相当于一个二重嵌套，A1...A7,B1...B7....
    print(f)
    #使用生成式（即[]）
    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    print(f)
    #使用生成器（即（））
    f = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
    print(f)    #此处输出为genexpr对象，只有在遍历调用时，才会实际赋值
    for val in f:
        print(val)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()