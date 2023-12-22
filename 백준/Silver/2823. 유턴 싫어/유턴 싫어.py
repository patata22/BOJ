dx=(-1,1,0,0)
dy=(0,0,-1,1)

n,m=map(int,input().split())
board=[list(input()) for i in range(n)]
answer=0
for x in range(n):
    for y in range(m):
        if board[x][y]=='.':
            temp=0
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]=='.':
                    temp+=1
            if temp==1: answer=1
print(answer)