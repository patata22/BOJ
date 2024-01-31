def sol(depth):
    if depth==n*m:
        global answer
        answer+=1
        return
    sol(depth+1)
    x=depth//m
    y=depth%m
    if x==0 or y==0:
        board[x][y]=1
        sol(depth+1)
        board[x][y]=0
    else:
        if board[x-1][y-1]+board[x-1][y]+board[x][y-1]!=3:
            board[x][y]=1
            sol(depth+1)
            board[x][y]=0

n,m=map(int,input().split())
board=[[0]*m for i in range(n)]
answer=0

sol(0)
print(answer)
