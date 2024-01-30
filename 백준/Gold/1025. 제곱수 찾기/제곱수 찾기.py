dx=(-1,1,-1,1)
dy=(-1,1,1,-1)

n,m=map(int,input().split())
board=[list(map(int,input())) for i in range(n)]
answer=-float('inf')
for i in range(n):
    for j in range(m):
        if board[i][j] in (0,1,4,9): answer=max(answer,board[i][j])
        for rowgap in range(n):
            for colgap in range(m):
                if rowgap==0 and colgap==0: continue
                for d in range(4):
                    temp=0
                    x,y=i,j
                    while 0<=x<n and 0<=y<m:
                        temp*=10
                        temp+=board[x][y]
                        if (temp**0.5)%1==0: answer=max(answer,temp)
                        x+=rowgap*dx[d]
                        y+=colgap*dy[d]
if answer==-float('inf'):print(-1)
else:print(answer)