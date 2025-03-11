import sys,heapq
input=sys.stdin.readline


def sol(s,e):
    q=[]
    distance=[(float('inf'),float('inf'))]*n
    q.append((0,0,s))
    distance[s]=(0,0)
    while q:
        outside,inside,now = heapq.heappop(q)
        if distance[now][0]!=outside or distance[now][1]!=inside:
            continue
        if now==e: return outside,inside

        for to,dist,isOutside in graph[now]:
            if isOutside:
                if distance[to][0]>outside+dist:
                    distance[to]=(outside+dist,inside)
                    heapq.heappush(q,(outside+dist,inside,to))
                elif distance[to][0]==outside+dist and distance[to][1]>inside:
                    distance[to]=(outside+dist,inside)
                    heapq.heappush(q,(outside+dist,inside,to))

            else:
                if distance[to][0]>outside:
                    distance[to]=(outside,inside+dist)
                    heapq.heappush(q,(outside,inside+dist,to))
                elif distance[to][0]==outside and distance[to][1]>inside+dist:
                    distance[to]=(outside,inside+dist)
                    heapq.heappush(q,(outside,inside+dist,to))
    return ['IMPOSSIBLE']

n,m,p=map(int,input().split())

graph=[[] for i in range(n)]
for _ in range(m):
    a,b,c,d = input().split()
    a,b,c=int(a),int(b),int(c)
    if d=='O': d=1
    else: d=0
    graph[a].append((b,c,d))
    graph[b].append((a,c,d))

for _ in range(p):
    a,b=map(int,input().split())
    print(*sol(a,b))