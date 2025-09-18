import sys,heapq
input=sys.stdin.readline

n,m=map(int,input().split())

number=[]
for _ in range(n):
    a,b=map(int,input().split())
    number.append((a,a+b))

number.sort(reverse=True)

answer=0

q=[]
while number:
    start,end=number.pop()
    while q and q[0]+m<start:  heapq.heappop(q)
    if q and q[0]<=start<=q[0]+m:
        heapq.heappop(q)
        heapq.heappush(q,end)
    else:
        answer+=1
        heapq.heappush(q,end)

print(n-answer)