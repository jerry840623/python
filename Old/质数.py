import math
primenumber = []
flag = False
for x in range(2,100):
    for i in primenumber:
        if x % i == 0:
            flag = True
            break
        if i >= math.ceil(math.sqrt(x)):
            flag = False
            break
    if not flag:
        print(x)
        primenumber.append(x)