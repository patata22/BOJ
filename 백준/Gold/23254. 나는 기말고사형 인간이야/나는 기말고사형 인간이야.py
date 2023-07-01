import heapq

n,m=map(int,input().split())
score=tuple(map(int,input().split()))
study=tuple(map(int,input().split()))
q=[]
total=24*n
count=0

for i,x in enumerate(score):
    heapq.heappush(q,(-study[i],x))
answer=0
while q and count<total:
    s,x=heapq.heappop(q)
    s=-s
    C=(100-x)//s
    C=min(total-count, C)
    count+=C
    x+=C*s
    if x==100: answer+=100
    else:
        heapq.heappush(q,(-(100-x),x))
for i,x in q: answer+=x
print(answer)
