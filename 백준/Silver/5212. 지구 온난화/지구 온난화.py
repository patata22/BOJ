dx=(-1,1,0,0)
dy=(0,0,-1,1)

n,m=map(int,input().split())
change=[]
board=[list(input()) for i in range(n)]
for x in range(n):
    for y in range(m):
        cnt=0
        for d in range(4):
            nx,ny=x+dx[d],y+dy[d]
            if not (0<=nx<n and 0<=ny<m and board[nx][ny]=='X'):
                cnt+=1
        if cnt>=3: change.append((x,y))

for x,y in change:board[x][y]='.'

lx=float('inf')
rx=-float('inf')
ly=float('inf')
ry=-float('inf')
for i in range(n):
    for j in range(m):
        if board[i][j]=='X':
            lx=min(lx,i)
            rx=max(rx,i)
            ly=min(ly,j)
            ry=max(ry,j)
answer=[]
for i in range(lx,rx+1):
    answer.append(board[i][ly:ry+1])

for i in range(len(answer)):
    print(''.join(answer[i]))
