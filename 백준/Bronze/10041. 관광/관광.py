import sys
input=sys.stdin.readline

w,h,n=map(int,input().split())
x,y=map(int,input().split())
answer=0
for _ in range(n-1):
    nx,ny=map(int,input().split())
    if (nx>=x and ny>=y) or (x>=nx and y>=ny):
        tx=abs(nx-x)
        ty=abs(ny-y)
        tz=min(tx,ty)
        answer+=tx+ty-tz
    else:answer+=abs(nx-x)+abs(ny-y)
    x,y=nx,ny

print(answer)