from tkinter import *
from tkinter.messagebox import showinfo
import tkinter.ttk as ttk
import tkinter.tix as tix
from tkinter.scrolledtext import ScrolledText 
import unit

class Layouts:
    def __init__(self):
        pass

    def run(self):
        self.create_tk()
        self.create_menu()
        self.create_body()
        self.tk.mainloop() #if alive

    def create_tk(self):
        self.tk = Tk()
        self.tk.title("U盘备份小工具")
        self.tk.wm_attributes("-topmost",0)
        self.tk.geometry("600x600")
        self.tk.update()

    def create_menu(self):
        self.menu = Menu(self.tk)

        self.filemenu = Menu(self.menu,tearoff=0)
        self.filemenu.add_command(label="退出",command=self.EXIT)
        self.menu.add_cascade(label="文件",menu=self.filemenu)

        self.aboutmenu = Menu(self.menu,tearoff=0)
        self.aboutmenu.add_command(label="关于本程序",command=self.aboutprogram)
        self.aboutmenu.add_command(label="关于作者",command=self.aboutauthor)
        self.menu.add_cascade(label="关于",menu=self.aboutmenu)

        self.tk.config(menu=self.menu)
    
    def create_body(self):
        self.udiskvar = StringVar()
        self.savetovar = StringVar()
        self.udiskvar.set("F:/")
        self.savetovar.set("D:/backups/")
        self.frame = ttk.LabelFrame(self.tk)
        self.frame.pack(expand=YES,fill=BOTH,pady=5,padx=5)
        Label(self.frame,text="输入U盘路径:").grid(row=0,padx=5,pady=5)
        Label(self.frame,text="输入保存路径:").grid(row=1,padx=5,pady=5)
        self.udiskpathentry = ttk.Entry(self.frame,textvariable=self.udiskvar)
        self.savetopathentry = ttk.Entry(self.frame,textvariable=self.savetovar)
        
        self.udiskpathentry.grid(row=0,column=1)
        self.savetopathentry.grid(row=1,column=1)
        Label(self.frame,text="详细数据输出").grid(row=2)
        self.scrolltext = ScrolledText(self.frame,width=40,height=20)
        self.scrolltext.grid(row=3,columnspan=3,padx=45)
        self.button = ttk.Button(self.tk,text="确定",command=self.enter)
        self.button.pack(side=LEFT,padx=45,pady=5)
        
    def enter(self):
        self.UDISKPATH = self.udiskpathentry.get()
        self.SAVETOPATH = self.savetopathentry.get()
        showinfo("提示","程序已开始")      
        self.output("U盘路径:"+self.UDISKPATH)
        self.output("保存路径:"+self.SAVETOPATH)
        self.output("参数：")
        self.output("------------------------")
        mainunit = unit.Main(self.udiskpathentry.get(),self.savetopathentry.get())
        mainunit.loop(self.output)

    def EXIT(self):
        exit()
    
    def aboutprogram(self):
        pass

    def aboutauthor(self):
        pass

    def output(self,text=""):
        self.scrolltext.insert(END,str(text)+"\n")

if __name__ == "__main__":
    main = Layouts()
    main.run()