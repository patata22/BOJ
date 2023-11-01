from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if x==ex and y==ey: return t-1
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<10 and 0<=ny<10 and board[nx][ny]=='.' and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1
        

board=[]
for i in range(10):
    temp=list(input())
    for j in range(10):
        if temp[j]=='B':
            sx,sy=i,j
            temp[j]='.'
        elif temp[j]=='L':
            ex,ey=i,j
            temp[j]='.'
    board.append(temp)
visited=[[0]*10 for i in range(10)]
print(sol())
