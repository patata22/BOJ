import sys
input=sys.stdin.readline

dx=(0,-1,1,0,0)
dy=(0,0,0,-1,1)

def getDistance(x1,y1,x2,y2):
    return abs(x2-x1)+abs(y2-y1)

n=int(input())
x,y=map(int,input().split())
dp=[[float('inf')]*5 for i in range(n+1)]
dp[0][0]=0

for i in range(1,n+1):
    a,b=map(int,input().split())
    for j in range(5):
        nx,ny=x+dx[j],y+dy[j]
        for k in range(5):
            na,nb=a+dx[k],b+dy[k]
            dp[i][k] = min(dp[i][k],dp[i-1][j]+getDistance(nx,ny,na,nb))
    x,y=a,b

print(min(dp[-1]))