import sys
input=sys.stdin.readline

dx=(1,0,-1,0)
dy=(0,-1,0,1)


n,t=map(int,input().split())
x,y=0,0
d=0
now=0
for _ in range(n):
    a,b=input().rstrip().split()
    a=int(a)
    x+=dx[d]*(a-now)
    y+=dy[d]*(a-now)
    if b=='right': d=(d+1)%4
    else: d=(d-1)%4
    now=a
x+=dx[d]*(t-now)
y+=dy[d]*(t-now)
print(x,y)

