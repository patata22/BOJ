from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    result=0
    for i in range(n):
        for j in range(m):
            if board[i][j] and not visited[i][j]:
                visited[i][j]=1
                result+=1
                travel(i,j)
    return result

def travel(i,j):
    q=deque()
    q.append((i,j))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny] and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny]=1
                

for tt in range(int(input())):
    print(f'Case #{tt+1}:')
    n,m=map(int,input().split())
    board=[list(map(int,input())) for i in range(n)]
    for _ in range(int(input())):
        cmd=input().split()
        if cmd[0]=='Q':
            visited=[[0]*m for i in range(n)]
            print(sol())
        else:
            r,c,d=map(int,cmd[1:])
            board[r][c]=d
    
