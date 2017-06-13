#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import re


def GetHTML(url):
     try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
 def GetElem(html):
     stock_elem = []
     soup = BeautifulSoup(html, "html.parser")
     elem_num = re.compile(r"\d\d\d\d")
     elem_name = re.compile(r"\w\w\w\w")
     for i in soup.find_all('div', id = "hot-list",string = "elem_name", "elem_num")
        stock_elem.append(i)
        return stock_elem
def PrintElem():
    print("{:^\w\w\w\w}\t{:^\d\d}\t".format("股票名称","热度"))
    for elem in stock_elem:
        print("{:^\w\w\w\w}\t{:^\d\d\d\d}\t".format(elem[0], elem[1]))
    return None

 def main():
    uinfo = []
    url = 'https://xueqiu.com/‘
    html = GetHTML(url)
    GetElem(uinfo, html)
    printUnivList(uinfo, 20) # 20 univs

print html
