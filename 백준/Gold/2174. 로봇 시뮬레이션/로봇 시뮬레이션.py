dx=(1,0,-1,0)
dy=(0,1,0,-1)
dir={'N':0,'E':1,'S':2,'W':3}

c,r=map(int,input().split())
board=[[0]*(c+1) for i in range(r+1)]


n,m=map(int,input().split())
direction=[0]*(n+1)
location=[0]
for i in range(1,n+1):
    b,a,C=input().split()
    board[int(a)][int(b)]=i
    location.append([int(a),int(b)])
    direction[i]=dir[C]

answer='OK'
problem=False
for i in range(m):
    if problem:break
    num,com,mul=input().split()
    num=int(num)
    mul=int(mul)
    if com=='R':
        direction[num]=(direction[num]+(mul%4))%4
    elif com=='L':
        direction[num]=(direction[num]-(mul%4))%4
    else:
        X,Y=location[num]
        d=direction[num]
        for j in range(mul):
            
            nx,ny=X+dx[d],Y+dy[d]
        
            if not (0<nx<=r and 0<ny<=c):
                answer=f'Robot {num} crashes into the wall'
                problem=True
                break
            elif board[nx][ny] not in (0,num):
                answer=f'Robot {num} crashes into robot {board[nx][ny]}'
                problem=True
                break
            X,Y=nx,ny
        board[X][Y]=num
        x,y=location[num]
        board[x][y]=0
        location[num]=X,Y

print(answer)
                
