import sys
input=sys.stdin.readline

def sol(now,prev,prev2):
    visited[now]=1
    for to in graph[now]:
        if to == prev2:
            global answer
            temp=len(graph[to])+len(graph[prev])+len(graph[now])-6
            answer=min(answer,temp)
        elif not visited[to]:
            sol(to,now,prev)

n,m=map(int,input().split())
adj=[[0]*(n+1) for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    adj[a][b]=1
    adj[b][a]=1

answer=float('inf')
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if adj[i][j]:
            for k in range(j+1,n+1):
                if adj[i][k] and adj[j][k]:
                    answer=min(answer,sum(adj[i])+sum(adj[j])+sum(adj[k])-6)

if answer==float('inf'):print(-1)
else:print(answer)
