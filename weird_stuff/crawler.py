# 專題實作做這題得 80分

from os.path import exists

from urllib.request import urlopen

import bs4

from bs4 import BeautifulSoup # pip install bs4 or pip install BeautifulSoup4

from time import localtime, strftime

import csv

myweb = urlopen("https://zh.wikipedia.org/wiki/%E6%A1%83%E5%9C%92%E5%B8%82%E7%AB%8B%E6%AD%A6%E9%99%B5%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1")

myObj = BeautifulSoup(myweb, "html.parser") # 讀取 HTML 原始碼進行解析 (解析器：lxml、html5lib、html.parser)

order = myObj.find("span", {"class":"mw-headline"}).contents[0]

for i in myObj.find("table", {"class":"wikitable"}).find("tbody").findAll("tr"):

    

    if i.find("th"):

        cell = i.findAll("th")

        mining_txt = cell[0].contents[0]

        mining_name = cell[1].contents[0]

        mining_txt_add = cell[4].contents[0]

        mining_txt_add = mining_txt_add.replace("\n", "")

    else:

        cell_y = i.findAll("td")

        mining_txt_y1 = cell_y[0].contents[0]

        mining_txt_n1 = cell_y[1].contents[0]

        mining_txt_add1 = cell_y[4].text

        if type(mining_txt_n1) is bs4.element.Tag:

            mining_txt_n1 = mining_txt_n1.text.split('›')[-1].replace(' ','')

        

        mining_txt_n1 = mining_txt_n1.replace("\r","")

        mining_txt_n1 = mining_txt_n1.replace("\n","")

        mining_txt_n1 = mining_txt_n1.replace(" ","")

        mining_txt_add1 = mining_txt_add1.replace("\n", "")

        mining_txt_add1 = mining_txt_add1.replace("\"", "")

        print(mining_txt + ":" + mining_txt_y1, mining_name + ":" + mining_txt_n1, sep =',', end ='\n')

        f_name = "mining_table.csv"

        now_time = strftime("%Y-%m-%d %H:%M:%S", localtime())

        if not exists(f_name):     # store to webmining.csv

            mydata = [['當前時間', 'th + td 標籤', '去除a標籤'], [now_time, mining_txt + ":" + mining_txt_y1, mining_name + ":" + mining_txt_n1, mining_txt_add + ":" + mining_txt_add1]]

        else:

            mydata = [[now_time, mining_txt + ":" + mining_txt_y1, mining_name + ":" + mining_txt_n1, mining_txt_add + ":" + mining_txt_add1]]

        fn = open(f_name, "a",  encoding="utf-8") # add 在文件的結尾

        wit = csv.writer(fn)

        wit.writerows(mydata)

        fn.close()