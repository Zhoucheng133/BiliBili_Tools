import os
import sys
from tkinter import *
import math
import tkinter.messagebox
import re
import requests


def Vsearch(kw):
    
    rlt=[]
    link="http://api.bilibili.com/x/web-interface/search/all/v2?keyword=\""
    # link="http://api.bilibili.com/x/web-interface/search/all/v2"

    tmp=list(link)
    tmp.append(kw)
    tmp.append("\"")
    # return tmp
    link=''.join(tmp)

    header={
        'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30",
        # 在下面粘贴Cookie!
        # "cookie":
    }
    r=requests.get(link,headers=header)
    html=r.text
    # return html
    st=html.find("bvid")
    while(st!=-1):
        i=html.find(",",st)
        rlt.append(html[st+7:i-1])
        st=i
        st=html.find("bvid",st)
    return rlt
    
if __name__=="__main__":
    kw=input()
    print(Vsearch(kw))
    pass