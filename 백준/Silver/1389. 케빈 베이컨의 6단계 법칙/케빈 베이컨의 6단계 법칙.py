from collections import deque

def bfs(v):
    q=deque([[v,0]])
    visited[v]=1
    bacon=0
    while q:
        p=q.popleft()
        v,t=p[0],p[1]
        t+=1
        for i in range(1,n+1):
            if graph[v][i]==1 and visited[i]==0:
                visited[i]=1
                bacon+=t
                q.append([i,t])
    return bacon

n,m=map(int,input().split())
graph=[[0]*(n+1) for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=1
minbacon=10000
answer=0
for i in range(1,n+1):
    visited=[0 for i in range(n+1)]
    x=bfs(i)
    if x<minbacon:
        minbacon=x
        answer=i
print(answer)