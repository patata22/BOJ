import sys,heapq
input=sys.stdin.readline

def sol(u1,u2,v1,v2,t):
    q=[]
    q.append((0,u1,u2))
    distance=[[float('inf')]*51 for i in range(n+1)]
    distance[u1][u2]=0
    while q:
        dist,line,station = heapq.heappop(q)
        if distance[line][station]!=dist: continue
        if line==v1 and station==v2: return dist
        total=temp[line]
        for nxt in (station-1,station+1):
            if 1<=nxt<=total and distance[line][nxt]>dist+1:
                distance[line][nxt]=dist+1
                heapq.heappush(q,(dist+1,line,nxt))
        for nxtline, nxt in graph[line][station]:
            if distance[nxtline][nxt]>dist+t:
                distance[nxtline][nxt]=dist+t
                heapq.heappush(q,(dist+t,nxtline,nxt))
                
n=int(input())
temp=[0]+list(map(int,input().split()))
graph=[[[] for i in range(51)] for i in range(n+1)]

for _ in range(int(input())):
    p1,p2,q1,q2=map(int,input().split())
    graph[p1][p2].append((q1,q2))
    graph[q1][q2].append((p1,p2))

for _ in range(int(input())):
    t,u1,u2,v1,v2=map(int,input().split())
    print(sol(u1,u2,v1,v2,t))