dx=(-1,0,1)

n,m=map(int,input().split())

board=[]
for i in range(n):
    temp=list(input())
    for j in range(m):
        if temp[j]=='R':
            temp[j]='.'
            sx,sy=i,j
    board.append(temp)

dp=[[-float('inf')]*m for i in range(n)]
dp[sx][sy]=0
door=set()
for j in range(sy+1,m):
    for i in range(n):
        if board[i][j]=='#':continue
        for k in range(3):
            x,y=i+dx[k],j-1
            if 0<=x<n and 0<=y<m:
                if board[i][j]=='C':
                    dp[i][j]=max(dp[i][j],dp[x][y]+1)
                else:
                    dp[i][j]=max(dp[i][j],dp[x][y])
            if board[i][j]=='O' and dp[i][j]!=-float('inf'):
                door.add((i,j))

if not door: print(-1)
else:
    answer=0
    for x,y in door:
        answer=max(answer,dp[x][y])
    print(answer)