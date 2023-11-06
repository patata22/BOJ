n,m,h=map(int,input().split())
board=[[list(input()) for i in range(n)] for i in range(h)]

for z in range(h):
    for x in range(n):
        for y in range(m):
            if board[z][x][y]!='.': continue
            temp=0
            for i in range(-1,2):
                for j in range(-1,2):
                    for k in range(-1,2):
                        nx,ny,nz=x+i,y+j,z+k
                        if 0<=nx<n and 0<=ny<m and 0<=nz<h and board[nz][nx][ny]=='*':
                            temp+=1
            board[z][x][y]=temp%10

for z in range(h):
    for x in range(n):
        print(*board[z][x],sep='')