dx=(-1,1,0,0)
dy=(0,0,-1,1)

def move(d):
    if d%2==0:
        s,e,g=0,8,1
    else:
        s,e,g=7,-1,-1
    for i in range(s,e,g):
        for j in range(s,e,g):
            if board[i][j]==0: continue
            x,y=i,j
            while 0<=x+dx[d]<8 and 0<=y+dy[d]<8 and board[x+dx[d]][y+dy[d]]==0:
                board[x+dx[d]][y+dy[d]]=board[x][y]
                board[x][y]=0
                x+=dx[d]
                y+=dy[d]
            if 0<=x+dx[d]<8 and 0<=y+dy[d]<8 and board[x][y]==board[x+dx[d]][y+dy[d]] and not used[x+dx[d]][y+dy[d]]:
                used[x+dx[d]][y+dy[d]]=1
                board[x+dx[d]][y+dy[d]]*=2
                board[x][y]=0

        

board=[list(map(int,input().split())) for i in range(8)]
used=[[0]*8 for i in range(8)]

cmd=input()
if cmd=='U': move(0)
elif cmd=='D': move(1)
elif cmd=='L': move(2)
else: move(3)

for i in range(8):
    print(*board[i])
