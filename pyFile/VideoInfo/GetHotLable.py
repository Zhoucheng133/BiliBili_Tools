# 模块-热点
import os
import sys
from tkinter import *
import math
import tkinter.messagebox
import re
import requests
import json

def hot():
    link="https://api.bilibili.com/x/web-interface/popular"
    header={
        'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30",
        "Accept":"*/*",
        # "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":	"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Host":"api.bilibili.com",
        "Origin":"https://www.bilibili.com",
        "Referer":"https://www.bilibili.com/",
        "Sec-Fetch-Dest":"empty",
        "Sec-Fetch-Mode":"cors",
        "Sec-Fetch-Site":"same-site",
        "TE":"trailers",
        # 在下面粘贴Cookie!
        # "cookie":
    }
    r=requests.get(link,headers=header)
    html=r.text
    lst:list=[]
    # return html
    while html.find("short_link\"")!=-1:
        st:int=html.find("short_link\"")
        st+=13
        i=st
        title=''
        while html[i]!="\"":
            i+=1
        title=html[st:i]
        lst.append(title)
        html=html[i:]
    return lst


if __name__=="__main__":
    l=(hot())
    for i in l:
        print(i)
    # print(l)