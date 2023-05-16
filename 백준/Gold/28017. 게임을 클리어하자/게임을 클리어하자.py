n,m=map(int,input().split())
board=[tuple(map(int,input().split())) for i in range(n)]

dp=[[0]*m for i in range(n)]
dp[0]=board[0]
for i in range(1,n):
    for j in range(m):
        temp=float('inf')
        for k in range(m):
            if j==k: continue
            temp=min(temp,dp[i-1][k])
        dp[i][j]=temp+board[i][j]
                    
        
print(min(dp[-1]))
