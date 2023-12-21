n=int(input())
board=[[' ']*n for i in range(n)]
for i in range(n):
    board[0][i]='*'
    board[-1][i]='*'
    board[i][-1]='*'
    board[i][0]='*'
    board[i][i]='*'
    board[i][n-1-i]='*'
for i in range(n):print(*board[i],sep='')
