import os
import sys
from tkinter import *
import math
import time
import io
import tkinter.messagebox
from pyFile.Hot.GetHotLable import hot
from pyFile.VideoInfo._GetVideoInfo import *
from pyFile.UserInfo._GetUserInfo import *
from pyFile.Search.SearchUser import Usearch
from pyFile.Search.SearchVideo import Vsearch
from PIL import Image,ImageTk
from urllib.request import urlopen
import webbrowser
import numpy as np
import scipy
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from pyFile.Download.Download import download
import platform
import threading

# 热门的界面
hotpicbn=["","","",""]
hotimg=["","","",""]

hottitle=["","","",""]
hottitlelabel=["","","",""]

hotbf=["","","",""]
hotbflabel=["","","",""]

hotup=["","","",""]
hotuplabel=["","","",""]

hotbv=["","","",""]

image_bytes=["","","",""]
data_stream=["","","",""]
pil_image=["","","",""]
tk_image=["","","",""]

TidStaticImg=None
TidStaticBt=None
TimeStaticImg=None
TimeStaticBt=None

# 下载的界面
OpenFileImg=None
OpenFileBt=None

# 搜索界面
VsearchE=None
VsearchImg=None
VsearchBt=None


ToE=None
ToImag=None
ToBt=None

# 视频详情界面
VimgLabel=None
VTLabel=None
VallInfo=None
opInbBt=None
dlvBt=None

# 用户详情界面


# 视频搜索结果页面
Vrlttitlelabel=["","","",""]
Vrlttitle=["","","",""]
Vrltuplabel=["","","",""]
Vrltbf=["","","",""]
Vrltbflabel=["","","",""]
Vrltimage_bytes=["","","",""]
Vrlttk_image=["","","",""]
Vrltpil_image=["","","",""]
Vrltdata_stream=["","","",""]
Vrltimg=["","","",""]
Vrltpicbn=["","","",""]
Vrltup=["","","",""]


# 用户搜索结果界面
# 放弃制作

# 用户详情页
# 放弃制作
'''
position:
0.没有显示任何东西
1.下载
2.热门
3.搜索
4.视频详情页
5.视频搜索结果页

bv:
bv号，默认为空
'''
# 其它参数
position:int=0
bv=None
    
def showInfo():
    tkinter.messagebox.showinfo("提示","")

def showError():
    tkinter.messagebox.showerror("警告","")

def get_image(filename,width,height):
    im=Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(im)

# 热门界面
def hotbt():
    global position
    # 热门的全局变量
    global TidStaticImg
    global TidStaticBt
    global TimeStaticImg
    global TimeStaticBt

    # 下载的全局变量
    global OpenFileBt
    global OpenFileImg
    
    # 搜索的全局变量
    global VsearchE
    global VsearchImg
    global VsearchBt


    global ToE
    global ToImag
    global ToBt

    # 视频详情页的全局变量
    global VimgLabel
    global VTLabel
    global VallInfo
    global opInbBt
    global dlvBt

    if position==2:
        return
    elif position==1:
        OpenFileBt.place_forget()
    elif position==3:
        VsearchE.place_forget()
        VsearchBt.place_forget()
        ToE.place_forget()
        ToBt.place_forget()
    elif position==4:
        VimgLabel.place_forget()
        VTLabel.place_forget()
        VallInfo.place_forget()
        opInbBt.place_forget()
        dlvBt.place_forget()
    elif position==5:
        for i in range(0,4):
            Vrlttitlelabel[i].place_forget()
            Vrltuplabel[i].place_forget()
            Vrltbflabel[i].place_forget()
            Vrltpicbn[i].place_forget()

    # 热点界面
    hots=hot()
    for i in range(0,4):
        hotdc=getVideoInfo(hots[i])
        
        hotimg[i]=(hotdc["pic"])
        hottitle[i]=(hotdc["title"])
        hotup[i]=(hotdc["up"])
        hotbf[i]=(hotdc["bf"])

        # picurl=hotimg[i]

        # image_bytes .append( urlopen(picurl).read())
        # data_stream .append( io.BytesIO(image_bytes[i]))
        # pil_image .append(Image.open(data_stream[i]))
        # pil_image[i]=pil_image[i].resize((130,80))
        # tk_image.append(ImageTk.PhotoImage(pil_image[i]))

        
        # hotpicbn.append(tkinter.Button(root,image=tk_image[i]))
        # hotpicbn[i].image=tk_image[i]
        # hotpicbn[i].place(x=20,y=120+100*i)

        hottitlelabel[i]=(tkinter.Label(text=hottitle[i],bg="white",wraplength=200,justify="left"))
        # hottitlelabel[i].place_forget()
        hottitlelabel[i].place(x=180,y=120+100*i)

        hotuplabel[i]=(tkinter.Label(text="up主: "+hotup[i],bg="white"))
        # hotuplabel[i].place_forget
        hotuplabel[i].place(x=180,y=160+100*i)

        hotbflabel[i]=(tkinter.Label(text="播放: "+hotbf[i],bg="white"))
        # hotuplabel[i].place_forget
        hotbflabel[i].place(x=180,y=180+100*i)

    TidStaticImg=get_image("img/Buttons/Tids.png", 100, 50)
    TidStaticBt=tkinter.Button(root,image=TidStaticImg,command=lambda:(Func1(hots)))
    # TidStaticBt.place_forget
    TidStaticBt.image=TidStaticImg
    TidStaticBt.place(x=50,y=520)

    TimeStaticImg=get_image("img/Buttons/Time.png", 100, 50)
    TimeStaticBt=tkinter.Button(root,image=TimeStaticImg,command=lambda:(Func2(hots)))
    # TidStaticBt.place_forget
    TimeStaticBt.image=TimeStaticImg
    TimeStaticBt.place(x=250,y=520)

    # 测试：
    picurl=hotimg[0]
    # 按钮1
    image_bytes [0]=( urlopen(picurl).read())
    data_stream [0]=( io.BytesIO(image_bytes[0]))
    pil_image [0]=(Image.open(data_stream[0]))
    pil_image[0]=pil_image[0].resize((130,80))
    tk_image[0]=(ImageTk.PhotoImage(pil_image[0]))

    hotpicbn[0]=(tkinter.Button(root,image=tk_image[0],command=lambda:VInfo(hots[0])))
    hotpicbn[0].image=tk_image[0]
    hotpicbn[0].place(x=20,y=120+100*0)

    # 按钮2
    picurl=hotimg[1]

    image_bytes [1]=( urlopen(picurl).read())
    data_stream [1]=( io.BytesIO(image_bytes[1]))
    pil_image [1]=(Image.open(data_stream[1]))
    pil_image[1]=pil_image[1].resize((130,80))
    tk_image[1]=(ImageTk.PhotoImage(pil_image[1]))

    hotpicbn[1]=(tkinter.Button(root,image=tk_image[1],command=lambda:VInfo(hots[1])))
    hotpicbn[1].image=tk_image[1]
    hotpicbn[1].place(x=20,y=120+100*1)

    # 按钮3
    picurl=hotimg[2]

    image_bytes[2]=( urlopen(picurl).read())
    data_stream [2]=( io.BytesIO(image_bytes[2]))
    pil_image [2]=(Image.open(data_stream[2]))
    pil_image[2]=pil_image[2].resize((130,80))
    tk_image[2]=(ImageTk.PhotoImage(pil_image[2]))

    hotpicbn[2]=(tkinter.Button(root,image=tk_image[2],command=lambda:VInfo(hots[2])))
    hotpicbn[2].image=tk_image[2]
    hotpicbn[2].place(x=20,y=120+100*2)

    # 按钮4
    picurl=hotimg[3]

    image_bytes [3]=( urlopen(picurl).read())
    data_stream[3]=( io.BytesIO(image_bytes[3]))
    pil_image[3]=(Image.open(data_stream[3]))
    pil_image[3]=pil_image[3].resize((130,80))
    tk_image[3]=(ImageTk.PhotoImage(pil_image[3]))

    hotpicbn[3]=(tkinter.Button(root,image=tk_image[3],command=lambda:VInfo(hots[3])))
    hotpicbn[3].image=tk_image[3]
    hotpicbn[3].place(x=20,y=120+100*3)
    

    position=2

# 按照分区统计
def Func1(lst:list):
    tids=[]
    for i in lst:
        dc=dict(getVideoInfo(i))
        tids.append(dc["tid"])
    para=set(tids)
    tst=dict()
    for i in tids:
        if i not in tst:
            tst[i]=1
        else:
            tst[i]+=1
    x=[]
    y=[]
    for keys in tst.keys():
        x.append(keys)
    for values in tst.values():
        y.append(values)

    fig, ax = plt.subplots(figsize=(10, 7))
    fig.canvas.manager.set_window_title('热搜榜按照分区分布图')
    ax.bar(
        x=x,
        height=y,
        color="gray",
        edgecolor="red"
    )
    xticks = ax.get_xticks()
    for i in range(len(y)):
        xy = (xticks[i], y[i] * 1.03)
        s = str(y[i])
        ax.annotate(
            text=s,  # 要添加的文本
            xy=xy,  # 将文本添加到哪个位置
            fontsize=12,  # 标签大小
            color="blue",  # 标签颜色
            ha="center",  # 水平对齐
            va="baseline"  # 垂直对齐
        )
    myfont = fm.FontProperties(fname=r'Font/奶酪陷阱体.ttf')
    plt.xticks(x, x, fontproperties=myfont, fontsize=15)
    plt.yticks(y, y, fontproperties=myfont, fontsize=15)
    # ax.Label(fontproperties=myfont)
    ax.set_title("热搜榜按照分区分布", fontproperties=myfont,fontsize=15)
    plt.show()

# 按照时长统计
def Func2(lst:list):
    length=[]
    for i in lst:
        dc=dict(getVideoInfo(i))
        length.append(dc["stime"])
    x = ["<30 s", "30 s~1 min", "1 min~2 min", "2 min~5 min", "5 min~10 min", "10 min~30 min", ">30 min"]
    y = [0,0,0,0,0,0,0]

    # length=[12,43,64,52,65,12,65,62,765,142,536,1242,456,235,4567]

    for i in length:
        if i<30:
            y[0]+=1
        elif i>=30 and i<60:
            y[1]+=1
        elif i>=60 and i<120:
            y[2]+=1
        elif i>=120 and i<300:
            y[3]+=1
        elif i>=300 and i<600:
            y[4]+=1
        elif i>=600 and i<1800:
            y[5]+=1
        elif i>=1800:
            y[6]+=1
    
    fig, ax = plt.subplots(figsize=(10, 7))
    fig.canvas.manager.set_window_title('热搜榜按照时长分布图')
    ax.bar(
        x=x,
        height=y,
        color="gray",
        edgecolor="red"
    )
    xticks = ax.get_xticks()
    for i in range(len(y)):
        xy = (xticks[i], y[i] * 1.03)
        s = str(y[i])
        ax.annotate(
            text=s,  # 要添加的文本
            xy=xy,  # 将文本添加到哪个位置
            fontsize=12,  # 标签大小
            color="blue",  # 标签颜色
            ha="center",  # 水平对齐
            va="baseline"  # 垂直对齐
        )
    myfont = fm.FontProperties(fname=r'Font/奶酪陷阱体.ttf')
    plt.xticks(x, x, fontproperties=myfont, fontsize=15)
    plt.yticks(y, y, fontproperties=myfont, fontsize=15)
    # ax.Label(fontproperties=myfont)
    ax.set_title("热搜榜按照时长分布", fontproperties=myfont,fontsize=15)
    plt.show()

# 打开文件夹
def openfolder():
    if platform.system()=="Darwin":
        os.system("open Downloads")
    elif platform.system()=="Windows":
        os.system("explorer Downloads")

# 下载界面
def downloadbt():
    # 热门的全局变量
    global position
    global TidStaticImg
    global TidStaticBt
    global TimeStaticImg
    global TimeStaticBt

    # 下载的全局变量
    global OpenFileBt
    global OpenFileImg

    # 搜索的全局变量
    global VsearchE
    global VsearchImg
    global VsearchBt


    global ToE
    global ToImag
    global ToBt

    # 视频详情页的全局变量
    global VimgLabel
    global VTLabel
    global VallInfo
    global opInbBt
    global dlvBt

    if position==1:
        return
    elif position==2:
        for i in range(0,4):
            hottitlelabel[i].place_forget()
            hotbflabel[i].place_forget()
            hotuplabel[i].place_forget()
            hotpicbn[i].place_forget()
        TidStaticBt.place_forget()
        TimeStaticBt.place_forget()
    elif position==3:
        VsearchE.place_forget()
        VsearchBt.place_forget()
        ToE.place_forget()
        ToBt.place_forget()
    elif position==4:
        VimgLabel.place_forget()
        VTLabel.place_forget()
        VallInfo.place_forget()
        opInbBt.place_forget()
        dlvBt.place_forget()
    elif position==5:
        for i in range(0,4):
            Vrlttitlelabel[i].place_forget()
            Vrltuplabel[i].place_forget()
            Vrltbflabel[i].place_forget()
            Vrltpicbn[i].place_forget()

    OpenFileImg=get_image("img/Buttons/openFile.png", 140, 50)
    OpenFileBt=tkinter.Button(root,image=OpenFileImg,command=openfolder)
    OpenFileBt.image=OpenFileImg
    OpenFileBt.place(x=125,y=270)

    position=1

# 搜索界面
def Sch():

    # 现在所在的界面
    global position

    # 热门的全局变量
    global position
    global TidStaticImg
    global TidStaticBt
    global TimeStaticImg
    global TimeStaticBt

    # 下载的全局变量
    global OpenFileBt
    global OpenFileImg

    # 搜索的全局变量
    global VsearchE
    global VsearchImg
    global VsearchBt


    global ToE
    global ToImag
    global ToBt

    # 视频详情页的全局变量
    global VimgLabel
    global VTLabel
    global VallInfo
    global opInbBt
    global dlvBt

    if position==1:
        OpenFileBt.place_forget()
    elif position==2:
        for i in range(0,4):
            hottitlelabel[i].place_forget()
            hotbflabel[i].place_forget()
            hotuplabel[i].place_forget()
            hotpicbn[i].place_forget()
        TidStaticBt.place_forget()
        TimeStaticBt.place_forget()
    elif position==3:
        pass
    elif position==4:
        VimgLabel.place_forget()
        VTLabel.place_forget()
        VallInfo.place_forget()
        opInbBt.place_forget()
        dlvBt.place_forget()
    elif position==5:
        for i in range(0,4):
            Vrlttitlelabel[i].place_forget()
            Vrltuplabel[i].place_forget()
            Vrltbflabel[i].place_forget()
            Vrltpicbn[i].place_forget()
    
    # 第1个模块-视频搜索
    VsearchE=tkinter.Entry(root,bd=1)
    VsearchE.place(x=15,y=120,width=360,height=30,)

    VsearchImg=get_image("img/Buttons/SchV.png", 100, 50)
    VsearchBt=tkinter.Button(root,image=VsearchImg,command=Vrlt)
    VsearchBt.image=VsearchImg
    VsearchBt.place(x=145,y=160)


    # 第2个模块-跳转
    ToE=tkinter.Entry(root,bd=1)
    ToE.place(x=15,y=250,width=360,height=30)

    ToImag=get_image("img/Buttons/ToV.png", 100, 50)
    ToBt=tkinter.Button(root,image=ToImag,command=lambda:VInfo(ToE.get()))
    ToBt.image=ToImag
    ToBt.place(x=145,y=290)

    position=3

# 用浏览器打开
def open_URL(bv:str):
    if bv.startswith("BV") or bv.startswith("bv"):
        pass
    elif bv.startswith("http") or bv.startswith("www"):
        i:int=bv.find("BV")
        o:int=bv.find("?",i)
        p:int=bv.find("/",i)
        if o==-1 and p==-1:
            bv=bv[i:]
        else:
            if o>p and p!=-1:
                bv=bv[i:p]
            elif p<=o and o!=-1:
                bv=bv[i:o]
    url="https://www.bilibili.com/video/"
    tmp=list(url)
    tmp.append(bv)
    url=''.join(tmp)
    webbrowser.open(url)

def tipStart():
    tkinter.messagebox.showinfo("提示","开始下载咯～\n下载完成会有提示哦～")
# 下载视频
def DlV(bv:str):
    # threads=[]
    if bv.startswith("BV") or bv.startswith("bv"):
        pass
    elif bv.startswith("http") or bv.startswith("www"):
        i:int=bv.find("BV")
        o:int=bv.find("?",i)
        p:int=bv.find("/",i)
        if o==-1 and p==-1:
            bv=bv[i:]
        else:
            if o>p and p!=-1:
                bv=bv[i:p]
            elif p<=o and o!=-1:
                bv=bv[i:o]
    url="https://www.bilibili.com/video/"
    tmp=list(url)
    tmp.append(bv)
    url=''.join(tmp)

    
    Thread=[]
    t1=threading.Thread(target=tipStart)
    Thread.append(t1)
    t2=threading.Thread(target=download,args=(url,))
    Thread.append(t2)
    for t in Thread:
        t.setDaemon(True)
        t.start()

# 视频详情界面
def VInfo(bv:str):
    # 现在所在的界面
    global position

    # 热门的全局变量
    global position
    global TidStaticImg
    global TidStaticBt
    global TimeStaticImg
    global TimeStaticBt

    # 下载的全局变量
    global OpenFileBt
    global OpenFileImg

    # 搜索的全局变量
    global VsearchE
    global VsearchImg
    global VsearchBt

    global ToE
    global ToImag
    global ToBt

    # 视频详情页的全局变量
    global VimgLabel
    global VTLabel
    global VallInfo
    global opInbBt
    global dlvBt

    if position==1:
        OpenFileBt.place_forget()
    elif position==2:
        for i in range(0,4):
            hottitlelabel[i].place_forget()
            hotbflabel[i].place_forget()
            hotuplabel[i].place_forget()
            hotpicbn[i].place_forget()
        TidStaticBt.place_forget()
        TimeStaticBt.place_forget()
    elif position==3:
        VsearchE.place_forget()
        VsearchBt.place_forget()
        ToE.place_forget()
        ToBt.place_forget()
    elif position==4:
        return
    elif position==5:
        for i in range(0,4):
            Vrlttitlelabel[i].place_forget()
            Vrltuplabel[i].place_forget()
            Vrltbflabel[i].place_forget()
            Vrltpicbn[i].place_forget()
    
    vinfs=getVideoInfo(bv)
    if vinfs=="error":
        position=3
        return Sch()
    vinfImglink=vinfs["pic"]
    Vimage_bytes=( urlopen(vinfImglink).read())
    Vdata_stream=io.BytesIO(Vimage_bytes)
    Vpil_image=(Image.open(Vdata_stream))
    Vpil_image=Vpil_image.resize((300,187))
    Vtk_image=ImageTk.PhotoImage(Vpil_image)

    VimgLabel=tkinter.Label(root,image=Vtk_image)
    VimgLabel.image=Vtk_image
    VimgLabel.place(x=50,y=120)

    VTLabel=tkinter.Label(text="标题:\n "+vinfs["title"],bg="white",font=("STHeitiSC-Light",17),wraplength=300,justify="left")
    VTLabel.place(x=50,y=320)

    VallInfo=tkinter.Label(text="播放: "+vinfs["bf"]+"\nup主: "+vinfs["up"]+"\n硬币数: "+vinfs["coin"]+"\n长度: "+vinfs["time"]+"\n收藏: "+vinfs["fav"]+"\n评论数: "+vinfs["reply"]+"\n点赞数: "+vinfs["like"]+"\n分区: "+vinfs["tid"],bg="white",justify="left")
    VallInfo.place(x=50,y=380)

    # 用浏览器打开按钮
    opInbImg=get_image("img/Buttons/openinB.png", 100, 50)
    opInbBt=tkinter.Button(root,image=opInbImg,command=lambda:(open_URL(bv)))
    opInbBt.image=opInbImg
    opInbBt.place(x=50,y=520)

    # 下载
    dlvImg=get_image("img/Buttons/dl.png", 100, 50)
    dlvBt=tkinter.Button(root,image=dlvImg,command=lambda:DlV(bv))
    dlvBt.image=dlvImg
    dlvBt.place(x=250,y=520)

    position=4
    
# 视频搜索结果页
def Vrlt():
    # 热门的全局变量
    global position
    global TidStaticImg
    global TidStaticBt
    global TimeStaticImg
    global TimeStaticBt

    # 下载的全局变量
    global OpenFileBt
    global OpenFileImg

    # 搜索的全局变量
    global VsearchE
    global VsearchImg
    global VsearchBt


    global ToE
    global ToImag
    global ToBt

    # 视频详情页的全局变量
    global VimgLabel
    global VTLabel
    global VallInfo
    global opInbBt
    global dlvBt


    Vkw=VsearchE.get()

    if position==1:
            OpenFileBt.place_forget()
    elif position==2:
        for i in range(0,4):
            hottitlelabel[i].place_forget()
            hotbflabel[i].place_forget()
            hotuplabel[i].place_forget()
            hotpicbn[i].place_forget()
        TidStaticBt.place_forget()
        TimeStaticBt.place_forget()
    elif position==3:
        VsearchE.place_forget()
        VsearchBt.place_forget()
        ToE.place_forget()
        ToBt.place_forget()
    elif position==4:
        VimgLabel.place_forget()
        VTLabel.place_forget()
        VallInfo.place_forget()
        opInbBt.place_forget()
        dlvBt.place_forget()
    elif position==5:
        return

    RltV=Vsearch(Vkw)

    # 注意添加全局变量
    
    for i in range(0,4):
        Vrltdic=getVideoInfo(RltV[i])
        Vrltimg[i]=(Vrltdic["pic"])
        Vrlttitle[i]=(Vrltdic["title"])
        Vrltup[i]=(Vrltdic["up"])
        Vrltbf[i]=(Vrltdic["bf"])

        Vrlttitlelabel[i]=(tkinter.Label(text=Vrlttitle[i],bg="white",wraplength=200,justify="left"))
        Vrlttitlelabel[i].place(x=180,y=120+100*i)

        Vrltuplabel[i]=(tkinter.Label(text="up主: "+Vrltup[i],bg="white"))
        Vrltuplabel[i].place(x=180,y=160+100*i)

        Vrltbflabel[i]=(tkinter.Label(text="播放: "+Vrltbf[i],bg="white"))
        Vrltbflabel[i].place(x=180,y=180+100*i)

    # 按钮1
    picurl=Vrltimg[0]
    Vrltimage_bytes [0]=( urlopen(picurl).read())
    Vrltdata_stream [0]=( io.BytesIO(Vrltimage_bytes[0]))
    Vrltpil_image [0]=(Image.open(Vrltdata_stream[0]))
    Vrltpil_image[0]=Vrltpil_image[0].resize((130,80))
    Vrlttk_image[0]=(ImageTk.PhotoImage(Vrltpil_image[0]))

    Vrltpicbn[0]=(tkinter.Button(root,image=Vrlttk_image[0],command=lambda:VInfo(RltV[0])))
    Vrltpicbn[0].image=Vrlttk_image[0]
    Vrltpicbn[0].place(x=20,y=120+100*0)

    # 按钮2
    picurl=Vrltimg[1]
    Vrltimage_bytes [1]=( urlopen(picurl).read())
    Vrltdata_stream [1]=( io.BytesIO(Vrltimage_bytes[1]))
    Vrltpil_image [1]=(Image.open(Vrltdata_stream[1]))
    Vrltpil_image[1]=Vrltpil_image[1].resize((130,80))
    Vrlttk_image[1]=(ImageTk.PhotoImage(Vrltpil_image[1]))

    Vrltpicbn[1]=(tkinter.Button(root,image=Vrlttk_image[1],command=lambda:VInfo(RltV[1])))
    Vrltpicbn[1].image=Vrlttk_image[1]
    Vrltpicbn[1].place(x=20,y=120+100*1)

    # 按钮3
    picurl=Vrltimg[2]
    Vrltimage_bytes [2]=( urlopen(picurl).read())
    Vrltdata_stream [2]=( io.BytesIO(Vrltimage_bytes[2]))
    Vrltpil_image [2]=(Image.open(Vrltdata_stream[2]))
    Vrltpil_image[2]=Vrltpil_image[2].resize((130,80))
    Vrlttk_image[2]=(ImageTk.PhotoImage(Vrltpil_image[2]))

    Vrltpicbn[2]=(tkinter.Button(root,image=Vrlttk_image[2],command=lambda:VInfo(RltV[2])))
    Vrltpicbn[2].image=Vrlttk_image[2]
    Vrltpicbn[2].place(x=20,y=120+100*2)

    # 按钮4
    picurl=Vrltimg[3]
    Vrltimage_bytes [3]=( urlopen(picurl).read())
    Vrltdata_stream [3]=( io.BytesIO(Vrltimage_bytes[3]))
    Vrltpil_image [3]=(Image.open(Vrltdata_stream[3]))
    Vrltpil_image[3]=Vrltpil_image[3].resize((130,80))
    Vrlttk_image[3]=(ImageTk.PhotoImage(Vrltpil_image[3]))

    Vrltpicbn[3]=(tkinter.Button(root,image=Vrlttk_image[3],command=lambda:VInfo(RltV[3])))
    Vrltpicbn[3].image=Vrlttk_image[3]
    Vrltpicbn[3].place(x=20,y=120+100*3)

    position=5
    
def GoTo():
    pass

if __name__=="__main__":
    root=Tk()

    root.title("BiliBili_Tools")
    root.geometry("400x600+300+150")
    root.iconphoto(False, tkinter.PhotoImage(file="img/Icons/icon.png"))
    root.resizable(False,False)

    cavas=tkinter.Canvas(root,width=400,height=600)
    im_root=get_image("img/BackGround/Bg.png",400,600)
    cavas.create_image(200,300,image=im_root)
    
    cavas.pack()

    dlbt=get_image("img/Buttons/download.png", 100, 50)
    bt=tkinter.Button(root,image=dlbt,command=downloadbt)
    bt.place(x=15,y=30,)

    ht=get_image("img/Buttons/hot.png", 100, 50)
    bt=tkinter.Button(root,image=ht,command=hotbt)
    bt.place(x=145,y=30,)

    scbt=get_image("img/Buttons/search.png", 100, 50)
    bt=tkinter.Button(root,image=scbt,command=Sch)
    bt.place(x=275,y=30,)

    root.mainloop()
    pass