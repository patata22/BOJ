n,t=map(int,input().split())

dp=[[0]*(t+1) for i in range(n)]
cost=[]
score=[]
for i in range(n):
    a,b=map(int,input().split())
    cost.append(a)
    score.append(b)
for i in range(n):
    for j in range(t+1):
        c=cost[i]
        s=score[i]
        if c>j:dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j-c]+s, dp[i-1][j])

print(dp[-1][-1])
