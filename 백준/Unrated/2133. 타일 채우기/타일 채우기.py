n=int(input())
if n==1:print(0)
else:
    dp=[0]*(n+1)
    dp[0]=1
    dp[2]=3
    for i in range(4,n+1,2):
        dp[i]=4*dp[i-2]-dp[i-4]
    print(dp[-1])