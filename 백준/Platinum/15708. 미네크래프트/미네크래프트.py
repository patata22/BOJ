import heapq

n,T,p=map(int,input().split())
T+=p
use=0
stone=list(map(int,input().split()))
answer=0
q=[]
for x in stone:
    T-=p
    use+=x
    heapq.heappush(q,-x)
    while use>T:
        if not q: break
        use+=heapq.heappop(q)
    answer=max(answer,len(q))
print(answer)

