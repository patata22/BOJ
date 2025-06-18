from collections import deque
import sys
input=sys.stdin.readline

def travel(x):
    q=deque()
    q.append(x)
    visited=[0]*(n+1)
    visited[x]=1
    result[x]+=1
    while q:
        now=q.popleft()
        for to in graph[now]:
            if not visited[to]:
                visited[to]=1
                result[to]+=1
                q.append(to)

k,n,m=map(int,input().split())

start=[int(input()) for _ in range(k)]

graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
result=[0]*(n+1)

for x in start: travel(x)

print(result.count(k))

