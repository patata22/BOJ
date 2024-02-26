from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    area=1
    peri=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny]=='.':peri+=1
                elif board[nx][ny]=='#' and not visited[nx][ny]:
                    q.append((nx,ny))
                    area+=1
                    visited[nx][ny]=1
            else:peri+=1
    return area,peri
                    
n=int(input())
board=[list(input()) for i in range(n)]
visited=[[0]*n for i in range(n)]
answer=0
perimeter=float('inf')
for x in range(n):
    for y in range(n):
        if board[x][y]=='#' and not visited[x][y]:
            area,peri=sol(x,y)
            if area>answer:
                answer=area
                perimeter=peri
            elif area==answer:
                perimeter=min(perimeter,peri)
print(answer,perimeter)