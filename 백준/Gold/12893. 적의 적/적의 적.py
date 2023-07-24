from collections import deque
import sys
input=sys.stdin.readline

def bfs(now):
    global answer
    if not answer: return
    q=deque()
    q.append(now)
    visited[now]=0
    t=1
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            for to in graph[now]:
                if visited[to]==-1:
                    visited[to]=t
                    q.append(to)
                elif visited[to]==1-t:
                    answer=0
                    return
        t=1-t
n,m=map(int,input().split())

graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[-1]*(n+1)
answer=1
for i in range(1,n+1):
    if visited[i]==-1:
        bfs(i)
print(answer)