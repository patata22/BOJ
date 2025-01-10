from collections import deque

dx=(0,0,-1,1,0,0)
dy=(0,0,0,0,-1,1)
# 0 0 D U R L

def sol():
    q=deque()
    visited=[[0]*m for i in range(n)]
    q.append((sx,sy))
    visited[sx][sy]=1
    t=0
    while q and t<=T:
        for _ in range(len(q)):
            x,y=q.popleft()
            if x==0 or x==n-1 or y==0 or y==m-1: return t
            for i in range(2,6):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and (board[nx][ny]==0 or board[nx][ny]==i) and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        t+=1
    return 'NOT POSSIBLE'

T,n,m=map(int,input().split())

board=[]
for i in range(n):
    temp=list(input())
    for j in range(m):
        if temp[j]=='S':
            temp[j]=0
            sx,sy=i,j
        elif temp[j]=='D': temp[j]=2
        elif temp[j]=='U': temp[j]=3
        elif temp[j]=='R': temp[j]=4
        elif temp[j]=='L': temp[j]=5
        else: temp[j]=int(temp[j])
    board.append(temp)

print(sol())
