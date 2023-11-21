for _ in range(int(input())):
    x=input()
    n=len(x)
    board=[[' ']*n for i in range(n)]
    for i in range(n):
        board[0][i]=x[i]
        board[-1][n-i-1]=x[i]
    for i in range(1,n-1):
        board[i][0]=x[i]
        board[n-i-1][-1]=x[i]
    for i in range(n):
        print(''.join(board[i]))
            
