from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append((sx,sy))
    visited=[[0]*m for i in range(n)]
    visited[sx][sy]=1
    answer=1
    while q:
        x,y=q.popleft()
        
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]=='.' and not visited[nx][ny]:
                visited[nx][ny]=1
                q.append((nx,ny))
                answer+=1
    return answer

while True:
    m,n=map(int,input().split())
    if not n: break
    board=[]
    for i in range(n):
        temp=list(input())
        for j in range(m):
            if temp[j]=='A':
                sx,sy=i,j
        board.append(temp)
    print(sol())
