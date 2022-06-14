from flask import Flask,render_template
import sqlite3
import jieba                            #分词
from wordcloud import WordCloud         #词云
from matplotlib import pyplot as plt    #绘图
from PIL import Image                   #图片处理
import numpy as np                      #矩阵运算

app = Flask(__name__)

#主页
@app.route('/')
def mainPage():  # put application's code here
    return render_template('index.html')

@app.route('/index.html')
def mainPage2():  # put application's code here
    return mainPage()
#电影信息列表
@app.route('/movie.html')
def movie():  # put application's code here
    movielist = []
    #从数据库取出数据
    conn = sqlite3.connect('movie.db')
    cur = conn.cursor()
    sql = "select * from movie250"
    #将游标数据取到列表里，但是此处的data数据直接来自游标，会因为游标的关闭而失去数据
    data = cur.execute(sql)
    #将data数据存到准备好的列表里
    for item in data:
        movielist.append(item)
    cur.close()
    conn.close()
    return render_template('movie.html',movies = movielist)
#电影评分
@app.route('/rating.html')
def rating():  # put application's code here
    score = []  #存储分数
    num = []    #存储分数对应的电影数
    # 从数据库取出数据
    conn = sqlite3.connect('movie.db')
    cur = conn.cursor()
    #从数据库中取出分数、每个分数的数量，以分数为依据分组
    sql = "select score,count(score) from movie250 group by score "
    data = cur.execute(sql)
    # 将data数据存到准备好的列表里
    for item in data:
        score.append(item[0])
        num.append(item[1])
    cur.close()
    conn.close()

    return render_template('rating.html',score = score,num = num)
#词云
@app.route('/wordcloud.html')
def wordcloud():  # put application's code here
    conn = sqlite3.connect('movie.db')
    cur=conn.cursor()
    sql='select instr from movie250'
    res = cur.execute(sql)
    text = ''
    for i in res:
        text = text +i[0]
    cur.close()
    conn.close()
    str = jieba.cut(text)
    str = ' '.join(str)
    img= Image.open('static/assets/img/bg-img.jpg')
    imgArry = np.array(img)
    wc = WordCloud(
        background_color='white',  # 生成后图片的背景色
        mask=imgArry,  # 转换后的数组
        font_path='C:\Windows\Fonts\msyh.ttc',  # 字体，加ttf后缀，位置在c:\window\fonts
        max_font_size=150,  # 设置字体最大值
        random_state=30  # 设置有多少种随机生成状态，即有多少种配色方案
    ).generate_from_text(str)
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.show()
    plt.savefig('static/assets/img/word.jpg', dpi=500)

    return render_template('wordcloud.html')
#团队
@app.route('/team.html')
def team():  # put application's code here
    return render_template('team.html')

if __name__ == '__main__':
    app.run()
