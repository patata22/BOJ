from collections import deque

dx=(1,0)
dy=(0,1)


def sol():
    q=deque()
    q.append((0,0))
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            for  i in range(2):
                nx,ny = x+dx[i],y+dy[i]
                if 0<=nx<=n and 0<=ny<=m:
                    if (x,y,nx,ny) in fix or (nx,ny,x,y) in fix: continue
                    dp[nx][ny]+=dp[x][y]
                    if not visited[nx][ny]:
                        visited[nx][ny]=1
                        q.append((nx,ny))
                

n,m=map(int,input().split())

fix=set()
for _ in range(int(input())):
    fix.add(tuple(list(map(int,input().split()))))

dp=[[0]*(m+1) for i in range(n+1)]
dp[0][0]=1
visited=[[0]*(m+1) for i in range(n+1)]
sol()
print(dp[-1][-1])
