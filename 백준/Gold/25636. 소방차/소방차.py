import sys,heapq
input=sys.stdin.readline

def sol():
    q=[]
    heapq.heappush(q, (0,-water[s],s))
    distance[s]=0
    tank[s] = water[s]
    while q:
        dist, w, now = heapq.heappop(q)
        if distance[now]!=dist or tank[now]!=-w: continue
        if now==e: return dist, -w
        for W, d,to in graph[now]:
            if distance[to]>dist+d:
                distance[to]=dist+d
                tank[to]=-(w+W)
                heapq.heappush(q, (dist+d, w+W, to))
            elif distance[to]==dist+d and tank[to]<-w-W:
                tank[to]=-(w+W)
                heapq.heappush(q,(dist+d, w+W, to))
    return -1

n=int(input())
water=[0]+list(map(int,input().split()))
graph = [[] for i in range(n+1)]
distance = [float('inf')]*(n+1)
tank = [float('inf')]*(n+1)
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    graph[a].append((-water[b],c,b))
    graph[b].append((-water[a],c,a))

for i in range(1,n+1): graph[i].sort()

s,e = map(int,input().split())

answer= sol()
if type(answer)==tuple: print(*answer)
else: print(answer)
