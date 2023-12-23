dx=(-1,1,0,0)
dy=(0,0,-1,1)

board=[list(input()) for i in range(7)]
answer=0
for x in range(7):
    for y in range(7):
        if board[x][y]=='o':
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                nnx,nny=x+2*dx[i],y+2*dy[i]
                if 0<=nx<7 and 0<=ny<7 and 0<=nnx<7 and 0<=nny<7:
                    if board[nx][ny]=='o' and board[nnx][nny]=='.':answer+=1
print(answer)