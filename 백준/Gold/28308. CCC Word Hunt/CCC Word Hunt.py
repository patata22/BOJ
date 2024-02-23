dx=(-1,1,0,0,-1,1,-1,1)
dy=(0,0,-1,1,1,-1,-1,1)

def sol(x,y,depth,canTurn,d):
    global answer
    if depth==W:
        answer+=1
        return
    if depth>1 and canTurn:
        if 0<=d<2: D=(2,3)
        elif 2<=d<4: D=(0,1)
        elif 4<=d<6: D=(6,7)
        elif 6<=d: D=(4,5)
        for nd in D:
            nx,ny=x+dx[nd],y+dy[nd]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]==word[depth]:
                sol(nx,ny,depth+1,False,nd)
                
    nx,ny=x+dx[d],y+dy[d]
    if 0<=nx<n and 0<=ny<m and board[nx][ny]==word[depth]:
        sol(nx,ny,depth+1,canTurn,d)

word = list(input())
W=len(word)
answer=0
n,m=int(input()),int(input())
board=[input().split() for i in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j]==word[0]:
            for k in range(8):
                sol(i,j,1,True,k)

print(answer)