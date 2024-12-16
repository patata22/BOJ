import sys,heapq
input=sys.stdin.readline

def sol():
    q=[]
    q.append((0,0))
    distance=[float('inf')]*(n+1)
    distance[0]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]!=dist: continue
        for s,e in plan:
            if s<=now: continue
            gap=max(dist,s-now-1)
            if distance[e]>gap:
                distance[e]=gap
                heapq.heappush(q,(gap,e))
    answer=float('inf')
    for i in range(n+1):
        blank=max(distance[i],n-i)
        if blank<answer:
            answer=blank
    return answer

n=int(input())
m=int(input())
plan=[tuple(map(int,input().split())) for i in range(m)]
print(sol())
