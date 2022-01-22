# 视频分区
import os
import sys
from tkinter import *
import math
import tkinter.messagebox
import re
import requests
from GetHotLable import hot
def TidManage(tid:int):
    if tid==1 or tid==24 or tid==25 or tid==47 or tid==210 or tid==86 or tid==27:
        return "动画"
    elif tid==13 or tid==33 or tid==32 or tid==51 or tid==152:
        return "番剧"
    elif tid==167 or tid==153 or tid==168 or tid==169 or tid==195 or tid==170:
        return "国创"
    elif tid==3 or tid==28 or tid==31 or tid==30 or tid==194 or tid==59 or tid==193 or tid==29 or tid==130:
        return "音乐"
    elif tid==129 or tid==20 or tid==198 or tid==199 or tid==200 or tid==154 or tid==156:
        return "舞蹈"
    elif tid==4 or tid==17 or tid==171 or tid==172 or tid==65 or tid==173 or tid==121 or tid==136 or tid==19:
        return "游戏"
    elif tid==36 or tid==201 or tid==124 or tid==228 or tid==207 or tid==208 or tid==209 or tid==229 or tid==122:
        return "知识"
    elif tid==188 or tid==95 or tid==230 or tid==231 or tid==232 or tid==233:
        return "科技"
    elif tid==234 or tid==235 or tid==164 or tid==236 or tid==237 or tid==238:
        return "运动"
    elif tid==233 or tid==176 or tid==224 or tid==225 or tid==226 or tid==227:
        return "汽车"
    elif tid==160 or tid==138 or tid==239 or tid==161 or tid==162 or tid==21:
        return "生活"
    elif tid==211 or tid==76 or tid==212 or tid==213 or tid==214 or tid==215:
        return "美食"
    elif tid==217 or tid==218 or tid==219 or tid==220 or tid==221 or tid==222 or tid==75:
        return "动物圈"
    elif tid==119 or tid==22 or tid==26 or tid==126 or tid==216 or tid==127:
        return "鬼畜"
    elif tid==155 or tid==157 or tid==158 or tid==159 or tid==192 or tid==242:
        return "时尚"
    elif tid==202 or tid==203 or tid==204 or tid==205 or tid==206:
        return "资讯"
    elif tid==5 or tid==71 or tid==137:
        return "娱乐"
    elif tid==182 or tid==182 or tid==183 or tid==85 or tid==184:
        return "影视"
    elif tid==177 or tid==37 or tid==178 or tid==179 or tid==180:
        return "纪录片"
    elif tid==23 or tid==147 or tid==145 or tid==146 or tid==83:
        return "电影"
    elif tid==11 or tid==185 or tid==187:
        return "电视剧"
    else:
        return "没找到该分区"

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
        
def tid(link:str):
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
    st:int=html.find("\"tid\"")
    # return st
    i=html.find(",",st+5)
    return TidManage(eval(html[st+6:i]))
    # return (html[st+6:i])


if __name__=="__main__":
    hots=hot()
    for i in hots:
        print(tid(i))