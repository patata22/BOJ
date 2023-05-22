dx=(-1,1,0,0)
dy=(0,0,-1,1)

def dfs(x,y,pipe,before):
    total=0
    visited[x][y]=1
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            if i==before and pipe:
                total=max(total,dfs(nx,ny,pipe-1,i))
            elif i!=before and pipe>1:
                total=max(total,dfs(nx,ny,pipe-2,i))
    visited[x][y]=0
    return board[x][y]+total
                


n,m=map(int,input().split())
board=[tuple(map(int,input().split())) for i in range(n)]
visited=[[0]*m for i in range(n)]
sx,sy,p=map(int,input().split())
visited[sx][sy]=1

print(dfs(sx,sy,p+1,-1))
