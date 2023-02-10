import sys,heapq
input=sys.stdin.readline

T,n=map(int,input().split())
t=0

scheduler= []
for _ in range(n):
    a,b,c = map(int,input().split())
    heapq.heappush(scheduler, (-c,a,b))

while t<T:
    t+=1
    c,a,b=heapq.heappop(scheduler)
    print(a)
    b-=1
    if b:
        heapq.heappush(scheduler, (c+1,a,b))
