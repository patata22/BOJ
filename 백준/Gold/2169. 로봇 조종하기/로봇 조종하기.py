n,m=map(int,input().split())

board=[tuple(map(int,input().split())) for i in range(n)]

dp=[[0]*m for i in range(n)]
for i in range(m):
    dp[0][i]=dp[0][i-1]+board[0][i]

for i in range(1,n):
    tempL=[-float('inf')]*m
    for j in range(m):
        tempL[j]=max(tempL[j-1],dp[i-1][j])+board[i][j]
    tempR=[-float('inf')]*m
    tempR[-1]=dp[i-1][-1]+board[i][-1]
    for j in range(m-2,-1,-1):
        tempR[j]=max(tempR[j+1],dp[i-1][j])+board[i][j]
    for j in range(m):
        dp[i][j]=max(tempL[j],tempR[j])

print(dp[-1][-1])
