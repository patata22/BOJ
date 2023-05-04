n,a,b=map(int,input().split())
dp=[i for i in range(n+1)]
for i in range(1,n+1):
    for x in (a+1,b+1):
        if i-x>=0:
            dp[i] = min(dp[i],dp[i-x]+1)
print(dp[-1])
