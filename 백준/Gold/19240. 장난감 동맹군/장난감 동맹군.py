from collections import deque
import sys
input=sys.stdin.readline


def sol(x):
    q=deque()
    q.append(x)
    visited[x]=1
    t=0
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            for to in graph[now]:
                if visited[to]==-1:
                    visited[to]=t
                    q.append(to)
                else:
                    if visited[to]==1-t:
                        return 0
        t=1-t
    return 1

for tt in range(int(input())):
    n,m=map(int,input().split())
    graph=[[] for i in range(n+1)]
    answer=1
    for _ in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited=[-1]*(n+1)
    for i in range(1,n+1):
        if visited[i]==-1:
            answer&=sol(i)
    if answer:print('YES')
    else: print('NO')
