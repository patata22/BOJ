from collections import deque

dx=(-1,-1,-1,0,0,1,1)
dy=(-1,0,1,-1,1,-1,1)

def sol():
    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=1
    answer=0
    while q:
        x,y=q.popleft()
        
        for i in range(7):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and board[nx][ny]=='.' and not visited[nx][ny]:
                visited[nx][ny]=1
                answer+=1
                q.append((nx,ny))
    return answer

n=int(input())
board=[]
for i in range(n):
    x=list(input())
    for j in range(n):
        if x[j]=='F': sx,sy=i,j

    board.append(x)

visited=[[0]*n for i in range(n)]

print(sol())
