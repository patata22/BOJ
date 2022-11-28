from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def rotate(x,y,l):
    temp = [[0]*l for i in range(l)]
    for i in range(l):
        for j in range(l):
            temp[i][j] = board[x+l-1-j][y+i]
    for i in range(l):
        for j in range(l):
            board[i+x][j+y] = temp[i][j]

def melt():
    target=[]
    for x in range(N):
        for y in range(N):
            if board[x][y]:
                temp = 0
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0<=nx<N and 0<=ny<N and board[nx][ny]:temp+=1
                if temp<3: target.append((x,y))
    for x,y in target: board[x][y]-=1

def searchAnswer(x,y):
    global big
    global total
    cnt=1
    q=deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and board[nx][ny]:
                cnt+=1
                total+=board[nx][ny]
                visited[nx][ny] = 1
                q.append((nx,ny))
    big = max(big, cnt)
    
n,q = map(int,input().split())
N=2**n

board = [list(map(int,input().split())) for i in range(N)]
visited= [[0]* (N) for i in range(N)]
L=list(map(int,input().split()))

total= 0
big = 0

for l in L:
    if l!=0:
        gap = 2**l
        for i in range(0,N,gap):
            for j in range(0,N,gap):
                rotate(i,j,gap)
    melt()

for i in range(N):
    for j in range(N):
        if board[i][j] and not visited[i][j]:
            total+=board[i][j]
            visited[i][j]=1
            searchAnswer(i,j)

print(total)
print(big)
