# -*- coding = utf-8 -*-
# @Time : 2022/6/17 16:32
# @Author : 牧川
# @File : demo_PIL_15.py

from PIL import Image

image = Image.open('./res/guido.jpg')

rect = 80, 20, 310, 360
#用一个矩形对img进行裁剪
img2 = image.crop(rect)
img2.show()