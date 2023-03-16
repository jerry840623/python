from tkinter import messagebox
import tkinter as tk


def main():
    flag = True

    def change_lable_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'hello world') if flag else ('blue', 'goodbye world')
        label.config(text=msg, fg=color)

    def comfirm_quit():
        if messagebox.askokcancel('溫馨提示', '確定退出'):
            top.quit()

    top = tk.Tk()
    top.geometry('240x160')
    top.title('small game')

    label = tk.Label(top, text='hello world', font='Arial -20', fg='red')
    label.pack()


    panel = tk.Frame(top)

    button1 = tk.Button(panel, text='修改', command=change_lable_text)
    button1.pack(side='left')
    button2 = tk.Button(panel, text='退出', command=comfirm_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')

    top.mainloop()


if __name__=='__main__':
    main()




    