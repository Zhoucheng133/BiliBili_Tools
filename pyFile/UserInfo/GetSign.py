import os
import sys
from tkinter import *
import math
import tkinter.messagebox
import re
import requests
def sign(mid):
    uid=str(mid)
    link="http://api.bilibili.com/x/space/acc/info?mid="
    tmp=list(link)
    tmp.append(str(mid))
    # return tmp
    link=''.join(tmp)

    header={
        'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30",
        # 在下面粘贴Cookie!
        # "cookie":
        "mid":uid
    }
    r=requests.get(link,headers=header)
    html=r.text
    # return html
    st:int=html.find("\"sign\"")
    # return st
    i=html.find(",",st+5)
    return (html[st+8:i-1])
    # return (html[st+6:i])
if __name__=="__main__":
    # mid=int(input())
    mid=5129395
    print(sign(mid))
    pass