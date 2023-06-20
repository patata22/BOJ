from collections import deque

import sys
input=sys.stdin.readline


def sol(l,r):
    q=deque()
    q.append(l)
    visited=[0]*(n+1)
    visited[l]=1
    count=1
    while q:
        now=q.popleft()
        for to in graph[now]:
            if now==l and to==r: continue
            if not visited[to]:
                visited[to]=1
                count+=1
                q.append(to)
    return count
        
    

n,m,k=map(int,input().split())
graph=[[] for i in range(n+1)]
for i in range(1,m+1):
    a,b=map(int,input().split())
    if i==k: l,r=a,b
    graph[a].append(b)
    graph[b].append(a)

print((n-sol(l,r))*(n-sol(r,l)))
