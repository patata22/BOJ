from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append((r,c,0))
    t=0
    while q:
        for _ in range(len(q)):
            x,y,visit = q.popleft()
            if visit == 63: return t
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0<=nx<5 and 0<=ny<5 and board[nx][ny]!=-1 and not visited[nx][ny][visit]:        
                    if not board[nx][ny]:
                        visited[nx][ny][visit] = 1
                        q.append((nx,ny,visit))
                    else:
                        temp = visit|(1<<(board[nx][ny]-1))
                        visited[nx][ny][temp] = 1
                        q.append((nx,ny,temp))
            
        t+=1
    return -1

board= [tuple(map(int,input().split())) for i in range(5)]
visited = [[[0]*64 for i in range(5)] for i in range(5)]
r,c=map(int,input().split())

print(sol())