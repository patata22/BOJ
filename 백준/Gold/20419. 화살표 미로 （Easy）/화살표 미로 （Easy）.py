#20419


from collections import deque

dx=(-1,0,1,0)
dy=(0,1,0,-1)
di={'R':1, 'L':3, 'U':0,'D':2}

def sol():
    q=deque()
    q.append((0,0,k,k))
    visited[0][0][k][k]=1
    while q:
        x,y,l,r = q.popleft()
        if x==R-1 and y==c-1: return 'Yes'
        i=di[board[x][y]]
        nx, ny= x+dx[i], y+dy[i]
        if 0<=nx<R and 0<=ny<c and not visited[nx][ny][l][r]:
            visited[nx][ny][l][r]=1
            q.append((nx,ny,l,r))
        if l>0:
            ni= (i-1)%4
            nx,ny= x+dx[ni],y+dy[ni]
            if 0<=nx<R and 0<=ny<c and not visited[nx][ny][0][r]:
                visited[nx][ny][0][r]=1
                q.append((nx,ny,0,r))
        if r>0:
            ni=(i+1)%4
            nx,ny=x+dx[ni],y+dy[ni]
            if 0<=nx<R and 0<=ny<c and not visited[nx][ny][l][0]:
                visited[nx][ny][l][0]=1
                q.append((nx,ny,l,0))
    return 'No'
            
R,c,k = map(int,input().split())
board = [tuple(input()) for i in range(R)]
visited=[[[[0]*2 for i in range(2)] for i in range(c)] for i in range(R)]
print(sol())
