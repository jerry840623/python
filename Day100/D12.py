import re
'''
def main():
    username=input('请输入用户名：')
    m1=re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    while not m1:
        username=input('请输入有效用户名：')
        m1=re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    qq=input('请输入QQ号:')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    while not m2:
        qq=input('请输入有效QQ号:')
        m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if m1 and m2:
        print('您输入的信息有效')


if __name__=='__main__':
    main()

'''

def main():
    pattern=re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    mylist=re.findall(pattern,sentence)
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


if __name__=='__main__':
    main()