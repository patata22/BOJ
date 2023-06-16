import sys
input=sys.stdin.readline
from collections import deque


def getDist():
    q=deque()
    q.append(n)
    distance[n]=0
    t=1
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            for to,c in graph[now]:
                if distance[to]==-1:
                    distance[to]=t
                    q.append(to)
        t+=1
    return distance[1]

def sol():
    q=deque()
    q.append(1)
    visited=[0]*(n+1)
    visited[1]=1
    color=[]
    while q:
        temp = float('inf')
        for _ in range(len(q)):
            now=q.popleft()
            for to,c in graph[now]:
                if distance[now]==distance[to]+1:
                    temp=min(temp,c)
            q.append(now)
        if temp==float('inf'): return color
        color.append(temp)
        for _ in range(len(q)):
            now=q.popleft()
            for to,c in graph[now]:
                if distance[now]==distance[to]+1 and c==temp and not visited[to]:
                    visited[to]=1
                    q.append(to)

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

for i in range(n+1):
    graph[i].sort(key=lambda x: x[1])

distance=[-1]*(n+1)
print(getDist())
print(*sol())
