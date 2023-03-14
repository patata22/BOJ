import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(now, depth):
    visited[now]=depth
    for to in graph[now]:
        if visited[to]<0:
            dfs(to,depth+1)
    


n,m,r=map(int,input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[-1]*(n+1)
for _ in range(n+1):
    graph[_].sort()

dfs(r,0)

for i in range(1,n+1):print(visited[i])
