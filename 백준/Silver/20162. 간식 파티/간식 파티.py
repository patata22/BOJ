n=int(input())
number=[int(input()) for i in range(n)]
dp=[[0]*(100001) for i in range(n)]

for i in range(n):
    num=number[i]
    for j in range(num):
        dp[i][j]=dp[i-1][j]
        dp[i][num]=max(dp[i][num],dp[i-1][j]+num)
    for j in range(num+1,100001):
        dp[i][j]=dp[i-1][j]
        dp[i][num]=max(dp[i][num],dp[i-1][num])
print(max(dp[-1]))