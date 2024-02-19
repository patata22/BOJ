import heapq

n,k=map(int,input().split())
number=list(map(int,input().split()))[::-1]
q=[]
now=0
answer=0
while len(q)<k and number:
    heapq.heappush(q,number.pop())

while number:
    finished=heapq.heappop(q)
    answer=max(answer,finished-now)
    now=finished
    heapq.heappush(q,number.pop()+now)
while q:
    finished=heapq.heappop(q)
    answer=max(answer,finished-now)
    now=finished

print(answer)
    