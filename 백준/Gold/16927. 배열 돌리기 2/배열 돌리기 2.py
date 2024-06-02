def sol():
    N=min(n,m)//2
    for i in range(N):
        count=2*(n+m-4*i)-4
        for j in range(r%count):rotate(i)
    
def rotate(depth):
    ly=depth
    ry=m-depth
    lx=depth
    rx=n-depth
    head=board[lx][ly]
    for i in range(ly,ry-1):
        board[lx][i]=board[lx][i+1]
    for i in range(lx,rx-1):
        board[i][ry-1]=board[i+1][ry-1]
    for i in range(ry-1,ly,-1):
        board[rx-1][i]=board[rx-1][i-1]
    for i in range(rx-1,lx,-1):
        board[i][ly]=board[i-1][ly]
    board[lx+1][ly]=head
    
    
n,m,r=map(int,input().split())
board=[list(map(int,input().split())) for i in range(n)]
sol()
for i in range(n): print(*board[i])
