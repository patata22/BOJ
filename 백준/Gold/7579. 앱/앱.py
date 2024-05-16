n,M=map(int,input().split())
memory=tuple(map(int,input().split()))
cost=tuple(map(int,input().split()))
C=sum(cost)+1
dp=[[0]*C for i in range(n)]
answer=float('inf')
for i in range(n):
    m,c=memory[i],cost[i]
    for j in range(C):
        if j<c:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-c]+m)
        if dp[i][j]>=M:
            answer=min(answer,j)

print(answer)
