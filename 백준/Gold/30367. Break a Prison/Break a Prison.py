from collections import deque

dx=(-1,0,1,0)
dy=(0,1,0,-1)


def sol():
    q=deque()
    visited=[[[0]*4 for i in range(m)] for i in range(n)]
    for i in range(4):
        q.append((sx,sy,i))
        visited[sx][sy][i]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y,prev=q.popleft()
            if x==ex and y==ey: return t
            forbidden=(prev+1)%4
            for d in range(4):
                if d==forbidden: continue
                nx,ny=x+dx[d],y+dy[d]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]=='.' and not visited[nx][ny][d]:
                    visited[nx][ny][d]=1
                    q.append((nx,ny,d))
        t+=1
    return -1

n,m=map(int,input().split())
board=[]
for i in range(n):
    temp=list(input())
    for j in range(m):
        if temp[j]=='S':
            sx,sy=i,j
            temp[j]='.'
        elif temp[j]=='E':
            ex,ey=i,j
            temp[j]='.'
    board.append(temp)

print(sol())
