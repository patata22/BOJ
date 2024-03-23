import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline


def sol(x):
    visited[x]=1
    dp[x][0]+=white[x]
    dp[x][1]+=black[x]
    for to in graph[x]:
        if not visited[to]:
            sol(to)
            dp[x][0]+=min(dp[to])
            dp[x][1]+=dp[to][0]
            
n=int(input())
graph=[[] for i in range(n)]
visited=[0]*n
for _ in range(n-1):
   a,b=map(int,input().split())
   graph[a].append(b)
   graph[b].append(a)
#0=white 1=black
dp=[[0]*2 for i in range(n)]
white=[0]*n
black=[0]*n
for i in range(n):
    w,b=map(int,input().split())
    white[i]=w
    black[i]=b

sol(0)
print(min(dp[0]))