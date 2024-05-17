dx=(-1,1,0,0)
dy=(0,0,-1,1)

def check(x,y):
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if not (0<=nx<n and 0<=ny<n) or used[nx][ny]:
            return False
    return True


def sol(depth, cost):
    global answer
    if depth==3:
        answer=min(answer,cost)
        return
    for x in range(n):
        for y in range(n):
            if not used[x][y] and check(x,y):
                c=board[x][y]
                for i in range(4):
                    nx,ny=x+dx[i],y+dy[i]
                    used[nx][ny]=1
                    c+=board[nx][ny]
                sol(depth+1, cost+c)
                for i in range(4):
                    nx,ny=x+dx[i],y+dy[i]
                    used[nx][ny]=0
            

n=int(input())
board=[list(map(int,input().split())) for i in range(n)]
used=[[0]*n for i in range(n)]
answer=float('inf')
sol(0,0)
print(answer)
