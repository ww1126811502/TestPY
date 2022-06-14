# -*- coding = utf-8 -*-
# @Time : 2022/4/9 18:40
# @Author : 牧川
# @File : Genshin.py
import os
import xlwt
import json
#一些转化用的字典
partName = {'flower':'花','feather':'毛','sand':'沙','cup':'杯','head':'头'}
tagName = {'attackStatic':'攻击固定值',
'attackPercentage':'攻击百分比',
'defendStatic':'防御固定值',
'defendPercentage':'防御百分比',
'lifeStatic':'生命固定值',
'lifePercentage':'生命百分比',
'critical':'爆率',
'criticalDamage':'爆伤',
'elementalMastery':'元素精通',
'recharge':'充能效率',
'cureEffect':'治疗加成',
'physicalBonus':'物伤加成',
'fireBonus':'火伤加成',
'thunderBonus':'雷伤加成',
'iceBonus':'冰伤加成',
'waterBonus':'水伤加成',
'windBonus':'风伤加成',
'rockBonus':'岩伤加成'
}

def main():
    path = "artifacts.genshinart.json"
    dict = getData(path)
    # Calculate(dict[0], "花", 40)
    # Calculate(dict[1], "毛", 40)
    # Calculate(dict[2], "沙", 40)
    # Calculate(dict[3], "杯", 40)
    # Calculate(dict[4], "头", 30)
    fdata = filter(dict, 5, 20)
    outExcel(fdata)

def getData(path):
#读入数据，json文件路径需要自己改
    with open(path,'rb') as load_f:
        load_dict = json.load(load_f)
    #按类别装到四个字典列表
    flower_dicts=load_dict['flower']
    feather_dicts=load_dict['feather']
    sand_dicts=load_dict['sand']
    cup_dicts=load_dict['cup']
    head_dicts=load_dict['head']
    alldict =[flower_dicts,feather_dicts,sand_dicts,cup_dicts,head_dicts]
    return alldict
#算分的函数，三个参数依次是圣遗物数据字典、类别名称、分数阈值
def Calculate(artDict,name,value):
    print("大于%d分的%s："%(value,name))
    for n in artDict:
        s = Calculate2(n)
        if s >= value:
            print(s)
#单独算一个圣遗物的分数
def Calculate2(data):
    s = 0
    for a in data['normalTags']:
        if a['name'] == 'criticalDamage':
            s += (a['value'])
        elif a['name'] == 'critical':
            s += (a['value']) * 2
    return round(s*100,2)
#根据条件进行筛选，顺便整理圣遗物属性
def filter(dict, star, level):
    #初始化一些数据：
    global partName
    global tagName
    #准备一个列表，存放圣遗物属性列表
    alldata = []
    i = 0
    #先根据star和level进行筛选，同时整理数据
    #循环五个圣遗物列表
    for list in dict:
        #循环每种圣遗物列表中的每个圣遗物属性字典
        for n in list:
            #对输入的筛选条件进行判断，如果成功则读入数据
            if n['level']>=level and n['star']>=star:
                data = []   #临时列表，用于存储一件圣遗物的所需属性
                data.append(n['detailName'])    #名称
                #套装预留个位置吧，没想到比较合适的搞套装的方法，遇到困难睡大觉.jpg
                data.append(n['setName'])  # 套装
                data.append(partName[n['position']])  # 部位，需要做一步转化
                data.append(n['level'])  # 等级
                data.append(n['star'])  # 星级吧
                data.append(tagName[n['mainTag']['name']])  # 主属性，也转化一次
                data.append(Calculate2(n))  #双暴分数
                #副属性这块，还需要处理两条三条的情况，好麻烦啊
                #前两条固定写入吧先
                data.append(tagName[n['normalTags'][0]['name']])    #属性名做个转换
                data.append(round(n['normalTags'][0]['value'],2))   #属性值取两位
                data.append(tagName[n['normalTags'][1]['name']])
                data.append(round(n['normalTags'][1]['value'], 2))
                if len(n['normalTags']) >=3:
                    data.append(tagName[n['normalTags'][2]['name']])
                    data.append(round(n['normalTags'][2]['value'], 2))
                if len(n['normalTags']) ==4:
                    data.append(tagName[n['normalTags'][3]['name']])
                    data.append(round(n['normalTags'][3]['value'], 2))
                #print('data中的数据:%s'%data[6])
                #全部属性写入后，放入dataall
                alldata.append(data)
                #print('alldata中的数据:%s' % alldata[i][0])
                i+=1
    print("处理成功")
    #将筛选处理后的列表返回
    return alldata
#导出到表格模块
def outExcel(data):
    #先把老表删了
    if os.path.exists('Genshin.xls'):
        os.remove('Genshin.xls')
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建wb对象
    worksheet = workbook.add_sheet('圣遗物信息')  # 创建工作表
    #开始写入表头
    worksheet.write(0, 0, '名称')
    worksheet.write(0, 1, '套装')
    worksheet.write(0, 2, '部位')
    worksheet.write(0, 3, '等级')
    worksheet.write(0, 4, '品质')
    worksheet.write(0, 5, '主属性')
    worksheet.write(0, 6, '双暴分数')
    worksheet.write(0, 7, '副词条1')
    worksheet.write(0, 8, '副词条1数值')
    worksheet.write(0, 9, '副词条2')
    worksheet.write(0, 10, '副词条2数值')
    worksheet.write(0, 11, '副词条3')
    worksheet.write(0, 12, '副词条3数值')
    worksheet.write(0, 13, '副词条4')
    worksheet.write(0, 14, '副词条4数值')
    # 写入圣遗物数据
    for n in range(len(data)):
        for m in range(len(data[n])):
            worksheet.write(n+1, m, "%s" %data[n][m])

    workbook.save('Genshin.xls')  # 进行保存


if __name__ == "__main__":
    main()