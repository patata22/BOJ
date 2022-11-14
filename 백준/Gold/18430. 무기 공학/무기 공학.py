#18430

dx1=(0,1)
dy1=(-1,0)

dx2=(-1,0)
dy2=(0,-1)

dx3=(-1,0)
dy3=(0,1)

dx4=(0,1)
dy4=(1,0)

dx=(dx1,dx2,dx3,dx4)
dy=(dy1,dy2,dy3,dy4)

def check(x,y,d):
    dxi,dyi = dx[d], dy[d]
    for i in range(2):
        nx,ny= x+dxi[i], y+dyi[i]
        if not (0<=nx<n and 0<=ny<m and not used[nx][ny]):
            return False
    return True
    
def sol(a,b,now):
    global answer
    answer=max(answer,now)
    for i in range(a,min(a+1,n)):
        for j in range(b,min(b+1,m)):
            if b!=m-1: sol(a,b+1,now)
            else: sol(a+1,0, now)
            if not used[i][j]:
                for k in range(4):
                    if check(i,j,k):
                        dxi,dyi = dx[k],dy[k]
                        for l in range(2):
                            nx, ny = i+dxi[l], j+dyi[l]
                            now+=board[nx][ny]
                            used[nx][ny]=1
                        now+=2*board[i][j]
                        used[i][j]=1
                        sol(a,b,now)
                        used[i][j]=0
                        now-=2*board[i][j]
                        for l in range(2):
                            nx,ny= i+dxi[l], j+dyi[l]
                            now-=board[nx][ny]
                            used[nx][ny]=0
                            
                    
    

n,m= map(int,input().split())

board=[list(map(int,input().split())) for i in range(n)]

used=[[0]*m for i in range(n)]

answer=0

sol(0,0,0)

print(answer)
