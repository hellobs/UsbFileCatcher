import os
from os.path import join,getsize
import time
from datetime import datetime
import shutil
import json
import threading
from tkinter.messagebox import showinfo,showerror
class Main():
    def __init__(self,udiskpath="H:/",savetopath="D:/backups/"):
        self.UDISKPATH = udiskpath
        self.SAVETOPATH = savetopath
        self.SIZE = 0
        self.calls = False
        self.oldsize = 0

    def get_dirs_size(self): 
        self.SIZE = 0
        for root, dirs, files in os.walk(self.UDISKPATH):
            self.SIZE += sum([getsize(join(root,name)) for name in files])
            return self.SIZE

    def check_newdisk(self):
        self.newsize = self.get_dirs_size()
        if self.newsize != self.oldsize:
            return True
        else:
            return False
    
    def copy_file(self):
        strings = "".join((self.SAVETOPATH,datetime.now().strftime("%Y-%m-%d_%H%M%S")))
        shutil.copytree(self.UDISKPATH,os.path.join((str(strings))))
        self.calls = True
        self.oldsize = self.get_dirs_size()
    
    def loop(self,outputfunc):
        thread = threading.Thread(target=self.main,args=[outputfunc])
        thread.start()

    def main(self,outputfunc=print):
        print = outputfunc
        
        while 1:
            if os.path.exists(self.UDISKPATH):
                print("检测到U盘插入")
                try:
                    if self.check_newdisk():
                        print("文件有新内容,字节大小："+str(self.get_dirs_size()))
                        self.copy_file()
                        print("完成操作.")
                        showinfo("提示","保存成功!")
                        print("------------------------")
                        self.calls = True
                
                except Exception as e:
                    print("发生错误:"+str(e))
                    showerror("错误","请检查填写路径是否正确，若问题仍在，请联系作者解决")
                    self.calls = False
                time.sleep(10)
            else:
                print("未发现u盘插入")
                self.calls = False
                time.sleep(10)


if __name__ == "__main__":
    print("UsbFileCatcher 1.0 ")
    print("Author: z-z-r")
    print("SavePath: Backups")
    print("--------------------------")
    obj = Main()
    obj.main()
