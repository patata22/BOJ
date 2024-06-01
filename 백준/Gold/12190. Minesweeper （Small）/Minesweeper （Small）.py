from collections import deque

dx=(-1,-1,-1,0,0,1,1,1)
dy=(-1,0,1,-1,1,-1,0,1)

def travel(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    while q:
        x,y=q.popleft()
        if count[x][y]: continue
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny]=1
                q.append((nx,ny))

for tt in range(int(input())):
    n=int(input())
    board=[list(input()) for i in range(n)]
    count=[[0]*n for i in range(n)]
    visited=[[0]*n for i in range(n)]

    for x in range(n):
        for y in range(n):
            if board[x][y]=='*':
                visited[x][y]=1
                for i in range(8):
                    nx,ny=x+dx[i],y+dy[i]
                    if 0<=nx<n and 0<=ny<n and board[nx][ny]=='.':
                        count[nx][ny]+=1
    answer=0
    for x in range(n):
        for y in range(n):
            if board[x][y]=='.' and not count[x][y] and not visited[x][y]:
                travel(x,y)
                answer+=1
    for x in range(n):
        for y in range(n):
            if board[x][y]=='.' and not visited[x][y]:
                visited[x][y]=1
                answer+=1
    print(f'Case #{tt+1}: {answer}')
