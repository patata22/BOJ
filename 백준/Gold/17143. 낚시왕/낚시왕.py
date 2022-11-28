dx=(-1,0,1,0)
dy=(0,1,0,-1)
direction = {1:0, 2:2, 3:1, 4:3}

def catch(x):
    global answer
    for i in range(R):
        if board[i][x]!=0:
            answer+=board[i][x]
            board[i][x]=0
            return

def move():
    global shark,board
    temp_board = [[0]*C for i in range(R)]
    temp_shark = []
    while shark:
        x,y,s,d,z = shark.pop()
        if board[x][y]!=z: continue
        temp_s = s
        nx=x
        ny=y
        while temp_s:
            nx+=dx[d]
            ny+=dy[d]
            if 0<=nx<R and 0<=ny<C: temp_s-=1
            else:
                d=(d+2)%4
                nx+=dx[d]
                ny+=dy[d]
        if temp_board[nx][ny]<z:
            temp_board[nx][ny] = z
            temp_shark.append((nx,ny,s,d,z))
    board= temp_board
    shark = temp_shark
    return
    
R,C,m= map(int,input().split())
board = [[0]*C for i in range(R)]
shark = []
for _ in range(m):
    r,c,s,d,z= map(int,input().split())
    if d in (1,2):
        shark.append((r-1,c-1,s%(2*R-2),direction[d],z))
    else:
        shark.append((r-1,c-1,s%(2*C-2),direction[d],z))
    board[r-1][c-1] = z
        
answer=0
for i in range(C):
    catch(i)
    move()
print(answer)

