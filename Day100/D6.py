
'''
count=0
for a in range(1,9):
    for b in range(1,9-a):
        for c in range(1,9-a-b):
            for d in range(1,9-a-b-c):
                if a+b+c+d==8:
                    count+=1
                    print('a:%d,b:%d,c:%d,d:%d' %(a,b,c,d))
                    
print(count)


import dd6_1

# 练习1
def gcd(x,y):
    if y>x:
        (x,y)=(y,x)
    for f in range(x,0,-1):
        if x%f==0 and y%f==0:
            return f
        
print(gcd(88,56))


def lcm(x,y):
    return x*y//gcd(x,y)

print(lcm(8,6))



# 练习2 实现判断一个数是不是回文数的函数

orint=int(input('请输入一个数：'))



def is_palindrome(num):
    tempint=0
    while num>0:
        tempint=tempint*10+num%10
        num//=10
    print(tempint)
    return(tempint==orint)
    


print(is_palindrome(orint))

    tempint=num
    for i in range(2,(tempint**0.5)+1):
        count=1
        if i %



# 实现判断一个数是不是素数的函数
is_pri=[]
def is_prime(num):
    for i in range(2,num+1):
        for k in range(2,i+1):
            if i % k==0:
                if i == k:
                    is_pri.append(i)
                else:
                    break
    
    

is_prime(50)
print(is_pri)
                
'''