spread_left = [[0,0,2,0,0], [0,10,7,1,0], [5, 0, 0, 0, 0], [0,10,7,1,0], [0,0,2,0,0]]
spread_right= []
for i in range(5):
    spread_right.append(spread_left[i][::-1])
spread_up = [[0,0,5,0,0], [0,10,0,10,0], [2,7,0,7,2], [0,1,0,1,0], [0,0,0,0,0]]
spread_down = []
for i in range(4,-1,-1):
    spread_down.append(spread_up[i])
up={}
down={}
left={}
right={}
for i in range(5):
    for j in range(5):
        if spread_up[i][j]:
            up[(i-2,j-2)]=spread_up[i][j]
        if spread_down[i][j]:
            down[(i-2,j-2)] = spread_down[i][j]
        if spread_left[i][j]:
            left[(i-2,j-2)]= spread_left[i][j]
        if spread_right[i][j]:
            right[(i-2,j-2)]= spread_right[i][j]

dx=(-1,0,1,0)
dy=(0,-1,0,1)
dust = (up, left, down, right)

def sol(x,y,d):
    global answer
    origin = board[x][y]
    for ax,ay in dust[d]:
        nx, ny = x+ax, y+ay
        moving_dust = (origin*dust[d][(ax,ay)])//100
        if 0<=nx<n and 0<=ny<n:
            board[nx][ny]+= moving_dust
        else: answer+=moving_dust
        board[x][y]-=moving_dust
    tx,ty = x+dx[d], y+dy[d]
    if 0<=tx<n and 0<=ty<n:
        board[tx][ty]+=board[x][y]
    else: answer+=board[x][y]
    board[x][y] = 0
    
n=int(input())
board= [list(map(int,input().split())) for i in range(n)]
visited= [[0]*n for i in range(n)]

x=n//2
y=n//2
d=0
visited[x][y]=1

answer=0
while x!=0 or y!=0:
    temp = (d+1)%4
    if not visited[x+dx[temp]][y+dy[temp]]:
        d=temp
    x,y= x+dx[d], y+dy[d]
    visited[x][y]=1
    sol(x,y,d)
    
print(answer)
