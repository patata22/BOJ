n=int(input())
number=list(map(int,input().split()))

dp=[[0]*2 for i in range(n)]
dp[0][0]=number[0]
dp[0][1]=-float('inf')
for i in range(1,n):
    dp[i][0]=max(dp[i-1][0]+number[i], number[i])
    dp[i][1]=max(dp[i-1][0],dp[i-1][1]+number[i])

answer=-float('inf')
for i in range(n):
    answer=max(answer,dp[i][0],dp[i][1])
print(answer)
