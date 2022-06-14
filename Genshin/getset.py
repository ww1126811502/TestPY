# -*- coding = utf-8 -*-
# @Time : 2022/4/22 18:43
# @Author : 牧川
# @File : getset.py

import urllib.request
import urllib.parse
import requests

response = requests.get("https://hk4e-api.mihoyo.com/event/simulator/reliquary?gids=2").json()
str = response['data']
str = str['select_item']
for i in range(len(str)):
    print(i)
    print(str[1]['name'])
