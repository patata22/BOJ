from collections import deque
import sys
input=sys.stdin.readline

n,w=map(int,input().split())

graph=[[] for i in range(n+1)]
cnt=0
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[0]*(n+1)
q=deque()
q.append(1)
visited[1]=1

while q:
    now = q.popleft()
    flag=False
    for to in graph[now]:
        if not visited[to]:
            visited[to]=1
            q.append(to)
            flag=True
    if not flag: cnt+=1

print(w/cnt)
