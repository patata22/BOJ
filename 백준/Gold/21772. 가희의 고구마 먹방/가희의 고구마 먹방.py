dx=(0,0,-1,1)
dy=(-1,1,0,0)

def sol(time, eat, x, y):
    global answer
    
    if time==t:
        answer=max(answer,eat)
        return

    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and board[nx][ny]!='#':
            #visited[nx][ny]=1
            if board[nx][ny]=='S':
                board[nx][ny]='.'
                sol(time+1, eat+1, nx, ny)
                board[nx][ny]='S'
            elif board[nx][ny]=='.':
                sol(time+1,eat,nx,ny)
            #visited[nx][ny]=0
            
n,m,t=map(int,input().split())
board=[]
for i in range(n):
    x=list(input())
    for j in range(m):
        if x[j]=='G':
            x[j]='.'
            X,Y=i,j
    board.append(x)
#visited=[[0]*m for i in range(n)]
answer=0
#visited[X][Y]=1
sol(0,0,X,Y)
print(answer)
