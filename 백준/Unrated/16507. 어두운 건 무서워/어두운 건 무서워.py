n,m,q=map(int,input().split())
board=[[0]*(m+1)]
for _ in range(n):
    board.append([0]+list(map(int,input().split())))

for i in range(1,n+1):
    board[i][1]+=board[i-1][1]

for i in range(1,m+1):
    board[1][i]+=board[1][i-1]


for i in range(2,n+1):
    for j in range(2,m+1):
        board[i][j]+=board[i-1][j]+board[i][j-1]-board[i-1][j-1]


for _ in range(q):
    r1,c1,r2,c2=map(int,input().split())
    temp=(r2-r1+1)*(c2-c1+1)
    print((board[r2][c2]-board[r1-1][c2]-board[r2][c1-1]+board[r1-1][c1-1])//temp)
