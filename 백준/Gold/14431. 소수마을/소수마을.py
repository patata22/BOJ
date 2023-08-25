import sys,heapq
input=sys.stdin.readline

def sieve():
    for i in range(2,8500):
        if isPrime[i]:
            for j in range(i+i,8500,i):
                isPrime[j]=0

def distance(x1,y1,x2,y2):
    return int(((x1-x2)**2+(y1-y2)**2)**0.5)

isPrime=[1]*8500
isPrime[0]=0
isPrime[1]=0
sieve()

def dijkstra():
    q=[]
    q.append((0,0))
    distance=[float('inf')]*(n+2)
    distance[0]=0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now]!=dist: continue
        if now==1: return dist
        for to,d in graph[now]:
            if distance[to]>dist+d:
                distance[to]=dist+d
                heapq.heappush(q,(dist+d,to))
    return -1

x1,y1,x2,y2=map(int,input().split())
point=[(x1,y1),(x2,y2)]
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    point.append((a,b))
graph= [[] for i in range(n+2)]
for i in range(n+2):
    x1,y1=point[i]
    for j in range(i+1,n+2):
        x2,y2=point[j]
        d = distance(x1,y1,x2,y2)
        if isPrime[d]:
            graph[i].append((j,d))
            graph[j].append((i,d))

print(dijkstra())