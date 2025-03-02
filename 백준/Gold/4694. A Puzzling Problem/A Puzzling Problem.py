from collections import deque
import sys
input=sys.stdin.readline
dx=(-1,1,0,0)
dy=(0,0,-1,1)

def makeBlock():
    n,m=map(int,input().split())
    tempBoard=[tuple(map(int,input().rstrip())) for i in range(n)]
    visited=[[0]*m for i in range(n)]
    result=[]
    q=deque()   
    for i in range(n):
        for j in range(m):
            if tempBoard[i][j] and not visited[i][j]:
                q.append((i,j))
                result.append((0,0))
                visited[i][j]=1
                while q:
                    x,y=q.popleft()
                    for d in range(4):
                        nx,ny=x+dx[d],y+dy[d]
                        if 0<=nx<n and 0<=ny<m and tempBoard[nx][ny] and not visited[nx][ny]:
                            q.append((nx,ny))
                            result.append((nx-i,ny-j))
                            visited[nx][ny]=1
        if result: return result

def check(x,y,b):
    for dx,dy in b:
        nx,ny=x+dx,y+dy
        if not (0<=nx<4 and 0<=ny<4) or board[nx][ny]: return False
    return True

def sol(depth):
    global flag
    if flag: return
    if depth==tt+1:
        flag=True
        return
    for i in range(tt):
        if not used[i]:
            b=block[i]
            for x in range(4):
                for y in range(4):
                    if not board[x][y] and check(x,y,b):
                        used[i]=1
                        for dx,dy in b:
                            board[x+dx][y+dy]=i+1
                        sol(depth+1)
                        if flag: return
                        for dx,dy in b:
                            board[x+dx][y+dy]=0
                        used[i]=0
cnt=0
while True:
    tt=int(input())
    if not tt: break
    if cnt:print()
    cnt+=1
    block=[makeBlock() for i in range(tt)]
    total=sum([len(x) for x in block])
    if total!=16:
        print('No solution possible')
        continue
    board=[[0]*4 for i in range(4)]
    used=[0]*tt
    flag=False
    sol(1)
    if not flag: print('No solution possible')
    else:
        for i in range(4):
            print(''.join(map(str,board[i])))