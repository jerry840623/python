from tkinter import *
from tkinter import messagebox
import time

root=Tk()
root.geometry('450x150+100+100')
root.title('Clock')

dstr=StringVar()


def gettime():
    t=time.gmtime()
    dstr.set(time.strftime("%Y-%m-%d %H:%M:%S",t))
    root.after(1000,gettime)

Label(root,textvariable=dstr,fg='green',).pack(side='bottom')

gettime()

root.mainloop()