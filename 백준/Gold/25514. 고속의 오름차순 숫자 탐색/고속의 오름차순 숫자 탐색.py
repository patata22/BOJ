from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append((r,c,0))
    visited[r][c][0]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y,now = q.popleft()
            if now==6: return t
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<nx<=5 and 0<ny<=5 and not visited[nx][ny][now] and board[nx][ny]!=-1:
                    visited[nx][ny][now]=1
                    if board[nx][ny]==now+1:
                        q.append((nx,ny,now+1))
                    else: q.append((nx,ny,now))
            for i in range(4):
                nx,ny=x,y
                while 0<=nx+dx[i]<7 and 0<=ny+dy[i]<7 and board[nx+dx[i]][ny+dy[i]]!=-1:
                    nx+=dx[i]
                    ny+=dy[i]
                    if board[nx][ny]==7:
                        if not visited[nx][ny][now]:
                            q.append((nx,ny,now))
                        visited[nx][ny][now]=1
                        break
                if not visited[nx][ny][now]:
                    visited[nx][ny][now]=1
                    if board[nx][ny]==now+1:
                        q.append((nx,ny,now+1))
                    else: q.append((nx,ny,now))
            
        t+=1
    return -1
        
board=[[-1]*7]
for _ in range(5):
    board.append([-1]+list(map(int,input().split()))+[-1])
board.append([-1]*7)
r,c=map(int,input().split())
r+=1
c+=1

visited=[[[0]*7 for i in range(7)] for i in range(7)]
visited_fast = [[[0]*7 for i in range(7)] for i in range(7)]

print(sol())
