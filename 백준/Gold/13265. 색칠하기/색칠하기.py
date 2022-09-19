#13265

from collections import deque
import sys
input=sys.stdin.readline


def sol(x):
    global answer
    q=deque()
    q.append(x)
    color=-1
    visited[x]=1
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            for x in graph[now]:
                if visited[x]==visited[now]:
                    answer='impossible'
                    return
                elif not visited[x]:
                    visited[x]=color
                    q.append(x)
        color*=-1


for _ in range(int(input())):
    answer='possible'
    n,m=map(int,input().split())
    graph=[[] for i in range(n+1)]
    for i in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited=[0]*(n+1)
    for i in range(1,n+1):
        if answer=='impossible': break
        if not visited[i]: sol(i)
    print(answer)
