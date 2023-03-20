import heapq

def solution(n, works):
    q=[]
    for work in works:
        heapq.heappush(q,-work)
    
    for i in range(n):
        now=heapq.heappop(q)
        now+=1
        if now: heapq.heappush(q, now)
        if not q: break
    
    return sum(map(lambda x: x*x, q))
    