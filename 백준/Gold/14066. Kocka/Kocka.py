def stackBox(i,j):
    height=box[i][j]
    x=R-1-2*(r-i-1)
    y=4*(j-1)+(2*(r-i+1))
    for i in range(height):
        drawBox(x-3*i,y)

def drawBox(x,y):
    board[x][y]='+'
    board[x][y+1]='-'
    board[x][y+2]='-'
    board[x][y+3]='-'
    board[x][y+4]='+'
    board[x-1][y]='|'
    board[x-1][y+1]=' '
    board[x-1][y+2]=' '
    board[x-1][y+3]=' '
    board[x-1][y+4]='|'
    board[x-1][y+5]='/'
    board[x-2][y]='|'
    board[x-2][y+1]=' '
    board[x-2][y+2]=' '
    board[x-2][y+3]=' '
    board[x-2][y+4]='|'
    board[x-2][y+5]=' '
    board[x-2][y+6]='+'
    board[x-3][y]='+'
    board[x-3][y+1]='-'
    board[x-3][y+2]='-'
    board[x-3][y+3]='-'
    board[x-3][y+4]='+'
    board[x-3][y+5]=' '
    board[x-3][y+6]='|'
    board[x-4][y+1]='/'
    board[x-4][y+2]=' '
    board[x-4][y+3]=' '
    board[x-4][y+4]=' '
    board[x-4][y+5]='/'
    board[x-4][y+6]='|'
    board[x-5][y+2]='+'
    board[x-5][y+3]='-'
    board[x-5][y+4]='-'
    board[x-5][y+5]='-'
    board[x-5][y+6]='+'
    
r,c=map(int,input().split())
box=[list(map(int,input().split())) for i in range(r)]
C=(4*c)+1+(2*r)
R=0
for i in range(r):
    for j in range(c):
        temp=(r-i)*2+3*box[i][j]+1
        R=max(R,temp)
board=[['.']*C for i in range(R)]


for i in range(r):
    for j in range(c):
        stackBox(i,j)

for i in range(R):
    print(''.join(board[i]))
