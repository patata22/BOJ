import sys,heapq
input=sys.stdin.readline

def calc(i):
    result=0
    for a,b,dist in graph:
        a = distance[i][a]
        b = distance[i][b]
        if a>b: a,b=b,a
        if b-a>=dist:
            result=max(result,a+dist)
        else:
            temp=b
            gap=b-a
            dist-=gap
            temp+=dist//2
            result=max(result,temp)
    return result

n,m=map(int,input().split())
distance=[[float('inf')]*n for i in range(n)]
graph=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    graph.append((a,b,2*c))
for a,b,c in graph:
    distance[a][b]=min(distance[a][b],c)
    distance[b][a]=min(distance[b][a],c)

for i in range(n):
    distance[i][i]=0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]

answer=float('inf')
for i in range(n):
    answer=min(answer,calc(i))
print(answer/2)
