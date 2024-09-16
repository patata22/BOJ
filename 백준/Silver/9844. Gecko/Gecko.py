dy=(-1,0,1)

n,m=map(int,input().split())
board=[list(map(int,input().split())) for i in range(n)]

for x in range(1,n):
    for y in range(m):
        temp=0
        for k in range(3):
            ny=y+dy[k]
            if 0<=ny<m:
                temp=max(temp,board[x-1][ny])
        board[x][y]+=temp
print(max(board[-1]))
