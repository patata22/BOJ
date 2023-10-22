def check():
    visit=[0]*(n*n+1)
    for i in range(n):
        for j in range(n):
            if not 0<board[i][j]<=n**2: return False
            visit[board[i][j]]+=1
            if visit[board[i][j]]>1:return False
    return True

def row(x):
    total=0
    for i in range(n):
        total+=board[x][i]
    return total==T

def col(x):
    total=0
    for i in range(n):
        total+=board[i][x]
    return total==T

def diaR():
    total=0
    for i in range(n):
        total+=board[i][i]
    return total==T

def diaL():
    total=0
    for i in range(n):
        total+=board[n-i-1][i]
    return total==T

def sol():
    if not check():
        return 'FALSE'
    for i in range(n):
        if not row(i): return 'FALSE'
        if not col(i): return 'FALSE'
    if not diaR(): return 'FALSE'
    if not diaL(): return 'FALSE'
    return 'TRUE'
n=int(input())
board=[list(map(int,input().split())) for i in range(n)]
T=(n*(n**2+1))//2
print(sol())
       
