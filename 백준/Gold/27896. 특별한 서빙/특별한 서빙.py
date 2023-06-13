import heapq

n,m=map(int,input().split())
number=list(map(int,input().split()))
total=0
answer=0
q=[]
for x in number:
    heapq.heappush(q,-x)
    total+=x
    if total>=m:
        answer+=1
        total+=2*heapq.heappop(q)
print(answer)

