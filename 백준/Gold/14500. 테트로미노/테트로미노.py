dx=(-1,1,0,0)
dy=(0,0,-1,1)


def sol(x,y,cnt,total):
    global answer
    if cnt==3:
        answer=max(answer,total)
        return
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny]=1
            sol(nx,ny,cnt+1,total+board[nx][ny])
            visited[nx][ny]=0

def sol2(x,y):
    global answer
    for k in range(4):
        temp=board[x][y]
        for i in range(4):
            if i==k: continue
            nx,ny=x+dx[i],y+dy[i]
            if not (0<=nx<n and 0<=ny<m): break
            temp+=board[nx][ny]
        answer=max(temp,answer)


n,m=map(int,input().split())
board=[list(map(int,input().split())) for i in range(n)]
visited=[[0]*m for i in range(n)]
answer=0

for x in range(n):
    for y in range(m):
        visited[x][y]=1
        sol(x,y,0,board[x][y])
        visited[x][y]=0
        sol2(x,y)
print(answer)
