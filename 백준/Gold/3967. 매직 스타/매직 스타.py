def check():
    a=board[1][1]+board[1][3]+board[1][5]+board[1][7]
    b=board[1][1]+board[2][2]+board[3][3]+board[4][4]
    c=board[1][7]+board[2][6]+board[3][5]+board[4][4]
    d=board[0][4]+board[1][3]+board[2][2]+board[3][1]
    e=board[0][4]+board[1][5]+board[2][6]+board[3][7]
    f=board[3][1]+board[3][3]+board[3][5]+board[3][7]
    return a==b==c==d==e==f

def sol(depth,now):
    global finished
    if finished: return
    if depth==b:
        finished=check()
        return
    x,y=blank[now]
    for i in range(12):
        if not used[i]:
            used[i]=1
            board[x][y]=i
            sol(depth+1,now+1)
            if finished: return
            board[x][y]='x'
            used[i]=0

board=[list(input()) for i in range(5)]
used=[0]*12
blank=[]
for i in range(5):
    for j in range(9):
        if board[i][j]=='x': blank.append((i,j))
        elif board[i][j].isupper():
            board[i][j]=ord(board[i][j])-65
            used[board[i][j]]=1
finished=False
b=len(blank)
sol(0,0)

for i in range(5):
    for j in range(9):
        if board[i][j]=='.':continue
        board[i][j]=chr(board[i][j]+65)

for i in range(5):
    print(*board[i],sep='')
