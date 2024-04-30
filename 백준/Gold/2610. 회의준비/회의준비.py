import sys
input=sys.stdin.readline
from collections import deque

def sol(x):
    q=deque()
    q.append(x)
    visited[x]=1
    member=[]
    member.append(x)
    while q:
        now=q.popleft()
        for to in graph[now]:
            if not visited[to]:
                visited[to]=1
                member.append(to)
                q.append(to)
    answer=float('inf')
    leader=0
    for x in member:
        temp=0
        for y in member:
            temp=max(temp,distance[x][y])
        if temp<answer:
            answer=temp
            leader=x
    return leader
        
n=int(input())
m=int(input())
graph=[[] for i in range(n+1)]
distance=[[float('inf')]*(n+1) for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    distance[a][b]=1
    distance[b][a]=1

for i in range(1,n+1):
    distance[i][i]=0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]

visited=[0]*(n+1)
leader=[]
for i in range(1,n+1):
    if not visited[i]:
        leader.append(sol(i))
leader.sort()
print(len(leader))
print(*leader, sep='\n')
