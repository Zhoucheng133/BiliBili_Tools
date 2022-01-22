import os
import sys
from tkinter import *
import math
import tkinter.messagebox
import re
import requests
import time

info=dict()

def GetUserInfo(mid):
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
    # 等级
    st:int=html.find("\"level\"")
    i=html.find(",",st+7)
    info["level"]=(html[st+8:i])
    # 姓名
    st:int=html.find("\"name\"")
    i=html.find(",",st+6)
    info["name"]= (html[st+8:i-1])
    # 性别
    st:int=html.find("\"sex\"")
    i=html.find(",",st+4)
    info["sex"]= (html[st+7:i-1])
    # 个性签名
    st:int=html.find("\"sign\"")
    i=html.find(",",st+5)
    info["sign"]= (html[st+8:i-1])
    # 头像
    st:int=html.find("\"face\"")
    i=html.find(",",st+7)
    info["face"]=(html[st+8:i])

    time.sleep(0.1)
    return info
if __name__=="__main__":
    print(GetUserInfo(5129395))