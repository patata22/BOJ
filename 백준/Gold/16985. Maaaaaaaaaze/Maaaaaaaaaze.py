from collections import deque

dx=(-1,1,0,0,0,0)
dy=(0,0,-1,1,0,0)
dz=(0,0,0,0,-1,1)


def rotate(x):
    return list(zip(*x[::-1]))

def makeMaze(depth):
    global answer
    if answer==12: return
    if depth==5:
        if playBoard[0][0][0] and playBoard[4][4][4]:
            answer=min(answer,bfs())
        return
    for x in board[depth]:
        for j in range(5):
            if not used[j]:
                used[j]=1
                playBoard[j]=x
                makeMaze(depth+1)
                playBoard[j]=0
                used[j]=0

def bfs():
    q=deque()
    visited=[[[0]*5 for i in range(5)] for i in range(5)]
    q.append((0,0,0))
    visited[0][0][0]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y,z=q.popleft()
            if x==4 and y==4 and z==4: return t
            for i in range(6):
                nx,ny,nz=x+dx[i],y+dy[i],z+dz[i]
                if 0<=nx<5 and 0<=ny<5 and 0<=nz<5 and playBoard[nx][ny][nz] and not visited[nx][ny][nz]:
                    visited[nx][ny][nz]=1
                    q.append((nx,ny,nz))
        t+=1

    return float('inf')

board=[[] for i in range(5)]
for _ in range(5):
    temp=[list(map(int,input().split())) for i in range(5)]
    board[_].append(temp)
    for __ in range(3):
        temp=rotate(temp)
        board[_].append(temp)
playBoard=[0]*5
used=[0]*5
answer=float('inf')
makeMaze(0)
if answer==float('inf'):print(-1)
else: print(answer)
