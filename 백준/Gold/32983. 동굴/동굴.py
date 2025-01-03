from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append((sx,sy))
    visited=[[0]*m for i in range(n)]
    visited[sx][sy]=1
    answer=0
    total=0
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            total+=board[x][y]
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]!=-1 and not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny]=1
        answer=max(answer,total-t*c)
        t+=1
    return answer
        


n,m,c=map(int,input().split())
sx,sy=map(lambda x: int(x)-1, input().split())
board=[list(map(int,input().split())) for i in range(n)]

print(sol())
