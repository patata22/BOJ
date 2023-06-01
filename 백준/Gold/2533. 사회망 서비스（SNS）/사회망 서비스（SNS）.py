import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)

def sol(now):
    for to in graph[now]:
        if not visited[to]:
            visited[to]=1
            sol(to)
            dp[now][0]+=min(dp[to])
            dp[now][1]+=dp[to][0]
            
n=int(input())
graph=[[] for i in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[0]*(n+1)
visited[1]=1
dp=[[1,0] for i in range(n+1)]
sol(1)
print(min(dp[1]))
