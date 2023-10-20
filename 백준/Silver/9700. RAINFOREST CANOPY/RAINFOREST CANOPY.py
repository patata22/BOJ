from collections import deque

dx=(-1,-1,-1,0,0,1,1,1)
dy=(-1,0,1,-1,1,-1,0,1)

def sol(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    while q:
        x,y=q.popleft()
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny]=1
                q.append((nx,ny))
    
t=0
while True:
    try:
        t+=1
        n=int(input())
        board=[list(map(int,input())) for i in range(n)]
        visited=[[0]*n for i in range(n)]
        answer=0
        for i in range(n):
            for j in range(n):
                if board[i][j] and not visited[i][j]:
                    answer+=1
                    sol(i,j)
        print(f'Case #{t}: {answer}')
                    
    except:
        break
