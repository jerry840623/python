import os
import time

'''
s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!
"""
print(s1, s2, s3, end='')

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')

s1 = 'hello ' * 3
print(s1) # hello hello hello 
s2 = 'world'
s1 += s2
print(s1) # hello hello hello world
print('ll' in s1) # True
print('good' in s1) # False
str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2]) # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5]) # c12
print(str2[2:]) # c123456
print(str2[2::2]) # c246
print(str2[::2]) # ac246
print(str2[::-1]) # 654321cba
print(str2[-3:-1]) # 45



str1= 'Hello, world!'

print(str1.find('or'))
print(str1.find('st'))
print(str1.index('or'))
print(str1.startswith('He'))
print(str1.startswith('he'))
print(str1.endswith('!'))
print(str1.center(50,'*'))


def sj(n):
    a='c'
    print(a.center(20,'*'))
    for i in range(1,n,2):
        print((a*i+a*2).center(20,'*'))

sj(10)

print(str1.rjust(20,'*'))

str2='abc123456'

print(str2.isdigit())
print(str2.isalpha())
print(str2.isalnum())

str3='   asfasf@163.com'
print(str3)
print(str3.strip())

for i in list1:
    print(i,end=' ')

for i in range(len(list1)):
    print(list1[i])

for i , enum in enumerate(list1):
    print(i+1,enum)

a,b=5,6
print(f'{a}*{b}={a*b}')



list1=[1,3,4,7,100]

list1.append(200)
print(list1)
list1.insert(1,111)

print(list1)

list1.extend([2222,33333])
print(list1)

if 1234 in list1:
    list1.remove(3)

list1.pop(len(list1)-1) # list1.pop(-1)
print(list1)


fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']

fruits2=fruits[1:4]
print(fruits,fruits2)



def fib(num):
    a,b=0,1
    for _ in range(0,num):
        a,b=b,a+b
        yield a
    

for val in fib(10):
    print(val)


def get_filelists(file_dir='.'):
    list_directory = os.listdir(file_dir)
    filelists = []
    for directory in list_directory:
        # os.path 模块稍后会讲到
        if os.path.isfile(directory):
            filelists.append(directory)
    return filelists

def list_file():
    list_file=os.listdir('E:/nsconfig')
    file_list=[]
    for file_name in list_file:
        file_path=os.path.join('E:/nsconfig\\\\',file_name)
        if os.path.isfile(file_path):
            file_list.append(file_name)
    return(file_list)

print(list_file())



#練習1
def main():
    content='北京欢迎您。。。。。。'
    while  True:
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content=content[1:]+content[0]


if __name__=='__main__':
    main()


#練習2
import random

def gen_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code=""
    for _ in range(code_len):
        code+=all_chars[random.randint(0,len(all_chars)-1)]
        # code.append(all_chars[random.randrange(0,len(all_chars)-1)])
    print(code)
def main():
    gen_code()


if __name__ == '__main__':
    main()

    
  '''  
def get_suffix(filename='E:', has_dot=False):
    file=os.listdir(filename)
    
    for f in file:
        dot= f.rfind('.')
        if 0<dot<len(f):
            yield f[dot+1:]
        else:
            yield 'no dot'
        





def main():
    dot_name=get_suffix('E:/nsconfig')
    for dot in dot_name:
        print(dot)

if __name__=='__main__':
    main()
