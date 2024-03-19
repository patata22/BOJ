n,m=map(int,input().split())

board=[[0]*(m+1)]
for i in range(n):
    board.append([0]+list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,m+1):
        board[i][j]+=board[i-1][j]+board[i][j-1]-board[i-1][j-1]
answer=-float('inf')

for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(1,i+1):
            for l in range(1,j+1):
                temp=board[i][j]-board[i-k][j]-board[i][j-l]+board[i-k][j-l]
                answer=max(answer,temp)
print(answer)
