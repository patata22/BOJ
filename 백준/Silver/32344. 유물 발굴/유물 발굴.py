import sys
input=sys.stdin.readline

r,c=map(int,input().split())
n=int(input())

lx=[float('inf')]*(n+1)
ly=[float('inf')]*(n+1)
rx=[-float('inf')]*(n+1)
ry=[-float('inf')]*(n+1)
target=[]
for _ in range(n):
    a,b,c=map(int,input().split())
    lx[a]=min(lx[a],b)
    ly[a]=min(ly[a],c)
    rx[a]=max(rx[a],b)
    ry[a]=max(ry[a],c)
    target.append(a)

size=0
answer=0
target.sort()
for x in target:
    s = (rx[x]-lx[x]+1)*(ry[x]-ly[x]+1)
    if s>size:
        size=s
        answer=x
print(answer,size)
