dx=(-1,1,0,0)
dy=(0,0,-1,1)

def dfs(x,y,count,apple):
    global answer
    if answer: return
    if count==3:
        if apple>=2:
            answer=1
        return
    for i in range(4):
        nx,ny= x+dx[i], y+dy[i]
        if 0<=nx<5 and 0<=ny<5 and board[nx][ny]!=-1:
            origin = board[nx][ny]
            board[nx][ny]=-1
            dfs(nx,ny,count+1, apple+origin)
            board[nx][ny]=origin
    

board = [list(map(int,input().split())) for i in range(5)]

answer=0

x,y=map(int,input().split())
board[x][y]=-1
dfs(x,y,0,0)
print(answer)
