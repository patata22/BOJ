n,m=map(int,input().split())
point=[]
for _ in range(n):
    temp=tuple(map(int,input().split()))
    for __ in range(m):
        if temp[__]==1:point.append((_,__))
print(abs(point[0][0]-point[1][0])+abs(point[0][1]-point[1][1]))
