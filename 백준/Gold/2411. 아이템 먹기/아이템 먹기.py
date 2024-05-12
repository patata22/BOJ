n,m,a,b=map(int,input().split())

board=[[0]*m for i in range(n)]

dp=[[[0]*200 for i in range(m)] for i in range(n)]

for _ in range(a):
    x,y=map(int,input().split())
    board[x-1][y-1]=1
for _ in range(b):
    x,y=map(int,input().split())
    board[x-1][y-1]=2

if board[0][0]==1: dp[0][0][1]=1
else: dp[0][0][0]=1

for i in range(1,m):
    if board[0][i]==2: continue
    elif board[0][i]==1:
        for k in range(1,200):
            dp[0][i][k]+=dp[0][i-1][k-1]
    else:
        for k in range(200):
            dp[0][i][k]+=dp[0][i-1][k]

for i in range(1,n):
    if board[i][0]==2: continue
    elif board[i][0]==1:
        for k in range(1,200):
            dp[i][0][k]+=dp[i-1][0][k-1]
    else:
        for k in range(200):
            dp[i][0][k]+=dp[i-1][0][k]
    
for i in range(1,n):
    for j in range(1,m):
        if board[i][j]==2: continue
        elif board[i][j]==1:
            for k in range(1,200):
                dp[i][j][k]+=dp[i][j-1][k-1]+dp[i-1][j][k-1]
        else:
            for k in range(200):
                dp[i][j][k]+=dp[i][j-1][k]+dp[i-1][j][k]

print(dp[-1][-1][a])
        