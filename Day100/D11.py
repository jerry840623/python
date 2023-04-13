import time
'''
def main():
    f=None
    try:
        with open('/Users/jigaotang/Downloads/Python-100-Days-master/Day01-15/code/Day11/致橡树.txt','r',encoding='utf-8') as f:
            lines=f.readlines()
            for line in lines:
                print(line)
                time.sleep(0.5)
    
            
    except FileNotFoundError:
        print('FileNotFound')
    except FileExistsError:
        print('Exists')
    finally:
        print('finally')


if __name__=='__main__':
    main()



from math import sqrt


def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成!')


if __name__ == '__main__':
    main()


import time
def main():

    with open('D:\\vs-code\\Python-100-Days-master\\Day01-15\\code\\Day11\\致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())
    

    with open('D:\\vs-code\\Python-100-Days-master\\Day01-15\\code\\Day11\\致橡树.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line)
            time.sleep(0.5)

    with open('D:\\vs-code\\Python-100-Days-master\\Day01-15\\code\\Day11\\致橡树.txt', 'r', encoding='utf-8') as f:
        lines=f.readlines()
        print(lines)
        for line in lines:
            print(line)

if __name__=='__main__':
    main()

    


import json

def main():
    mydict={
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }

    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict,fs)
    except FileNotFoundError as e:
        print(e)
    print('Save date Finshed')



if __name__=='__main__':
    main()


import requests
import json


def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)

    for news in data_model['newslist']:
        print(news['title'])

if __name__=='__main__':
    main()
'''

import re


def main():
    # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    # 查找所有匹配并保存到一个列表中
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------华丽的分隔线--------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------华丽的分隔线--------')
    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


if __name__ == '__main__':
    main()