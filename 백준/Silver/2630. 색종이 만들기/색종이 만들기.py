def sol(x,y,n):
    global a0,a1
    if n==1:
        if board[x][y]: a1+=1
        else:a0+=1
        return
    temp=0
    for i in range(x,x+n):
        temp+=sum(board[i][y:y+n])
    if temp==n*n:a1+=1
    elif not temp:a0+=1
    else:
        N=n//2
        sol(x,y,N)
        sol(x+N,y,N)
        sol(x,y+N,N)
        sol(x+N,y+N,N)
        
        

n=int(input())
board = [tuple(map(int,input().split())) for i in range(n)]
a0=0
a1=0
sol(0,0,n)
print(a0)
print(a1)

