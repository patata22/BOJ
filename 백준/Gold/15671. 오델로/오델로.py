dx=(-1,-1,-1,0,0,1,1,1)
dy=(-1,0,1,-1,1,-1,0,1)


def play(x,y):
    for d in range(8):
        check(x,y,d)

def check(x,y,d):
    flag=False
    color=board[x][y]
    nx,ny=x,y
    while 0<=nx+dx[d]<6 and 0<=ny+dy[d]<6:
        nx+=dx[d]
        ny+=dy[d]
        if board[nx][ny]=='.': break
        if board[nx][ny]==board[x][y]:
            flag=True
            break
    if flag:
        while not (nx==x and ny==y):
            
            board[nx][ny]=board[x][y]
            nx-=dx[d]
            ny-=dy[d]

n=int(input())

board=[['.']*6 for i in range(6)]
board[2][2]='W'
board[3][3]='W'
board[2][3]='B'
board[3][2]='B'

isBlackTurn=0
for _ in range(n):
    isBlackTurn = 1-isBlackTurn
    a,b=map(lambda x: int(x)-1,input().split())
    board[a][b]='WB'[isBlackTurn]
    play(a,b)
for i in range(6):
    print(''.join(board[i]))
B=0
W=0
for i in range(6):
    for j in range(6):
        if board[i][j]=='B':B+=1
        elif board[i][j]=='W': W+=1

print('Black') if B>W else print('White')
   