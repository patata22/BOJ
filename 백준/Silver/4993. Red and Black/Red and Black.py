from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=1
    cnt=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]=='.' and not visited[nx][ny]:
                visited[nx][ny]=1
                q.append((nx,ny))
                cnt+=1
    return cnt

while True:
    m,n=map(int,input().split())
    if not n: break
    board=[]
    for x in range(n):
        temp=list(input())
        for y in range(m):
            if temp[y]=='@':
                sx,sy=x,y
                temp[y]='.'
        board.append(temp)
    visited=[[0]*m for i in range(n)]
    print(sol())
    
                
    
