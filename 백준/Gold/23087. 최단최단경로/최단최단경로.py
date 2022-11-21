import sys, heapq
input= sys.stdin.readline

DIV = 10**9+9

def sol():
    q=[]
    q.append((0,0,X))
    distance[X] = 0
    MOVE[X]=0
    COUNT[X]=1
    while q:
        dist, move, now = heapq.heappop(q)
        C = COUNT[now]
        if distance[now]!=dist: continue
        for to,d in graph[now]:
            if distance[to]>dist+d:
                distance[to]=dist+d
                MOVE[to]=move+1
                COUNT[to]= C
                heapq.heappush(q, (dist+d, move+1, to))
            elif distance[to] == dist+d and MOVE[to]==move+1:
                COUNT[to]= (COUNT[to]+C)%DIV
    if distance[Y]==float('inf'): return -1
    else: return distance[Y], MOVE[Y], COUNT[Y]%DIV
                
n,m,X,Y = map(int,input().split())
graph = [[] for i in range(n+1)]
distance= [float('inf')]*(n+1)
MOVE = [float('inf')]*(n+1)
COUNT = [0]*(n+1)
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

answer= sol()
if answer==-1: print(answer)
else:
    for x in answer:print(x)
    
