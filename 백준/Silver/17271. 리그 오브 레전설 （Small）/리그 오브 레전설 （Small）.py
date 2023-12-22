DIV=10**9+7

n,m=map(int,input().split())
dp=[0]*(n+1)
dp[0]=1
for i in range(1,n+1):
    dp[i]=dp[i-1]
    if i>=m:dp[i]+=dp[i-m]
    dp[i]%=DIV
print(dp[-1])
