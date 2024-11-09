dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol(x,y):
    visited[x][y]=1
    d=0
    while True:
        cnt=0
        while not (0<=x+dx[direction[d]]<n and 0<=y+dy[direction[d]]<m and not visited[x+dx[direction[d]]][y+dy[direction[d]]]):
            cnt+=1
            d=(d+1)%D
            if cnt==4: return x,y
        x=x+dx[direction[d]]
        y=y+dy[direction[d]]
        visited[x][y]=1
        

n,m=map(int,input().split())
visited=[[0]*m for i in range(n)]
for _ in range(int(input())):
    a,b=map(int,input().split())
    visited[a][b]=1
x,y=map(int, input().split())
direction=list(map(lambda x: int(x)-1, input().split()))
D=len(direction)

print(*sol(x,y))
