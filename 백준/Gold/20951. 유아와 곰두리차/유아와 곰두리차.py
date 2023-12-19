import sys
input=sys.stdin.readline

DIV=10**9+7

def sol(now,depth):
    if dp[now][depth]>=0: return dp[now][depth]
    dp[now][depth]=0
    for to in graph[now]:
        dp[now][depth]+=sol(to,depth-1)%DIV
    return dp[now][depth]%DIV

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dp=[[-1]*8 for i in range(n+1)]
for i in range(1,n+1): dp[i][0]=1
answer=0
for i in range(1,n+1):
    answer+=sol(i,7)
print(answer%DIV)
