dx = (0,0,1,-1)
dy = (1,-1,0,0)

def sol(x,y,t):
    if t==n: return 1
    temp = 0
    visited[x][y] = 1
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if not visited[nx][ny]:
            visited[nx][ny]=1
            temp+=dz[i]*sol(nx,ny,t+1)
            visited[nx][ny]=0
    return temp


n, E,W,S,N = map(int,input().split())
dz = (E/100, W/100, S/100, N/100)
visited = [[0]*30 for i in range(30)]


print(sol(15,15,0))
