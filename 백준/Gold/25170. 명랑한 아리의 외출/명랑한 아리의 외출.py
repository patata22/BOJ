dx=(-1,-1,0)
dy=(-1,0,-1)

n,m,T=map(int,input().split())

work=[tuple(map(int,input().split())) for i in range(n)]
time=[tuple(map(int,input().split())) for i in range(n)]
board=[[[-float('inf')]*(T+1) for i in range(m)] for i in range(n)]

board[0][0][0]=0

for i in range(1,m):
    tt=time[0][i]+1
    for t in range(1,T+1):
        board[0][i][t]=max(board[0][i][t],board[0][i-1][t-1])
        if work[0][i] and t>=tt:
            board[0][i][t]=max(board[0][i][t],board[0][i-1][t-tt]+work[0][i])

for i in range(1,n):
    tt=time[i][0]+1
    for t in range(1,T+1):
        board[i][0][t]=max(board[i][0][t],board[i-1][0][t-1])
        if work[i][0] and t>=tt:
            board[i][0][t]=max(board[i][0][t],board[i-1][0][t-tt]+work[i][0])
            

for x in range(1,n):
    for y in range(1,m):
        tt=time[x][y]+1
        for t in range(1,T+1):
            for d in range(3):
                nx,ny=x+dx[d],y+dy[d]
                board[x][y][t]=max(board[x][y][t],board[nx][ny][t-1])
                if work[x][y] and t>=tt:
                    board[x][y][t]=max(board[x][y][t],board[nx][ny][t-tt]+work[x][y])

print(max(board[-1][-1]))
        
