n,m=map(int,input().split())
board=[list(input()) for i in range(n)]

mid=m//2
for i in range(n):
    for j in range(m):
        if board[i][j]!='.':
            board[i][m-1-j]=board[i][j]
    

for i in range(n):
    print(''.join(board[i]))
        
            
