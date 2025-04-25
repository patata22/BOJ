from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def drop(board):
    for i in range(n-1,0,-1):
        for j in range(m):
            if board[i][j]==0:
                for k in range(1,i+1):
                    if board[i-k][j]:
                        board[i][j]=board[i-k][j]
                        board[i-k][j]=0
                        break
    return board
                    
def sol(depth,board,score):
    global answer
    if depth==3:
        
        return
    used=[[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] and  not used[i][j]:
                nxt=[board[k][:] for k in range(n)]
                q=deque()
                q.append((i,j))
                block=nxt[i][j]
                used[i][j]=1
                result=1
                while q:
                    x,y=q.popleft()
                    nxt[x][y]=0
                    for d in range(4):
                        nx,ny=x+dx[d],y+dy[d]
                        if 0<=nx<n and 0<=ny<m and nxt[nx][ny]==block and not used[nx][ny]:
                            used[nx][ny]=1
                            q.append((nx,ny))
                            result+=1
                answer=max(answer,score+(result**2))
                nxt=drop(nxt)
                sol(depth+1,nxt,score+(result**2))

m,n=map(int,input().split())
board=[list(map(int,input().split())) for i in range(n)]
answer=0

sol(0,board,0)
print(answer)