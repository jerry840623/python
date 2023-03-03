# triangle = [[1],[1,1]]
# n=10
# for i in range(2,n):
#     pre = triangle[i-1]
#     cur = [1]
#     for j in range (0,i-1):
#         cur.append(pre[j]+pre[j+1])
#     cur.append(1)
#     triangle.append(cur)
#     print(triangle[i])


triangle=[]
n=int(input('>>>>>>>'))
for i in range(n):
    row=[1]
    triangle.append(row)
    if i == 0:
        print (triangle[0])
        continue
    for j in range(i-1):
        row.append(triangle[i-1][j]+triangle[i-1][j+1])
    row.append(1)
    print(triangle[i])