DIV=1000000007

dp=[0]*1000001
dp[0]=1
dp[1]=2
dp[2]=7
dp[3]=22
n=int(input())
for i in range(4,n+1):
    dp[i]=(3*dp[i-1]+dp[i-2]-dp[i-3])%DIV
print(dp[n])
