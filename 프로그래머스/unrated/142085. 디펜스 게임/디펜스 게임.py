import heapq

def solution(n, k, enemy):
    E=len(enemy)
    now=0
    chance=0
    q=[]
    while now<E:
        target=enemy[now]
        if n-target<0 and k:
            heapq.heappush(q,-target)
            n-=target
            n-=heapq.heappop(q)
            k-=1
        else:
            n-=target
            heapq.heappush(q,-target)
        if n<0: break
        now+=1
    return now