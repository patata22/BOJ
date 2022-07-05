dx=(-1,1,0,0)
dy=(0,0,-1,1)

r,c=map(int,input().split())
board=[]
wolf=[]
for i in range(r):
    x=list(input())
    for j in range(c):
        if x[j]=='W':
            wolf.append((i,j))
        elif x[j]=='.':x[j]='D'
    board.append(x)

catch=False
for x,y in wolf:
    if catch:break
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<r and 0<=ny<c:
            if board[nx][ny]=='S':
                catch=True
                break

if catch:print(0)
else:
    print(1)
    for i in range(r):
        print(*board[i],sep='')
