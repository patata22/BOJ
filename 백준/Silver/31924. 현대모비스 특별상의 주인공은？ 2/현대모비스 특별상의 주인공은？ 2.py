X='MOBIS'
dx=(-1,-1,-1,0,0,1,1,1)
dy=(-1,0,1,-1,1,-1,0,1)

def sol(x,y,depth,d):
    if depth==4:
        global answer
        answer+=1
        return
    nx,ny=x+dx[d],y+dy[d]
    if 0<=nx<n and 0<=ny<n and board[nx][ny]==X[depth+1]:sol(nx,ny,depth+1,d)

n=int(input())
board=[list(input()) for i in range(n)]
answer=0

for i in range(n):
    for j in range(n):
        if board[i][j]=='M':
            for k in range(8):
                sol(i,j,0,k)
print(answer)