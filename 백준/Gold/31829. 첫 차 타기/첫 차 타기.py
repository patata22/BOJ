import sys,heapq
input=sys.stdin.readline

def sol():
    q=[]
    distance=[float('inf')]*(N+1)
    q.append((0,1))
    distance[1]=0
    while q:
        dist,now= heapq.heappop(q)
        if distance[now]!=dist:continue
        if now==N: return dist
        for to,d in road[now]:
            if distance[to]>dist+d:
                distance[to]=dist+d
                heapq.heappush(q,(dist+d,to))
        if dist>=K:
            for to,d in bus[now]:
                if distance[to]>dist+d:
                    distance[to]=dist+d
                    heapq.heappush(q,(dist+d,to))
        else:
            wait=K-dist
            for to,d in bus[now]:
                if distance[to]>dist+d+wait:
                    distance[to]=dist+d+wait
                    heapq.heappush(q,(dist+d+wait,to))
                    
N,K,X,Y=map(int,input().split())
road=[[] for i in range(N+1)]
for _ in range(X):
    a,b,c=map(int,input().split())
    road[a].append((b,c))
    road[b].append((a,c))
bus=[[] for i in range(N+1)]
for _ in range(Y):
    a,b,c=map(int,input().split())
    bus[a].append((b,c))
    bus[b].append((a,c))


print(sol())
