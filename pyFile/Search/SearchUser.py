import os
import sys
from tkinter import *
import math
import tkinter.messagebox
import re
import requests

rlt=[]

def Usearch(kw):
    link="http://api.bilibili.com/x/web-interface/search/type?search_type=bili_user&keyword=\""

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
    rlt=[]
    st=html.find("uname")
    while(st!=-1):
        i=html.find(",",st)
        rlt.append(html[st+8:i-1])
        st=i
        st=html.find("uname",st)
    Names=rlt[::2]
    # print(Names)
    rlt=[]
    st=html.find("mid")
    while(st!=-1):
        i=html.find(",",st)
        rlt.append(html[st+5:i])
        st=i
        st=html.find("mid",st)
    IDs=rlt
    # print(IDs)
    return dict(zip(Names, IDs))
    
if __name__=="__main__":
    kw=input()
    print(Usearch(kw))
    # Usearch(kw)
    pass