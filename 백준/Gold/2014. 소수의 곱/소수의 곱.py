import heapq

MAX = 2**31

k,n=map(int,input().split())
prime = tuple(map(int,input().split()))
q=[]
for p in prime:
    q.append(p)

count = 0
for i in range(n):
    now = heapq.heappop(q)
    for p in prime:
        temp = p*now
        if temp<MAX:
            heapq.heappush(q, temp)
            if now%p==0: break

print(now)
