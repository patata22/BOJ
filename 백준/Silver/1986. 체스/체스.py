dqx=(-1,-1,-1,0,0,1,1,1)
dqy=(-1,0,1,-1,1,-1,0,1)
dkx=(-1,-2,-2,-1,1,2,2,1)
dky=(-2,-1,1,2,-2,-1,1,2)

def moveQueen(x,y):
    for i in range(8):
        nx,ny=x+dqx[i],y+dqy[i]
        while 0<=nx<n and 0<=ny<m and board[nx][ny]!=-1:
            board[nx][ny]=1
            nx+=dqx[i]
            ny+=dqy[i]

def moveKnight(x,y):
    for i in range(8):
        nx,ny=x+dkx[i],y+dky[i]
        if 0<=nx<n and 0<=ny<m and board[nx][ny]==0:
            board[nx][ny]=1

n,m=map(int,input().split())
board=[[0]*m for i in range(n)]

queen=[]
temp=tuple(map(lambda x: int(x)-1,input().split()))
for i in range(1,len(temp), 2):
    x,y=temp[i],temp[i+1]
    queen.append((x,y))
    board[x][y]=-1
    
knight=[]
temp=tuple(map(lambda x: int(x)-1,input().split()))
for i in range(1,len(temp), 2):
    x,y=temp[i],temp[i+1]
    knight.append((x,y))
    board[x][y]=-1
    
temp=tuple(map(lambda x: int(x)-1,input().split()))
for i in range(1,len(temp), 2):
    x,y=temp[i],temp[i+1]
    board[x][y]=-1

for x,y in queen:
    moveQueen(x,y)
for x,y in knight:
    moveKnight(x,y)

answer=0
for i in range(n):
    for j in range(m):
        if not board[i][j]: answer+=1
print(answer)
