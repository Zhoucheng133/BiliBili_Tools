# 视频标题
import os
import sys
from tkinter import *
import math
import tkinter.messagebox
import re
import requests

def switch(s:str):
    if s.startswith("BV") or s.startswith("bv"):
        return s
    elif s.startswith("http") or s.startswith("www"):
        i:int=s.find("BV")
        o:int=s.find("?",i)
        p:int=s.find("/",i)
        if o==-1 and p==-1:
            s=s[i:]
        else:
            if o>p and p!=-1:
                s=s[i:p]
            elif p<=o and o!=-1:
                s=s[i:o]
        return s
    else:
        return error

def title(link:str):
    bv=switch(link)
    link="http://api.bilibili.com/x/web-interface/view"

    header={
        'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30",
        # 在下面粘贴Cookie!
        # "cookie":
        "bvid":bv
    }
    r=requests.get(link,headers=header)
    html=r.text
    # return html
    st:int=html.find("title\"")
    # return st
    i=html.find(",",st+8)
    return (html[st+8:i-1])



if __name__=="__main__":
    print(title("BV1Pp4y1b7GZ"))