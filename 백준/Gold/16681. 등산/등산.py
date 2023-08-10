import sys,heapq
input=sys.stdin.readline

def dijkstra(start):
    q=[]
    q.append((0,start))
    distance=[float('inf')]*(n+1)
    distance[start]=0
    while q:
        cost, now = heapq.heappop(q)
        if distance[now]!=cost: continue
        for c,b in graph[now]:
            if distance[b]>cost+c:
                distance[b]=cost+c
                heapq.heappush(q,(cost+c,b))
    return distance


n,m,d,e=map(int,input().split())
height=[0]+list(map(int,input().split()))
graph=[[] for i in range(n+1)]
answer=-float('inf')
for i in range(m):
    a,b,c=map(int,input().split())
    if height[a]<height[b]:graph[a].append((c,b))
    elif height[b]<height[a]:graph[b].append((c,a))

distance_home = dijkstra(1)
distance_school = dijkstra(n)

for i in range(1,n+1):
    answer=max(answer, height[i]*e - d*(distance_home[i]+distance_school[i]))
if answer==-float('inf'): print("Impossible")
else: print(answer)
