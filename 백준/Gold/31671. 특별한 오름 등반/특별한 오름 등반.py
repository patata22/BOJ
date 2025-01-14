import sys
input=sys.stdin.readline

n,m=map(int,input().split())
teacher=set()
for _ in range(m):
    teacher.add(tuple(map(int,input().split())))

dp=[[-1]*(n+1) for i in range(2*n+1)]
dp[0][0]=0
for x in range(1,n+1):
    for y in range(n+1):
        if y>x: break
        if (x,y) in teacher: continue
        for k in (-1,1):
            ny=y+k
            if (x-1,ny) in teacher: continue
            if 0<=ny<=x and dp[x-1][ny]!=-1:
                dp[x][y]=max(y,dp[x-1][ny])

for x in range(n+1,2*n+1):
    for y in range(n+1):
        if x+y>2*n: continue
        if (x,y) in teacher: continue
        for k in (-1,1):
            ny=y+k
            if (x-1,ny) in teacher: continue
            if 0<=ny and dp[x-1][ny]!=-1:
                dp[x][y]=max(y,dp[x-1][ny])
                
print(dp[-1][0])