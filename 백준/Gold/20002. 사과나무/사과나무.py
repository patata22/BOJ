n=int(input())
board=[[0]*(n+1)]
for i in range(n):
    board.append([0]+list(map(int,input().split())))
for i in range(1,n+1):
    for j in range(1,n+1):
        board[i][j]+=board[i-1][j]+board[i][j-1]-board[i-1][j-1]
answer=-float('inf')
for k in range(1,n+1):
    for i in range(1,n+1):
        if i+k>n+1: break
        for j in range(1,n+1):
            if j+k>n+1:break
            answer=max(answer,board[i+k-1][j+k-1]-board[i-1][j+k-1]-board[i+k-1][j-1]+board[i-1][j-1])
print(answer)            