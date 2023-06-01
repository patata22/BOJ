import sys
input=sys.stdin.readline
from collections import deque

def bfs(i):
    q=deque()
    q.append(i)
    node_count=0
    graph_count=len(graph[i])
    while q:
        now=q.popleft()
        for to in graph[now]:
            if not visited[to]:
                visited[to]=1
                node_count+=1
                graph_count+=len(graph[to])
                q.append(to)
    graph_count//=2
    return graph_count-node_count

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[0]*(n+1)

connect=-1
cut=0
for i in range(1,n+1):
    if not visited[i]:
        visited[i]=1
        connect+=1
        cut+=bfs(i)

print(connect+cut)
    
