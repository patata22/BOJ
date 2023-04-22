def check(x,y):
    global answer,flag,X,Y
    if checkRow(x,y) or checkCol(x,y) or checkDigR(x,y):
        X,Y=x,y
        answer=board[x][y]
        flag=True
        return
    if checkDigL(x,y):
        X,Y=x+4,y-4
        answer=board[x][y]
        flag=True
        return

def checkRow(x,y):
    nx=x
    cnt=1
    while nx<18 and board[nx+1][y]==board[x][y]:
        nx+=1
        cnt+=1
    if x>0 and board[x-1][y]==board[x][y]:cnt+=1
    
    if cnt==5:
        if x>0 and board[x-1][y]==board[x][y]:return False
        return True
    return False

def checkCol(x,y):
    cnt=1
    ny=y
    while ny<18 and board[x][ny+1]==board[x][y]:
        ny+=1
        cnt+=1
    
    if cnt==5:
        if y>0 and board[x][y-1]==board[x][y]:return False
        return True
    return False

def checkDigR(x,y):
    cnt=1
    nx,ny=x,y
    while nx<18 and ny<18 and board[nx+1][ny+1]==board[x][y]:
        nx+=1
        ny+=1
        cnt+=1
    
    if cnt==5:
        if x>0 and y>0 and board[x-1][y-1]==board[x][y]:return False
        return True
    return False
        
def checkDigL(x,y):
    cnt=1
    nx,ny=x,y
    while nx<18 and ny>0 and board[nx+1][ny-1]==board[x][y]:
        nx+=1
        ny-=1
        cnt+=1
    
    if cnt==5:
        if x>0 and y<18 and board[x-1][y+1]==board[x][y]:return False
        return True
    return False

board=[tuple(map(int,input().split())) for i in range(19)]
flag=False
X,Y=0,0
for x in range(19):
    if flag:break
    for y in range(19):
        if board[x][y]:
            check(x,y)
            if flag:break

if not flag:print(0)
else:
    print(board[X][Y])
    print(X+1,Y+1)
