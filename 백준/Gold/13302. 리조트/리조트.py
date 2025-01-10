n,m=map(int,input().split())
temp=[]
if m: temp=set(map(int,input().split()))


dp=[[float('inf')]*41 for i in range(n+1)]
dp[0][0]=0
for i in range(1,n+1):
    if i in temp:
        for j in range(41):
            dp[i][j]=min(dp[i][j],dp[i-1][j])
    for j in range(41):
        if j>=3: dp[i][j-3]=min(dp[i][j-3],dp[i-1][j])
        dp[i][j]=min(dp[i][j],dp[i-1][j]+10000)
    if i>=5:
        for j in range(2,41):
            dp[i][j]=min(dp[i][j],dp[i-5][j-2]+37000)
    if i>=3:
        for j in range(1,41):
            dp[i][j]=min(dp[i][j],dp[i-3][j-1]+25000)
                    
print(min(dp[-1]))
