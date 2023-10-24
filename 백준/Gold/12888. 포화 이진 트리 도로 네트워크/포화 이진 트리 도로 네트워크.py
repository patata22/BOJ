n=int(input())
if n==0 or n==1: print(1)
else:
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=3
    for i in range(3,n+1):
        if i%2==1: dp[i]=dp[i-1]*2-1
        else: dp[i]=dp[i-1]*2+1
    print(dp[-1])
