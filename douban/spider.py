# -*- coding = utf-8 -*-
# @Time : 2022/4/10 18:12
# @Author : 牧川
# @File : spider.py
import sys
import re
from bs4 import BeautifulSoup
import urllib.request,urllib.error
import xlwt
import sqlite3

def main():
    baseUrl = "https://movie.douban.com/top250?start="
    #爬取网页
    dataList = getData(baseUrl)
    savePath = ".\\豆瓣电影top250.xls"
    dbpath = "movie.db"
    # 保存数据到excel
    #saveData(dataList,savePath)
    #保存数据到数据库：
    saveDB(dataList,dbpath)

#定义一些全局变量
findlink = re.compile(r'<a href="(.*?)">')
findImgSrc = re.compile(r'src="(.*?)"',re.S)    #忽略换行
findname = re.compile(r'<span class="title">(.*)</span>')
findrating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findjudge = re.compile(r'<span>(\d*)人评价</span>')
findinq = re.compile(r'<span class="inq">(.*)</span>')
findbd = re.compile(r'<p class="">(.*?)</p>',re.S)

def getData(baseURL):
    dataList = []
    #逐一获取网页源码html
    for i in range(0,10):
        url = baseURL+str(i*25)
        #print(url)
        html = askURL(url)  #获取到源码
    #将获取的网页源码进行解析：
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_='item'):
            #print(item)
            data = []   #用于保存一部电影中的所需信息
            item = str(item)

            link = re.findall(findlink,item)[0]
            data.append(link)

            img = re.findall(findImgSrc,item)[0]
            data.append(img)

            name = re.findall(findname, item)
            if len(name) == 2:
                cname = name[0]
                data.append(cname)
                oname = name[1].replace("/","")
                data.append(oname)
            else:
                data.append(name[0])
                data.append(' ')

            rating = re.findall(findrating, item)[0]
            data.append(rating)

            judge = re.findall(findjudge, item)[0]
            data.append(judge)

            inq = re.findall(findinq, item)
            if len(inq) == 0:
                data.append(' ')
            else:
                data.append(inq[0].replace("。",""))

            bd = re.findall(findbd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?','',bd)
            bd = re.sub('/','',bd)
            data.append(bd.strip())     #去掉空格

            dataList.append(data)
    #print(dataList)
    return dataList

#获取单一网页信息
def askURL(url):
    #将UA信息放进head，包成一个request
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
    req = urllib.request.Request(url=url,headers=head)
    html = ""
    try:
        #使用包好的request进行访问，并保存返回的response
        resp = urllib.request.urlopen(req)
        html = resp.read().decode('utf-8')
        #print("访问链接：%s成功" % url)
        # with open("douban.html","wb") as f:
        #     f.write(bytes(html,encoding='utf-8'))
    except Exception as e:
        print("访问链接：%s失败，错误类型:%s"%(url,e))
    return html
#保存数据到表格
def saveData(dataList,savePath):
    book = xlwt.Workbook(encoding='utf-8',style_compression=0)  # 创建wb对象
    sheet = book.add_sheet('电影信息',cell_overwrite_ok=True)  # 创建工作表
    col = ("电影链接","图片链接","中文名","外文名","评分","评价数","概况","相关信息")
    #写入表头
    for i in range(0,8):
        sheet.write(0,i,col[i])
    #写入数据：
    for i in range(0,250):
        print("写入第%d条数据成功"%i)
        data = dataList[i]
        for j in range(0, 8):
            sheet.write(i+1,j, data[j])
    book.save(savePath)  # 进行保存
#保存数据到数据库
def saveDB(dataList,dbPath):
    sql = ""
    #初始化数据库
    init_db(dbPath)
    #连接数据库，并实例化一个游标单位
    conn = sqlite3.connect(dbPath)
    cur = conn.cursor()
    #写入每一行数据：
    for data in dataList:
        # 给原数据加上双引号
        for i in range(len(data)):
            data[i] = '"'+data[i]+'"'
        #下面重点，书写sql语句的时候，如果需要传参进去，可以先用占位符，在引号外面加内容
        sql = '''
        insert into movie250(
        info_link,pic_link,cname,ename,score,rated,instr,info)
        values (%s)
        '''%",".join(data)
        #每一条均执行一次sql语句，并提交
        #print(sql)
        cur.execute(sql)
        conn.commit()
        print("成功写入一条数据")
    cur.close()
    conn.close()
    print("成功")

def init_db(dbpath):
    #创建数据表
    sql = '''
        create table if not exists movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar ,
        ename varchar ,
        score numeric ,
        rated numeric ,
        instr text,
        info text
        );
    '''
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute(sql)
    #保存并关闭
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #main()
    #askURL("https://movie.douban.com/top250?start=25")
    #getData("https://movie.douban.com/top250?start=")
    #saveData(".\\豆瓣电影top250.xls")
    #init_db("test.db")
    main()