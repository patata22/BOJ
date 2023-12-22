dx=(-1,0)
dy=(0,-1)

n,m=map(int,input().split())
board=[[0]*301 for i in range(301)]
for _ in range(n):
    a,b=map(int,input().split())
    board[a][b]=m

for x in range(301):
    for y in range(301):
        temp=0
        for i in range(2):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<301 and 0<=ny<301:
                temp=max(temp,board[nx][ny])
        board[x][y]=max(0,board[x][y]-x-y)+temp
        
print(board[-1][-1])
        
        