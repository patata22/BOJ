dx=(1,0,-1,0)
dy=(0,1,0,-1)

m,n=map(int,input().split())
k=int(input())
if n*m<k: print(0)
else:
    board=[[0]*m for i in range(n)]
    d=0
    x,y=0,0
    for i in range(1,k):
        board[x][y]=i
        nx,ny=x+dx[d],y+dy[d]
        if not (0<=nx<n and 0<=ny<m) or board[nx][ny]:
            d=(d+1)%4
        x+=dx[d]
        y+=dy[d]
    print(y+1,x+1)
