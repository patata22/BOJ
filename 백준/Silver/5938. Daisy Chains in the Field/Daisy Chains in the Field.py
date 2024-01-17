from collections import deque

n,m=map(int,input().split())

graph=[[] for i in range(n+1)]
visited=[0]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q=deque()
q.append(1)
visited[1]=1
while q:
    now=q.popleft()
    for to in graph[now]:
        if not visited[to]:
            visited[to]=1
            q.append(to)
if sum(visited)==n:
    print(0)
else:
    for i in range(1,n+1):
        if not visited[i]:print(i)
