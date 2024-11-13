import sys,heapq
input=sys.stdin.readline


def sol():
    q=[]
    q.append((0,0,0))
    distance=[[float('inf')]*(n+1) for i in range(m+1)]
    distance[0][0]=0
    while q:
        dist,day,now=heapq.heappop(q)
        if distance[day][now]!=dist: continue
        if now==n: return dist
        if day==m: continue
        if distance[day+1][now]>dist:
            distance[day+1][now]=dist
            heapq.heappush(q,(dist,day+1,now))
        d=city[now]*weather[day]
        if distance[day+1][now+1]>dist+d:
            distance[day+1][now+1]=dist+d
            heapq.heappush(q,(dist+d,day+1,now+1))
n,m=map(int,input().split())

city=[int(input()) for i in range(n)]
weather=[int(input()) for i in range(m)]

print(sol())
