
dx=(-1,-1,-1,0,0,1,1,1)
dy=(-1,0,1,-1,1,-1,0,1)
d={1:('N','S'), 2:('F','T'), 3:('P','J')}

def sol(x,y,cnt,z):
    global answer
    if cnt==4:
        answer+=1
        return
    nx,ny=x+dx[z],y+dy[z]
    if 0<=nx<n and 0<=ny<m and board[nx][ny] in d[cnt]:
        sol(nx,ny,cnt+1,z)



n,m=map(int,input().split())
board=[list(input()) for i in range(n)]
answer=0
for i in range(n):
    for j in range(m):
        if board[i][j] in ('E','I'):
            for k in range(8):
                sol(i,j,1,k)

print(answer)
