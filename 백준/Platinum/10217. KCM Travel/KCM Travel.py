
import sys,heapq
input=sys.stdin.readline

def sol():
    q=[]
    q.append((0,0,1))
    distance=[[float('inf')]*(M+1) for i in range(n+1)]
    distance[1]=[0]*(M+1)
    while q:
        time,money,now=heapq.heappop(q)
        if distance[now][money]!=time: continue
        if now==n: return time
        for to,m,t in graph[now]:
            if money+m>M:continue
            if distance[to][money+m]>time+t:
                distance[to][money+m]=time+t
                for i in range(money+m+1,M+1):
                    if distance[to][i]<=time+t: break
                    distance[to][i]=time+t
                
                heapq.heappush(q,(time+t, money+m,to))

    return "Poor KCM"

for tt in range(int(input())):
    n,M,k=map(int,input().split())
    graph=[[] for i in range(n+1)]
    for _ in range(k):
        a,b,c,d=map(int,input().split())
        graph[a].append((b,c,d))
    for i in range(1,n+1):graph[i].sort(key=lambda x: x[2])
    print(sol())