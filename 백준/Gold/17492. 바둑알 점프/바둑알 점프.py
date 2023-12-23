dx=(-1,-1,-1,0,0,1,1,1)
dy=(-1,0,1,-1,1,-1,0,1)

def sol(depth):
    global answer
    if depth==total-1:
        answer='Possible'
        return
    for x in range(n):
        for y in range(n):
            if board[x][y]==2:
                for i in range(8):
                    nx,ny=x+dx[i],y+dy[i]
                    nnx,nny=x+2*dx[i],y+2*dy[i]
                    if 0<=nx<n and 0<=ny<n and board[nx][ny]==2 and 0<=nnx<n and 0<=nny<n and board[nnx][nny]==0:
                        board[x][y]=0
                        board[nx][ny]=0
                        board[nnx][nny]=2
                        sol(depth+1)
                        board[nnx][nny]=0
                        board[nx][ny]=2
                        board[x][y]=2
n=int(input())
board=[list(map(int,input().split())) for i in range(n)]
total=0
for i in range(n):
    for j in range(n):
        if board[i][j]==2: total+=1

answer='Impossible'
sol(0)
print(answer)
