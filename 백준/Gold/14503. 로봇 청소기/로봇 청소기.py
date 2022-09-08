dx=(-1,0,1,0)
dy=(0,-1,0,1)


n,m=map(int,input().split())
x,y,d=map(int,input().split())
if d%2: d=(d+2)%4

board=[list(map(int,input().split())) for i in range(n)]
clear=[[0]*m for i in range(n)]
clear[x][y]=1
answer=1


Done=False
while not Done:
    Done=True
    Back=True
    for i in range(1,5):
        nd=(d+i)%4
        nx,ny=x+dx[nd],y+dy[nd]
        if board[nx][ny]==0 and not clear[nx][ny]:
            clear[nx][ny]=1
            answer+=1
            x,y,d=nx,ny,nd
            Done=False
            Back=False
            break
    if Back:
        nx,ny=x-dx[d],y-dy[d]
        if board[nx][ny]==0:
            x,y=nx,ny
            Done=False
        
print(answer)
