n=int(input())
dp=[0]*(n+1)
dp[1]=1
for i in range(2,n+1):
    if i%2==0: dp[i]=dp[i-1]*2
    else: dp[i]=2*dp[i-1]-1

if n%2:print((dp[n]-1)//2)
else:print(dp[n]//2)