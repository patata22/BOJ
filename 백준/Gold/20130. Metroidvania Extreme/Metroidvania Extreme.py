from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append((sx,sy))
    visited=[[0]*m for i in range(n)]
    visited[sx][sy]=1
    key=set()
    noKey={}
    answer=[]
    while q:
        x,y=q.popleft()
        answer.append((x,y))
        if x==ex and y==ey: break
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]!='#' and not visited[nx][ny]:
                if board[nx][ny].isalpha():
                    if board[nx][ny].islower():
                        visited[nx][ny]=1
                        q.append((nx,ny))
                        key.add(board[nx][ny])
                        K=board[nx][ny].upper()
                        if K in noKey:
                            for mx, my in noKey[K]:
                                if not visited[mx][my]:
                                    visited[mx][my]=1
                                    q.append((mx,my))
                            del noKey[K]
                    else:
                        if board[nx][ny].lower() in key:
                            visited[nx][ny]=1
                            q.append((nx,ny))
                            
                        else:
                            if board[nx][ny] not in noKey:
                                noKey[board[nx][ny]]=[(nx,ny)]
                            else:
                                noKey[board[nx][ny]].append((nx,ny))
                            
                else:
                    visited[nx][ny]=1
                    q.append((nx,ny))
    print(len(answer))
    for x,y in answer:
        print(x+1, y+1)

n,m=map(int,input().split())
board=[]
for i in range(n):
    x=list(input())
    for j in range(m):
        if x[j]=='@':
            x[j]='*'
            sx,sy=i,j
        elif x[j]=='!':
            x[j]='!'
            ex,ey=i,j
    board.append(x)

sol()
