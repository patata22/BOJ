from collections import deque

dx=(0,-1,1,0,0)
dy=(0,0,0,-1,1)

def choice(x,y, board):
    temp=[]
    for i in range(3):
        temp.append(board[i][:])
    for i in range(5):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<3 and 0<=ny<3:
            if temp[nx][ny]=='*': temp[nx][ny]='.'
            else: temp[nx][ny]='*'
    return temp
    

def record(b):
    temp=""
    for i in range(3):
        temp+="".join(b[i])
    return temp

def sol():
    q=deque()
    q.append(board)
    t=0
    while q:
        for _ in range(len(q)):
            b = q.popleft()
            if b[0]==b[1]==b[2]==['.','.','.']: return t
            for i in range(3):
                for j in range(3):
                    temp= choice(i,j,b)
                    if record(temp) not in visited:
                        visited[record(temp)]=1
                        q.append(temp)
    

        t+=1
for _ in range(int(input())):
    board=[list(input()) for i in range(3)]
    visited= {}
    visited[record(board)]=1
    print(sol())
