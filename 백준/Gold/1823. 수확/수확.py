import sys
input=sys.stdin.readline

n=int(input())
number=[0]+[int(input()) for i in range(n)]

dp=[[0]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    dp[i][0]=dp[i-1][0]+i*number[i]

for j in range(1,n+1):
    dp[0][j]=dp[0][j-1]+j*number[-j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>n: break
        dp[i][j]=max(dp[i-1][j]+number[i]*(i+j),dp[i][j-1]+number[-j]*(i+j))

answer=0

for i in range(n+1):
    for j in range(n+1):
        answer=max(answer,dp[i][j])
print(answer)
