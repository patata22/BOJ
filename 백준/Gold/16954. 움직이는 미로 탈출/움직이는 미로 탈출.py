from collections import deque

dx=(-1,-1,-1,0,0,1,1,1)
dy=(-1,0,1,-1,1,-1,0,1)

def move():
    board.pop()
    board.insert(0,['.']*8)

def sol():
    q=deque()
    q.append((7,0))
    visited[7][0]=1
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if board[x][y]=='#':continue
            if x==0 and y==7: return 1
            for i in range(8):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<8 and 0<=ny<8 and board[nx][ny]=='.':
                    visited[nx][ny]=1
                    q.append((nx,ny))
            q.append((x,y))
        move()
    return 0
                

board=[list(input()) for i in range(8)]
visited=[[0]*8 for i in range(8)]
print(sol())
