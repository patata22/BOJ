from collections import deque

dx=(-1,-2,-2,-1,1,2,2,1)
dy=(-2,-1,1,2,-2,-1,1,2)

def toString(x):
    temp=temp=[]
    for i in range(4):
        for j in range(4):
            temp.append(str(x[i][j]))
    return ''.join(temp)
    
def toBoard(x):
    temp=[[0]*4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            temp[i][j]=int(x[4*i+j])
    return temp

def copyBoard(x):
    temp=[[0]*4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            temp[i][j]=x[i][j]
    return temp

def sol():
    q=deque()
    visited=[0]*(1<<16)
    start=toString([list(map(int,input())) for i in range(4)])
    end=int(toString([list(map(int,input())) for i in range(4)]),2)
    q.append(start)
    visited[int(start,2)]=1
    t=0
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            if int(now,2)==end: return t
            board=toBoard(now)
            for x in range(4):
                for y in range(4):
                    if board[x][y]:
                        nxt=copyBoard(board)
                        for d in range(8):
                            nx,ny=x+dx[d],y+dy[d]
                            if 0<=nx<4 and 0<=ny<4 and not nxt[nx][ny]:
                                nxt[nx][ny]=1
                                nxt[x][y]=0
                                temp=toString(nxt)
                                if not visited[int(temp,2)]:
                                    visited[int(temp,2)]=1
                                    q.append(temp)
                                nxt[x][y]=1
                                nxt[nx][ny]=0
        t+=1

print(sol())