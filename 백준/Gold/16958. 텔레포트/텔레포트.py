import sys
input=sys.stdin.readline

n,t=map(int,input().split())
special=[0]*n
spe=[]
city=[]
spedist=[float('inf')]*n
for i in range(n):
    s,x,y=map(int,input().split())
    special[i]=s
    if s: spe.append((x,y))
    city.append((x,y))

for i in range(n):
    if special[i]:
        spedist[i]=0
    else:
        x1,y1=city[i]
        for x2,y2 in spe:
            spedist[i] = min(spedist[i],abs(x1-x2)+abs(y1-y2))

for _ in range(int(input())):
    a,b=map(int,input().split())
    a-=1
    b-=1
    x1,y1=city[a]
    x2,y2=city[b]
    dist=abs(x1-x2)+abs(y1-y2)
    if special[a] and special[b]:print(min(dist,t))
    else:
        print(min(abs(x1-x2)+abs(y1-y2),spedist[a]+spedist[b]+t))
