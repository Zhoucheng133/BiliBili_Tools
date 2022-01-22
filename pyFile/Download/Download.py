# 下载模块
import os
import sys
from tkinter import *
import math
import tkinter.messagebox
import time
import platform
import subprocess
from pygame import mixer
def download(url):
    cmd=("you-get -o Downloads %s")%url

    # cmd="you-get -o Downloads https://www.bilibili.com/video/BV1YA411H7LM"
    result=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    out,err = result.communicate()
    rltlst=[]
    for line in out.splitlines():  
        rltlst.append(line)

    output_str=str(rltlst)
    # print(output_str)

    if "download" in output_str:
        print("下载完成")
        mixer.init()
        mixer.music.load('music/14392.mp3')
        mixer.music.play()

        tkinter.messagebox.showinfo("完成","下载完成，去下载界面\n打开文件夹中查看吧～")
    else:
        print("失败")
        tkinter.messagebox.showerror("失败","下载失败")
if __name__ =="__main__":
    download("https://www.bilibili.com/video/BV1YA411H7LM?spm_id_from=333.999.0.0")