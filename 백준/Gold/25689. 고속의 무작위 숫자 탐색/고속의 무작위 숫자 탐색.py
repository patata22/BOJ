from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append((r,c,0))
    visited[r][c][0]=0
    t=0
    while q:
        for _ in range(len(q)):
            x,y,bit = q.popleft()        
            if bit==63: return t
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<5 and 0<=ny<5 and board[nx][ny]!=-1:
                    if not board[nx][ny] and not visited[nx][ny][bit]:
                        visited[nx][ny][bit]=1
                        q.append((nx,ny,bit))
                    if 1<=board[nx][ny]<=6:
                        nxt=bit|(1<<board[nx][ny]-1)
                        if not visited[nx][ny][nxt]:
                            visited[nx][ny][nxt]=1
                            q.append((nx,ny,nxt))
            for i in range(4):
                nx,ny=x,y
                while 0<=nx+dx[i]<5 and 0<=ny+dy[i]<5 and board[nx+dx[i]][ny+dy[i]]!=-1:
                    nx+=dx[i]
                    ny+=dy[i]
                    if board[nx][ny]==7: break
                if (board[nx][ny]==0 or board[nx][ny]==7) and not visited[nx][ny][bit]:
                    visited[nx][ny][bit]=1
                    q.append((nx,ny,bit))
                if 1<=board[nx][ny]<=6:
                    nxt = bit|(1<<board[nx][ny]-1)
                    if not visited[nx][ny][nxt]:
                        visited[nx][ny][nxt]=1
                        q.append((nx,ny,nxt))
                                    
        t+=1
    return -1

board=[tuple(map(int,input().split())) for i in range(5)]
r,c=map(int,input().split())
visited=[[[0]*64 for i in range(5)] for i in range(5)]
print(sol())