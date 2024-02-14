from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def pirate():
    q=deque()
    q.append((px,py))
    visited=[[-1]*m for i in range(n)]
    visited[px][py]=0
    t=1
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]=='.' and visited[nx][ny]==-1:
                    visited[nx][ny]=t
                    q.append((nx,ny))
        t+=1
    time=[[float('inf')]*m for i in range(n)]
    for i in range(n):
        short=float('inf')
        left=float('inf')
        right=-1
        for j in range(m):
            if board[i][j]=='.':
                short=min(short,visited[i][j])
                left=min(left,j)
                right=max(right,j)
            elif board[i][j]=='I':
                if left!=float('inf'):
                    for k in range(left,j):
                        time[i][k]=short
                left=float('inf')
                right=-1
                short=float('inf')
        if left!=float('inf'):
            for k in range(left,right+1):
                time[i][k]=short
    for j in range(m):
        short=float('inf')
        up=float('inf')
        down=-1
        for i in range(n):
            if board[i][j]=='.':
                short=min(short,visited[i][j])
                up=min(up,i)
                down=max(down,i)
            elif board[i][j]=='I':
                if up!=float('inf'):
                    for k in range(up,i):
                        time[k][j]=min(time[k][j],short)
                up=float('inf')
                down=-1
                short=float('inf')
        if up!=float('inf'):
            for k in range(up,down+1):
                time[k][j]=min(time[k][j],short)
    return time

def sol():
    q=deque()
    q.append((sx,sy))
    visited=[[-1]*m for i in range(n)]
    visited[sx][sy]=0
    t=1
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if x==ex and y==ey: return 'YES'
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]=='.' and visited[nx][ny]==-1 and time[nx][ny]>t:
                    q.append((nx,ny))
                    visited[nx][ny]=t
        t+=1
    return 'NO'
            
    

n,m=map(int,input().split())
board=[]
for i in range(n):
    temp=list(input())
    for j in range(m):
        if temp[j]=='Y':
            sx,sy=i,j
            temp[j]='.'
        elif temp[j]=='V':
            px,py=i,j
            temp[j]='.'
        elif temp[j]=='T':
            ex,ey=i,j
            temp[j]='.'
    board.append(temp)
                    
time=pirate()
print(sol())
