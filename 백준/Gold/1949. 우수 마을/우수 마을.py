import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)

def sol(now):
    for to in graph[now]:
        if not visited[to]:
            visited[to]=1
            sol(to)
            dp[now][0]+=dp[to][1]
            dp[now][1]+=max(dp[to])
            

n=int(input())
number=tuple(map(int,input().split()))
graph=[[] for i in range(n)]
for _ in range(n-1):
    a,b=map(lambda x: int(x)-1, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp=[[number[i],0] for i in range(n)]
visited=[0]*(n+1)
visited[0]=1
sol(0)
print(max(dp[0]))
