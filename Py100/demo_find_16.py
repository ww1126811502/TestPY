# -*- coding = utf-8 -*-
# @Time : 2022/6/19 0:02
# @Author : 牧川
# @File : demo_find_16.py

def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]
    #从第一位开始查找
    for i in range(len(items) - 1):
        min_index = i
        #对比之后的数，通过不断换位，保证i为最小
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def bubble_sort(items, comp=lambda x, y: x > y):
    """冒泡排序"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                print(f"将第{j}位与第{j+1}位互换")
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        print(f"一轮完成,当前i = {i}")
        if not swapped:
            break
    return items


print(bubble_sort([27, 5, 9, 16, 7, 23]))
