def sol1():
    new=[[0]*m for i in range(n)]
    for j in range(m):
        for i in range(n):
            new[i][j]=board[n-1-i][j]
    return new
        
def sol2():
    return [board[i][::-1] for i in range(n)]

def sol3():
    global n,m,N,M
    new=[[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            new[i][j]= board[n-1-j][i]
    n,m=m,n
    N,M=M,N
    return new

def sol4():
    global n,m,N,M
    new=[[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            new[i][j]=board[j][m-1-i]
    n,m=m,n
    N,M=M,N
    return new

def sol5():
    new=[[0]*m for i in range(n)]
    for i in range(N):
        for j in range(M):
            new[i][j]=board[i+N][j]
    for i in range(N):
        for j in range(M,m):
            new[i][j]=board[i][j-M]
    for i in range(N,n):
        for j in range(M,m):
            new[i][j]=board[i-N][j]
    for i in range(N,n):
        for j in range(M):
            new[i][j]=board[i][j+M]
    return new

def sol6():
    new=[[0]*m for i in range(n)]
    for i in range(N):
        for j in range(M):
            new[i][j]=board[i][j+M]
    for i in range(N):
        for j in range(M,m):
            new[i][j]=board[i+N][j]
    for i in range(N,n):
        for j in range(M,m):
            new[i][j]=board[i][j-M]
    for i in range(N,n):
        for j in range(M):
            new[i][j]=board[i-N][j]
    return new

n,m,r=map(int,input().split())
N=n//2
M=m//2

board=[list(map(int,input().split())) for i in range(n)]
for x in map(int,input().split()):
    if x==1: board=sol1()
    elif x==2: board=sol2()
    elif x==3: board=sol3()
    elif x==4: board=sol4()
    elif x==5: board=sol5()
    elif x==6: board=sol6()

for i in range(len(board)):
    print(*board[i])
    
