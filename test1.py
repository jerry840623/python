from tkinter import *
from tkinter import messagebox

win=Tk()
win.geometry('400x400+200+200')
win.title('Login')
win.config(background='yellow')

lb1=Label(win,text='UserName:',bg='green',fg='white').grid(row=0)
lb2=Label(win,text='Password',bg='green',fg='white').grid(row=1)

ent1=Entry(win,width=30).grid(row=0,column=1)
ent2=Entry(win,show='********',width=30).grid(row=1,column=1)

def LogSussess():
    messagebox.showinfo('welcom','login sucsses')

def LogCannel():
    messagebox.showwarning('Cannel','Sorry,Login Cannel')
    win.destroy()



bt1=Button(win,text='Login',command=LogSussess).grid(row=2,column=0)
bt2=Button(win,text='Cannel',command=LogCannel,).grid(row=2,column=1)

win.mainloop()

