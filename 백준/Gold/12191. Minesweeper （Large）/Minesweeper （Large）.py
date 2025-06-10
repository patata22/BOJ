from collections import deque

dx=(-1,-1,-1,0,0,1,1,1)
dy=(-1,0,1,-1,1,-1,0,1)

def init():
    count=[[0]*n for i in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y]=='.':
                cnt=0
                for d in range(8):
                    nx,ny=x+dx[d],y+dy[d]
                    if 0<=nx<n and 0<=ny<n and board[nx][ny]=='*':
                        cnt+=1
                count[x][y]=cnt
    return count

def travel(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    while q:
        x,y=q.popleft()
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and board[nx][ny]=='.' and not visited[nx][ny]:
                visited[nx][ny]=1
                if count[nx][ny]==0: q.append((nx,ny))            

for tt in range(int(input())):
    n=int(input())
    board=[list(input()) for i in range(n)]
    count=init()
    answer=0
    visited=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]=='.' and not count[i][j] and not visited[i][j]:
                answer+=1
                travel(i,j)
    for i in range(n):
        for j in range(n):
            if board[i][j]=='.' and not visited[i][j]: answer+=1
            
  
    print(f'Case #{tt+1}: {answer}')
    
