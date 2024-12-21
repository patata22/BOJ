import sys
input=sys.stdin.readline

n,t=map(int,input().split())
special=[0]*n
city=[]
for i in range(n):
    s,x,y=map(int,input().split())
    special[i]=s
    city.append((x,y))

distance=[[float('inf')]*n for i in range(n)]

for i in range(n):
    distance[i][i]=0
    x1,y1=city[i]
    for j in range(i+1,n):
        x2,y2=city[j]
        dist=abs(x1-x2)+abs(y1-y2)
        if special[i] and special[j]:
            distance[i][j]=distance[j][i]=min(dist,t)
        else: distance[i][j]=distance[j][i]=dist

for k in range(n):
    for i in range(n):
        for j in range(i+1,n):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]
                distance[j][i]=distance[i][j]

for _ in range(int(input())):
    a,b=map(int,input().split())
    print(distance[a-1][b-1])