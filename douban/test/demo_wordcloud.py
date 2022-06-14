# -*- coding = utf-8 -*-
# @Time : 2022/4/21 21:18
# @Author : 牧川
# @File : demo_wordcloud.py
import jieba                            #分词
from wordcloud import WordCloud         #词云
from matplotlib import pyplot as plt    #绘图
from PIL import Image                   #图片处理
import numpy as np                      #矩阵运算
import sqlite3

def main():
    text = getStr()
    #直接用jieba库进行分词，返回值为对象，无法直接打印
    #返回的结构都是一个可迭代的generator
    # 可以使用for循环来获得得到的每一个词语，也可以用list(jieba.cut(...))转化为list
    cut = jieba.cut(text)
    #可以用join方法连成一整个字符串来打印或作为字符串输入
    str =' '.join(cut)
    str = str.replace('的','')
    #print(str)
    img = getImg()
    wc = getWC(str,img)
    printImg(wc)

#打开图片，并将其转化为图片数组
def getImg():
    img = Image.open('background.jpg')
    #numpyd的array方法，可以将图片转化为数组
    img_arry = np.array(img)
    return img_arry
#从数据库里面把所有的字符串拿出来
def getStr():
    conn = sqlite3.connect('F:\MyPython\douban\movie.db')
    cur = conn.cursor()
    sql = 'select instr from movie250'
    str = cur.execute(sql)
    text = ''
    #返回值为二维列表str，所以其中的每一个项目i也还是列表，需要用i[0]取出
    for i in str:
        #print(i)
        text = text +i[0]
    #text = text.replace(' ','')
    cur.close()
    conn.close()
    #print(text)
    return text
#设置wc对象的格式和内容
def getWC(cut,img):
    # 声明一个wc对象，先设定好格式属性
    wc = WordCloud(
        background_color='white',  # 生成后图片的背景色
        mask=img,  # 转换后的数组
        font_path='C:\Windows\Fonts\msyh.ttc',  # 字体，加ttf后缀，位置在c:\window\fonts
        max_font_size=150,  # 设置字体最大值
        random_state=30  # 设置有多少种随机生成状态，即有多少种配色方案
    )
    # jieba切好的词放进去
    wc.generate_from_text(cut)
    return wc

#图像绘制
def printImg(wc):
    fig = plt.figure(1) #1代表在第一个位置绘制
    plt.imshow(wc)  #按照wc的规则进行绘制
    plt.axis('off') #设置不显示坐标轴
    #设置完成后，用show方法显示
    #plt.show()
    #输出图片到文件
    plt.savefig('word.jpg',dpi=500)

if __name__ == '__main__':
    main()
