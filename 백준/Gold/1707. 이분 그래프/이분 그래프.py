from collections import deque
import sys
input=sys.stdin.readline

def sol(x):
    global answer
    q=deque()
    q.append(x)
    visited[x]=0
    t=1
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            for to in graph[now]:
                if visited[to]==-1:
                    visited[to]=t
                    q.append(to)
                else:
                    if visited[to]%2==visited[now]%2: answer='NO'
        t+=1

for tt in range(int(input())):
    n,m=map(int,input().split())
    graph=[[] for i in range(n+1)]
    for _ in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited=[-1]*(n+1)
    answer='YES'
    for i in range(1,n+1):
        if visited[i]==-1: sol(i)
    print(answer)
