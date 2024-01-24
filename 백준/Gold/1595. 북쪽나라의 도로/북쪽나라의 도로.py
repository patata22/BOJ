import sys
from collections import deque

def sol():
    q=deque()
    q.append(1)
    visited=[-1]*10001
    visited[1]=0
    while q:
        now=q.popleft()
        for to,d in graph[now]:
            if visited[to]==-1:
                visited[to] = visited[now]+d
                q.append(to)
    x=visited.index(max(visited))
    visited=[-1]*10001
    visited[x]=0
    q.append(x)
    while q:
        now=q.popleft()
        for to,d in graph[now]:
            if visited[to]==-1:
                visited[to]=visited[now]+d
                q.append(to)
    return max(visited)  

graph=[[] for i in range(10001)]
while True:
    try:
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    except:
        break
print(sol())