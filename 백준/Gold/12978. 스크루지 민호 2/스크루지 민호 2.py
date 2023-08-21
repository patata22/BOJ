import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(now):
    visited[now]=1
    for to in graph[now]:
        if not visited[to]:
            dfs(to)
            dp[now][0]+=dp[to][1]
            dp[now][1]+=min(dp[to])
    

n=int(input())
graph=[[] for i in range(n+1)]
visited=[0]*(n+1)
dp=[[0,1] for i in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(min(dp[1]))
