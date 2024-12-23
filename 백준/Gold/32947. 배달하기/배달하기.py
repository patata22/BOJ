from collections import deque
import sys
input=sys.stdin.readline

def sol():
    q=deque()
    q.append(s)
    visited=[0]*(n+1)
    visited[s]=1
    for i in range(1,n+1):
        if count[i]==K: visited[i]=1
    t=0
    while q:
        C=cc[t%K]
        for _ in range(len(q)):
            now=q.popleft()
            if now==C:
                q.append(now)
                continue
            if now==e: return t
            for to in graph[now]:
                if not visited[to]:
                    visited[to]=1
                    q.append(to)
        t+=1
    return -1

n,m=map(int,input().split())
s,e=map(int,input().split())
K=int(input())
cc=tuple(map(int,input().split()))
count=[0]*(n+1)
for x in cc: count[x]+=1

graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(sol())
