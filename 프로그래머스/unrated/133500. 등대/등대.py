import sys
sys.setrecursionlimit(10**6)

def solution(n, lighthouse):
    graph=[[] for i in range(n+1)]
    for a,b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
    visited=[0]*(n+1)
    dp=[[1,0] for i in range(n+1)]
    def sol(now):
        for to in graph[now]:
            if not visited[to]:
                visited[to]=1
                sol(to)
                dp[now][0]+=min(dp[to])
                dp[now][1]+=dp[to][0]
    visited[1]=1
    sol(1)
    return min(dp[1])