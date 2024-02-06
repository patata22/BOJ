from collections import deque
DIV=2**31-1
def sol():
    q=deque()
    q.append((0,0))
    visited[0][0]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and board[nx][ny]!='#' and not visited[nx][ny]:
                visited[nx][ny]=1
                q.append((nx,ny))
                

dx=(-1,0,1,0)
dy=(0,-1,0,1)
n=int(input())
board=[list(input()) for i in range(n)]
dp=[[0]*n for i in range(n)]
dp[0][0]=1
for x in range(n):
    for y in range(n):
        if board[x][y]=='#': continue
        for d in range(2):
            nx,ny=x+dx[d],y+dy[d]
            if 0<=nx<n and 0<=ny<n:
                dp[x][y]+=dp[nx][ny]

if dp[-1][-1]:print(dp[-1][-1]%DIV)
else:
    visited=[[0]*n for i in range(n)]
    sol()
    if visited[-1][-1]:
        print("THE GAME IS A LIE")
    else:
        print("INCONCEIVABLE")
