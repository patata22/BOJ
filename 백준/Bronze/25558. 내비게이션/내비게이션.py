import sys
input=sys.stdin.readline

n=int(input())
sx,sy,ex,ey=map(int,input().split())
dist=float('inf')
answer=0
for _ in range(1,n+1):
    x,y=sx,sy
    temp=0
    for __ in range(int(input())):
        nx,ny=map(int,input().split())
        temp+=abs(nx-x)+abs(ny-y)
        x,y=nx,ny
    temp+=abs(ex-x)+abs(ey-y)
    if temp<dist:
        dist=temp
        answer=_
print(answer)
        
