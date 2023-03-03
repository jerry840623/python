import random
# import math
import calendar
import os
import string
import jieba
import wordcloud
import functools

"""
number=random.randint(1,9)
guess=-1
print("猜數遊戲")

while guess != number:
    guess = int(input("請輸入你猜的數字，按0退出"))
    if guess == 0:
        break
    if guess == number:
        print("恭喜你猜對了")
    elif guess < number:
        print("數字小了")
    elif guess > number:
        print("數字大了")


year = int(input("請輸入年份："))
if (year % 4 ==0 and year % 100 != 0 or year % 400 == 0):
    print("閏年")
else:
    print("不是閏年")

print(isinstance(year,str)) 




for qing in range(10):
    for long in range(10):
        for shan in range(10):
            for wai in range(10):
                if (qing == long or qing == shan or qing == wai or long == shan or long == wai or shan == wai):
                    continue
                elif (qing*1000+long*100+shan*10+wai==shan*100+wai*10+shan+qing*100+long*10+shan):
                    print('qing=',qing,'long=',long,'shan=',shan,'wai=',wai)
                    # print('qing=%d,long=%d,shan=%d,wai=%d'%(qing,long,shan,wai))
                    break


s='星期一星期二星期三星期四星期五星期六星期日'

while True:
    y=input('請輸入年份，按x退出：')

    if y == 'x':
        break

    else:
        m=input('請輸入月份：')
        d=input('請輸入日期：')
        i=calendar.weekday(int(y),int(m),int(d))
        print(i)
        print('你輸入的日期{0}年{1}月{2}日是：{3:>5}'.format(y,m,d,s[i*3:i*3+3]))


y=input('請輸入年份：')
m=input('請輸入月份：')
d=input('請輸入日期：')
dic={0:'星期一',1:'星期二',2:'星期三',3:'星期四',4:'星期五',5:'星期六',6:'星期日'}
if y.isdigit() and m.isdigit() and d.isdigit() and 1<=int(m)<=12 and 1<=int(d)<=31:
    w=calendar.weekday(int(y),int(m),int(d))
    print(dic.get(w))
else:
    print('日期錯誤')

print(calendar.month(2023,1))


os.chdir('D:\\vs-code\\python')
l=open('1.txt','r',encoding='utf-8')
f=open('score.txt','a')
a=l.readline()
bl=[]
while 1:
    x=l.readlines()
    for i in x:
        if len(i)>0:
            c=[]
            for d in list(i.split()):
                c.append(int(d))
            sum=c[1]+c[2]+c[3]
            if c[1]>=85 and c[2]>=85 and c[3]>=85 and sum>=260:
                f.write('%s\t%s\n'%(c[0],'優秀'))
            elif c[2]>=90:
                f.write('%s\t%s\n'%(c[0],'良好'))
            elif c[2]>=60 and c[3]>=60 and sum>=160:
                f.write('%s\t%s\n'%(c[0],'及格'))

            else:
                f.write('%s\t%s\n'%(c[0],'不及格'))



        else:
            break
    if len(x)==0:
        break




 
l.close()
f.close()





os.chdir('D:\\vs-code\\python')
LS=open('2.txt','r',encoding='utf-8')
la=open('3.txt','w',encoding='utf-8')

car=[]
carone=list(LS.read().split('\n'))
print(carone)
for c in carone:
    d=c.split(',')
    if 31.2222<=float(d[2])<=31.2333 and 121.45<=float(d[3])<=121.55:
        c=c+'\n'
        print(c)
        car.append(c)

la.writelines(car)
la.close
LS.close


LS=list(open('2.txt','r',encoding='utf-8'))
min_n,min_e=31.2222,121.45
max_n,max_e=31.2333,121.55
car=[]
for s in LS:
    carone=s[:-1].split(',')
    car.append(carone)
for t in range(len(car)):
    if min_n<float(car[t][2])<=max_n and min_e<float(car[t][3])<max_e:
        print('時間:%s\t車牌：%s\t北緯:%s,東經：%s'%(car[t][0],car[t][1],car[t][2],car[t][3]))


os.chdir('D:\\vs-code\\python')
la=open('3.txt','r',encoding='utf-8')
speech_text=la.read()
la.close
speech=speech_text.lower().split()
dic={}
for word in speech:
    if word not in dic:
        dic[word]=1
    else:
        dic[word]+=1

swd=sorted(list(dic.items()),key=lambda st1:st1[1],reverse=True)
print(swd)
for kword,times in swd:
    print(kword,times)


os.chdir('D:\\vs-code\\python')
f=open('荷塘月色.txt','r',encoding='utf-8')
fl=f.read()
f.close
article=jieba.lcut(fl)
dic={}
for word in article:
    if word not in dic:
        dic[word]=1
    else:
        dic[word]+=1
swd=sorted(list(dic.items()),key=lambda lst:lst[1],reverse=True)
f1=open('stop_words.txt','r',encoding='utf-8')
stop_word=f1.read()
for kword,items in swd:
    if kword not in stop_word:

        print(kword,items)

os.chdir("D:\\vs-code\\python")
txt='荷塘 采莲 今晚 路 叶子 想起 一条 这是 白天 树 知道 月光'
wd=wordcloud.WordCloud(background_color='white',width=150,height=120,max_font_size=48,font_path='c:/windows/fonts/simhei.ttf')
wd.generate(txt)
wd.to_file('txt.png')


def add(a,b):
    return a+b
def subtract(a,b):
    return a-b

def func(a,b,fun):
    return fun(a,b)
a=int(input('請輸入第一個參數：'))
b=int(input('請輸入第二個參數：'))
method=add
print('%s:參數1為%d，參數2為：%d,結果為%d' %(method,a,b,func(a,b,method)))

method=subtract

print('%s:參數1為%d，參數2為：%d,結果為%d' %(method,a,b,func(a,b,method)))


x=0
def outer():
    x=1 #enclosing
    def inner():
        x=2 #local
        print('local: x=',x)
    inner()
    print('enclosing=',x)
outer()
print('global=',x)


def fb(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fb(i-1) + fb(i-2)  
n=6
print(fb(n))

lfb=[0,1]
for t in range(n):
    lfb.append(lfb[t]+lfb[t+1])
print(lfb[n])



def gcd(a,b):
    if b ==0:
        return a
    else:
        return gcd(b,a%b)
a,b=167,189
print(gcd(a,b))


from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
 
        a_func()
 
        print("I am doing some boring work after executing a_func()")
 
    return wrapTheFunction
#@a_new_decorator
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

#a_function_requiring_decoration()
#outputs: "I am the function which needs some decoration to remove my foul smell"
 
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
#now a_function_requiring_decoration is wrapped by wrapTheFunction()
 
a_function_requiring_decoration()
#outputs:I am doing some boring work before executing a_func()
#        I am the function which needs some decoration to remove my foul smell
#        I am doing some boring work after executing a_func()
print(a_function_requiring_decoration.__name__)


os.chdir('D:\\vs-code\\python')
def logit(logfile='out.log'):
    def logging_decorator(func):
        @functools.wraps(func)
        def wrapped_function(*args,**kwargs):
            log_string= func.__name__+'was called'
            print(log_string)
            with open(logfile,'a') as opened_file:
                opened_file.write(log_string+'\n')
            return(func(*args,**kwargs))
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    print('fun1')

#myfunc1()


@logit(logfile='out1.log')
def myfunc2():
    pass

#myfunc2()

#print(myfunc1.__name__)

import random
def redEnv(rest):
    m=random.random()
    return m
total=int(input('請輸入紅包金額：'))
num = int(input('請輸入紅包個數：'))

remain=total
for i in range(num-1):
    money=redEnv(remain)
    remain-=money
    print('紅包%d： %d元' %(i+1,money))

print('紅包%d： %d元' %(num,remain))


class Scale:
    def check(self):
        if self.count_person > 500:
            return "%s是個大公司。" %self.name
        else:
            return "%s是個小公司。" %self.name

class Detail:
    def show(self,scale):
        print("%s,公司有%s名員工。" %(scale,self.count_person))

class Company(Scale,Detail):
    def __init__(self,name,count):
        self.name = name
        self.count_person = count

if __name__ == "__main__":
    my_company=Company('abc',800)
    company_scale = my_company.check()
    my_company.show(company_scale)

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
    if messagebox.showwarning('Cannel','Sorry,Login Cannel'):
        win.destroy()



bt1=Button(win,text='Login',command=LogSussess).grid(row=2,column=0)
bt2=Button(win,text='Cannel',command=LogCannel,).grid(row=2,column=1)

ety=Entry(win)
ety.grid(row=3,column=0)


win.mainloop()



"""

