n=int(input())
board=[list(map(int,input().split())) for i in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if board[i][k] and board[k][j]: board[i][j]=1

for i in range(n):
    print(*board[i])
