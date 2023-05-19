def checkH(x,y):
    now=board[x][y]
    cnt=1
    ny=y
    while 0<ny<19 and board[x][ny+1]==now:
        cnt+=1
        ny+=1
    ny=y
    while 1<ny<20 and board[x][ny-1]==now:
        cnt+=1
        ny-=1
    if cnt==5:return True
    return False

def checkV(x,y):
    now=board[x][y]
    cnt=1
    nx=x
    while 0<nx<19 and board[nx+1][y]==now:
        cnt+=1
        nx+=1
    nx=x
    while 1<nx<20 and board[nx-1][y]==now:
        cnt+=1
        nx-=1
    if cnt==5:return True
    return False

def checkDR(x,y):
    now=board[x][y]
    cnt=1
    nx,ny=x,y
    while 0<nx<19 and 0<ny<19 and board[nx+1][ny+1]==now:
        cnt+=1
        nx+=1
        ny+=1
    nx,ny=x,y
    while 1<nx<20 and 1<ny<20 and board[nx-1][ny-1]==now:
        cnt+=1
        nx-=1
        ny-=1
    if cnt==5:return True
    return False

def checkLR(x,y):
    now=board[x][y]
    cnt=1
    nx,ny=x,y
    while 1<nx<20 and 0<ny<19 and board[nx-1][ny+1]==now:
        cnt+=1
        nx-=1
        ny+=1
    nx,ny=x,y
    while 0<nx<19 and 1<ny<20 and board[nx+1][ny-1]==now:
        cnt+=1
        nx+=1
        ny-=1
    if cnt==5: return True
    return False
        
def check(x,y):
    return checkH(x,y)|checkV(x,y)|checkDR(x,y)|checkLR(x,y)
def sol():
    for _ in range(n):
        a,b=map(int,input().split())
        if _%2==0:
            board[a][b]=1
        else:
            board[a][b]=2
        if check(a,b): return _+1
    return -1

n=int(input())
board=[[0]*20 for i in range(20)]
print(sol())
