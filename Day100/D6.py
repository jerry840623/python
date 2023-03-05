
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
'''

def gcd(x,y):
    if y>x:
        (x,y)=(y,x)
    for f in range(x,0,-1):
        if x%f==0 and y%f==0:
            return f
        
print(gcd(88,56))




