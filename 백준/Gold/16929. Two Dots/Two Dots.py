dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol(bx,by,x,y):
    visited[x][y]=1
    global answer
    if answer: return
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx==bx and ny==by: continue
        if 0<=nx<n and 0<=ny<m and board[nx][ny]==board[x][y]:
            if visited[nx][ny] and not finished[nx][ny]:
                answer=1
                return
            if not visited[nx][ny]: sol(x,y,nx,ny)
            

    finished[x][y]=1
        

n,m=map(int,input().split())
board=[list(input()) for i in range(n)]
visited=[[0]*m for i in range(n)]
finished=[[0]*m for i in range(n)]
answer=0
a=['No','Yes']

for i in range(n):
    for j in range(m):
        if not visited[i][j]: sol(-1,-1,i,j)
print(a[answer])
