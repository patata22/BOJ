n,k=map(int,input().split())
number=tuple(map(int,input().split()))
dp=[[0]*(k+1) for i in range(n)]
for i in range(n):
    if not number[i]%2:
        for j in range(k+1):
            dp[i][j]=dp[i-1][j]+1
    else:
        for j in range(1,k+1):
            dp[i][j]=dp[i-1][j-1]
answer=0
for i in range(n):
    for j in range(k+1):
        answer=max(answer,dp[i][j])
print(answer)
