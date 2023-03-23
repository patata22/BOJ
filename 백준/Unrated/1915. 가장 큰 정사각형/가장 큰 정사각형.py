n,m=map(int,input().split())
board=[list(map(int, list(input()))) for i in range(n)]
for i in range(1,n):
    for j in range(1,m):
        if board[i][j]:
            board[i][j]+=min(board[i-1][j],board[i-1][j-1],board[i][j-1])
print(max([max(board[i]) for i in range(n)])**2)