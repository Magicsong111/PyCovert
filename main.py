'''
  Made by Magic_song
'''
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import shutil
import sys
root=Tk()  #窗口
def error(msg:str,line:int)->None:
    '''报错函数
    弹窗后返回退出代码 `-1`
    
    :param msg: 报错消息
    :type msg: str
    :param line: 报错行数
    :type line: int
    '''
    s="Error!\nIn line "+str(line)+"\n"+msg  #报错消息
    messagebox.showerror("Error!",s)  #弹窗提醒
    sys.exit(-1)  #退出程序
def End()->None:
    '''按下 `X` 按钮时调用的代码'''
    t=messagebox.askyesno("退出","确定要退出吗?")  #弹窗提醒
    if t:  #确定?
        sys.exit(0)  #正常退出
def Button1()->None:
    '''按下 `按钮1` 按钮调用的代码'''
    s=filedialog.askopenfilename(filetypes=[("py(*.py)",".py")],parent=root)  #创建一个打开文件窗口
    e1["textvariable"]=StringVar(root,s)  #文本框e1文字改变
def Button2()->None:
    '''按下 `按钮2` 按钮调用的代码'''
    s=filedialog.askopenfilename(filetypes=[("图标(*.ico)",".ico")],parent=root)  #创建一个打开文件窗口
    e2["textvariable"]=StringVar(root,s)  #文本框e2文字改变
def Button3()->None:
    '''按下 `按钮3` 按钮调用的代码'''
    s=filedialog.askopenfilename(filetypes=[("版本(*.txt)",".txt")],parent=root)  #创建一个打开文件窗口
    e3["textvariable"]=StringVar(root,s)  #文本框e3文字改变
def Button4()->None:
    '''按下 `按钮4` 按钮调用的代码'''
    s=filedialog.askdirectory(parent=root)  #创建一个打开文件夹窗口
    e4["textvariable"]=StringVar(root,s)  #文本框e4文字改变
def Button5()->None:
    '''按下 `按钮5` 按钮调用的代码
    注意,转换中会输出运行参数

    >>>pyinstaller -F -w -n output --version-file 1.txt --distpath C:\ 114514.py
    '''
    global running  #全局变量running
    running=[]  #初始化
    running.append(e1.get())  #加入e1字符串内容
    running.append(e2.get())  #加入e2字符串内容
    running.append(e3.get())  #加入e3字符串内容
    running.append(e4.get())  #加入e4字符串内容
    if running[0]=="":  #没选*.py文件?
        error("致命错误:\n  无输入文件",69)  #报错
    if running[3]=="":  #没选输出路径?
        running[3]="C:"  #默认输出路径
    cmd="pyinstaller -F "  
    if i.get()==0:  #窗口模式
        cmd+="-w "
    cmd+="-n output "  #输出文件名称
    if i2.get():  #选了图标
        cmd+="-i \""+running[1]+"\" "
    if i3.get():  #选了版本
        cmd+=" --version-file \""+running[2]+"\" "
    cmd+="--distpath \""+running[3]+"\" "  #设定输出路径
    cmd+=running[0]
    print(cmd)  
    os.system(cmd)  #运行
    messagebox.showinfo("完成!","转换完成")  #弹窗提醒
    """ 删除所有临时文件 """
    os.remove("./output.spec")  
    shutil.rmtree("./build")
def Button6()->None:
    '''按下 `按钮6` 按钮调用的代码'''
    temp="start "+running[3]
    os.system(temp)
def PackButton(txt:str,x:int,y:int,w:int,h:int,master:Tk,fuc:object)->Button:
    '''包装按钮:使用 `Button类的构造器` 进行包装

    :param txt: 文本
    :type txt: str
    :param x: x坐标
    :type x: int
    :param y: y坐标
    :type y: int
    :param w: 宽度
    :type w: int
    :param h: 高度
    :type h: int
    :param master: 父窗口
    :type master: Tk
    :param fuc: 按下按钮时调用的函数
    :type fuc: object
    :return: 返回这个类
    :rtype: Button
    '''
    button=Button(master,text=txt,width=int(w/10),height=int(h/10),command=fuc)
    button.place(x=x,y=y)
    return button
def PackEntry(txt:str,x:int,y:int,w:int,master:Tk)->Entry:
    '''包装文本框:使用 `Entry类的构造器` 进行包装
    
    :param txt: 文本
    :type txt: str
    :param x: x坐标
    :type x: int
    :param y: y坐标
    :type y: int
    :param w: 宽度
    :type w: int
    :param master: 父窗口
    :type master: Tk
    :return: 返回这个类
    :rtype: Entry
    '''
    entry=Entry(master,text=txt,width=int(w/10))
    entry.place(x=x,y=y)
    return entry
def PackCheckButton(txt:str,x:int,y:int,w:int,h:int,master:Tk,i:IntVar)->Checkbutton:
    '''包装多选按钮:使用 `CheckButton类的构造器` 进行包装

    :param txt: 文本
    :type txt: str
    :param x: x坐标
    :type x: int
    :param y: y坐标
    :type y: int
    :param w: 宽度
    :type w: int
    :param h: 高度
    :type h: int
    :param master: 父窗口
    :type master: Tk
    :param i: 存储数据变量
    :type i: IntVar
    :return: 返回这个类
    :rtype: CheckButton
    '''
    Check=Checkbutton(master,text=txt,width=int(w/10),height=int(h/10),variable=i)
    Check.place(x=x,y=y)
    return Check
def PackRadioButton(txt:str,x:int,y:int,w:int,h:int,master:Tk,v:IntVar,b:int)->Radiobutton:
    '''包装单选按钮:使用 `RadioButton类的构造器` 进行包装

    :param txt: 文本
    :type txt: str
    :param x: x坐标
    :type x: int
    :param y: y坐标
    :type y: int
    :param w: 宽度
    :type w: int
    :param h: 高度
    :type h: int
    :param master: 父窗口
    :type master: Tk
    :param v: 存储数据变量
    :type v: IntVar
    :return: 返回这个类
    :rtype: RadioButton

    '''
    Radio=Radiobutton(master,text=txt,width=int(w/10),height=int(h/10),variable=v,value=b)
    Radio.place(x=x,y=y)
    return Radio
def main()->None:
    '''主函数'''
    root.geometry("600x370+0+0")  #初始化大小
    root.title("PY COVERT")  #标题
    root.protocol("WM_DELETE_WINDOW",End)  #设定按下X键时调用End函数
    """ 组件 """
    global b1,b2,b3,b4,b5,b6 
    global e1,e2,e3,e4
    global l1,l2,l3
    global cb1,cb2
    global rb1,rb2
    global i
    global i2,i3
    i=IntVar()
    i.set(0)
    i2=BooleanVar()
    i3=BooleanVar()
    """ 绘制文本 """
    l1=Label(root,text="输入文件:").place(x=10,y=10)
    l2=Label(root,text="输出文件:").place(x=10,y=145)
    l3=Label(root,text="模式:").place(x=10,y=180)
    """ 包装组件 """
    e1=PackEntry("",80,12,630,root)
    b1=PackButton("选择",525,12,100,10,root,Button1)
    cb1=PackCheckButton("图标",0,40,70,30,root,i2)
    e2=PackEntry("",80,60,630,root)
    b2=PackButton("选择",525,60,100,10,root,Button2)
    cb2=PackCheckButton("版本",0,80,70,30,root,i3)
    e3=PackEntry("",80,100,630,root)
    b3=PackButton("选择",525,100,100,10,root,Button3)
    e4=PackEntry("",80,150,630,root)
    b4=PackButton("选择",525,150,100,10,root,Button4)
    rb1=PackRadioButton("window",145,180,135,10,root,i,0)
    rb2=PackRadioButton("cmd",300,180,135,10,root,i,1)
    b5=PackButton("转换",60,225,210,70,root,Button5)
    b6=PackButton("查看文件位置",400,225,210,70,root,Button6)
    """ 大循环 """
    root.mainloop()
    sys.exit(0)  #结束程序
if __name__=="__main__":
    """ 主程序入口 """
    main()

