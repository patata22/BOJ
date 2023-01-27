n=int(input())

food = [int(input()) for i in range(n)]

dp=[[0]*3 for i in range(n)]
dp[0][1]=food[0]
for i in range(1,n):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0]+food[i]
    dp[i][2] = dp[i-1][1]+food[i]//2

print(max(dp[-1]))
