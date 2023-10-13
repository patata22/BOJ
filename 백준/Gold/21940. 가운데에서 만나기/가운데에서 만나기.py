import sys
input=sys.stdin.readline

n,m=map(int,input().split())

distance=[[float('inf')]*n for i in range(n)]

for i in range(n):
    distance[i][i]=0
for _ in range(m):
    a,b,c=map(int, input().split())
    distance[a-1][b-1]=c


for k in range(n):
    for i in range(n):
        for j in range(n):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]

k=map(int,input().split())
start=tuple(map(lambda x:int(x)-1,input().split()))

answer=[]
minDistance=float('inf')

for i in range(n):
    temp=0
    for s in start:
        temp = max(temp,distance[s][i]+distance[i][s])
        
    if temp<minDistance:
        answer=[i+1]
        minDistance=temp
    elif temp==minDistance:answer.append(i+1)

answer.sort()
print(*answer)
