import os
import sys
from tkinter import *
import math
import tkinter.messagebox
import re
import requests
import time

info=dict()
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
    elif tid==155 or tid==157 or tid==158 or tid==159 or tid==192:
        return "时尚"
    elif tid==202 or tid==203 or tid==204 or tid==205 or tid==206:
        return "资讯"
    elif tid==5 or tid==71 or tid==137 or tid==241:
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
        tkinter.messagebox.showerror("Error","不存在的链接或BV号")
        return "error"
    
def getVideoInfo(link:str):
    bv=switch(link)
    if(bv=="error"):
        return "error"
    link="http://api.bilibili.com/x/web-interface/view"

    header={
        'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30",
        # 在下面粘贴Cookie!
        # "cookie":
        "bvid":bv
    }
    r=requests.get(link,headers=header)
    html=r.text

    # 播放量
    st:int=html.find("\"view\"")
    i=html.find(",",st+6)
    info["bf"]=html[st+7:i]

    # 硬币数
    st:int=html.find("\"coin\"")
    i=html.find(",",st+6)
    info["coin"]=html[st+7:i]

    # 弹幕数
    st:int=html.find("danmaku\"")
    i=html.find(",",st+9)
    info["dm"]=(html[st+9:i])

    # 收藏数
    st:int=html.find("\"favorite\"")
    i=html.find(",",st+11)
    info["fav"]= (html[st+11:i])

    # 点赞数
    st:int=html.find("\"like\"")
    i=html.find(",",st+7)
    info["like"]= (html[st+7:i])

    # 用户id
    st:int=html.find("\"mid\"")
    i=html.find(",",st+5)
    info["uid"]= (html[st+6:i])

    # 视频封面
    st:int=html.find("\"pic\"")
    i=html.find(",",st+5)
    info["pic"]=html[st+7:i-1]

    # 回复数
    st:int=html.find("\"reply\"")
    i=html.find(",",st+8)
    info["reply"]=(html[st+8:i])

    # 分区
    st:int=html.find("\"tid\"")
    i=html.find(",",st+5)
    info["tid"]=TidManage(eval(html[st+6:i]))

    # 时长
    st:int=html.find("\"duration\"")
    i=html.find(",",st+10)
    t=eval(html[st+11:i])
    if t<60:
        info["time"]=str(t)+"s"
    else:
        info["time"]=str(int(t/60))+" min "+str(int(t%60))+" s"

    # 标题
    st:int=html.find("title\"")
    i=html.find(",",st+8)
    info["title"]=(html[st+8:i-1])

    # up主名称
    st:int=html.find("\"name\"")
    i=html.find(",",st+6)
    info["up"] =(html[st+8:i-1])

    # bv号
    st:int=html.find("\"name\"")

    # 以秒记数时长
    st:int=html.find("\"duration\"")
    i=html.find(",",st+10)
    info["stime"]=eval(html[st+11:i])

    # time.sleep(0.1)

    return info

if __name__=="__main__":
    print(getVideoInfo("BV1HL411M7z9"))