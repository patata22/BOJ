n,k=map(int,input().split())
number=tuple(map(int,input().split()))

dp=[[0]*2 for i in range(n)]
dp[0][0]=1
answer=0
for i in range(1,n):
    if number[i-1]<=k:
        dp[i][0]=dp[i-1][0]+1
        dp[i][1]=dp[i-1][1]+1
    else:
        answer=max(answer,dp[i-1][0],dp[i-1][1])
        dp[i][0]=1
        dp[i][1]=dp[i-1][0]+1
        

answer=max(max(dp[-1]),answer)
print(answer)
    
        
