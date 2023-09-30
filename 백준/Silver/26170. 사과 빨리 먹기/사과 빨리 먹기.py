dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol(x,y,t,cnt):
    global answer
    visited[x][y]=1
    if cnt==3: answer=min(answer,t)
    else:
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny] and board[nx][ny]!=-1:
                if board[nx][ny]: sol(nx,ny,t+1,cnt+1)
                else: sol(nx,ny,t+1,cnt)
    visited[x][y]=0

board=[list(map(int,input().split())) for i in range(5)]
r,c=map(int,input().split())

visited=[[0]*5 for i in range(5)]
answer=float('inf')
sol(r,c,0,0)
if answer==float('inf'):print(-1)
else:print(answer)
