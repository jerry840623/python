#练习1

for ra in range(100,1000):
    low=ra%10
    mid=ra//10%10
    high=ra//100
    if ra ==low**3+mid**3+high**3:
        print('%d是水仙花数' %ra)



#练习2
num = int(input('num='))

re_num=0

while num>0:
    re_num=re_num*10+num%10

    num//=10

print(re_num)

#练习3

for x in range(0,20):
    for y in range(0,33):
        z=100-x-y
        if x*5+y*3+z/3==100:
            print('有公鸡%d,母鸡%d,小鸡%d' %(x,y,z))


    
#作业1
fb=[1,1]
for i in range(0,18):
    fb.append(fb[i]+fb[i+1])

print(len(fb))
print(fb)

#作业2
import math

for num in range(2, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)
