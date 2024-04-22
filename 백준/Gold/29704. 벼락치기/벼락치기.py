n,t=map(int,input().split())
problem=[tuple(map(int,input().split())) for i in range(n)]

answer=0
for d,c in problem:answer+=c

dp=[[0]*(t+1) for i in range(n)]
for i in range(n):
    day,cost=problem[i]
    for j in range(t+1):
        if day>j: dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-day]+cost)
print(answer-dp[-1][-1])
