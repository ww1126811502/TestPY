# -*- coding = utf-8 -*-
# @Time : 2022/6/15 12:51
# @Author : 牧川
# @File : demo_class_09.py
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        print("访问了name属性")
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        print("访问了age属性")
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        print("修改了age属性")
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    print(f"大锤的年龄是：{person.age}")
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()