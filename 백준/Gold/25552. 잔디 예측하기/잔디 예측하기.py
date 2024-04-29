from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    cnt=0
    for i in range(n):
        for j in range(m):
            if board[i][j]=='O':
                q.append((i,j))
                visited[i][j][0]=1
    while q:
        Q=deque()
        Q.append(q.popleft())
        t=1
        while Q and t<=d:
            for _ in range(len(Q)):
                x,y=Q.popleft()
                for i in range(4):
                    nx,ny=x+dx[i],y+dy[i]
                    if 0<=nx<n and 0<=ny<m and not visited[nx][ny][t]:
                        visited[nx][ny][t]=1
                        Q.append((nx,ny))
                        if board[nx][ny]=='X' and target[nx][ny]=='O':
                            board[nx][ny]='O'
                            cnt+=1
                            q.append((nx,ny))
            t+=1
    if cnt==count:print('YES')
    else: print('NO')

n,m=map(int,input().split())
board=[list(input()) for i in range(n)]
d=int(input())
target=[list(input()) for i in range(n)]
visited=[[[0]*(d+1) for i in range(m)] for i in range(n)]
strange=False
count=0
for i in range(n):
    for j in range(m):
        if board[i][j]=='O' and target[i][j]=='X':
            strange=True
            break
        elif board[i][j]=='X' and target[i][j]=='O':
            count+=1

if strange:(print('NO'))
else:sol()
    
