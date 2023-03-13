dx=(-1,-1,-1,0,0,1,1,1)
dy=(-1,0,1,-1,1,-1,0,1)

r,s=map(int,input().split())
board=[list(input()) for i in range(r)]

sang=0
answer=0

for x in range(r):
    for y in range(s):
        temp=0
        for k in range(8):
            nx,ny=x+dx[k], y+dy[k]
            if 0<=nx<r and 0<=ny<s and board[nx][ny]=='o':temp+=1
        if board[x][y]=='.': sang=max(sang,temp)
        else: answer+=temp
            
print(answer//2+sang)
