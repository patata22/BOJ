from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def travel(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    color=board[x][y]
    record=[]
    record.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<12 and 0<=ny<6 and board[nx][ny]==color and not visited[nx][ny]:
                visited[nx][ny]=1
                q.append((nx,ny))
                record.append((nx,ny))
    if len(record)>=4:
        for x,y in record:
            board[x][y]='.'
        return 1
    return 0

def drop():
    for i in range(10,-1,-1):
        for j in range(6):
            if board[i][j]!='.':
                x=i
                while x+1<12 and board[x+1][j]=='.':
                    board[x+1][j]=board[x][j]
                    board[x][j]='.'
                    x+=1
                    
board=[list(input()) for i in range(12)]
answer=0
while True:
    cnt=0
    visited=[[0]*6 for i in range(12)]
    for i in range(12):
        for j in range(6):
            if board[i][j]!='.' and not visited[i][j]:
                cnt+=travel(i,j)
    if not cnt:break
    drop()
    answer+=1
print(answer)