from collections import deque
import sys
input=sys.stdin.readline

def sol():
    q=deque()
    q.append(r)
    visited[r]=1
    answer=0
    d=1
    t=1
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            for x in graph[now]:
                if not visited[x]:
                    visited[x]=1
                    q.append(x)
                    t+=1
                    answer+=d*t
        d+=1
    return answer

n,m,r=map(int,input().split())
visited=[0]*(n+1)
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n+1):graph[i].sort()

print(sol())
