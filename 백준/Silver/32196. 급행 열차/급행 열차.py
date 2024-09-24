import sys
input=sys.stdin.readline

n,m,k,x,y=map(int,input().split())
ka,kb=k,k
station=[]
for _ in range(n):
    a,b=map(int,input().split())
    station.append((a,b,x*a,y*b))

station.sort(key=lambda x: x[2]-x[3])
for i in range(m):
    ka+=station[i][0]
    kb-=station[i][1]

print(ka*x+kb*y)
