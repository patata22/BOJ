import sys,heapq
input=sys.stdin.readline

def sol():
    q=[]
    distance=[[float('inf')]*(T+1) for i in range(n+1)]
    q.append((0,0,1))
    distance[1]=[0]*(T+1)
    while q:
        money,time,now=heapq.heappop(q)
        if distance[now][time]!=money: continue
        if now==n: return money
        for to,t,m in graph[now]:
            if time+t<=T and money+m<=M:
                if distance[to][time+t]>money+m:
                    distance[to][time+t]=money+m
                    heapq.heappush(q,(money+m,time+t,to))
                    for i in range(time+t+1,T+1):
                        if distance[to][time+t]<money+m:break
                        distance[to][time+t]=money+m
    return -1
                            
    

n=int(input())
T,M=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(int(input())):
    a,b,t,m=map(int,input().split())
    graph[a].append((b,t,m))
    graph[b].append((a,t,m))

print(sol())