n,k=map(int,input().split())
item=[(0,0)]
for _ in range(n):
    item.append(tuple(map(int,input().split())))

dp=[[0]*(k+1) for i in range(n+1)]

for i in range(1,n+1):
    w,v=item[i]
    for j in range(k+1):
        if j<w:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j-w]+v,dp[i-1][j])
print(dp[-1][-1])
