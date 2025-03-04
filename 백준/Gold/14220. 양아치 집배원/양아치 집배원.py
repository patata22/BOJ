n=int(input())
graph=[tuple(map(int,input().split())) for i in range(n)]
dp=[[float('inf')]*n for i in range(n)]

for i in range(n):dp[0][i]=0

for i in range(1,n):
    for now in range(n):
        for prev in range(n):
            if now==prev or not graph[prev][now]: continue
            dp[i][now]=min(dp[i][now], dp[i-1][prev]+graph[prev][now])

answer=min(dp[-1])
if answer==float('inf'): print(-1)
else: print(answer)