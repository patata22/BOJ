import sys,heapq
input=sys.stdin.readline

time=[]
for _ in range(int(input())):
    n,start,end=list(map(int,input().split()))
    time.append((start,end))
time.sort()

q=[]
answer=0
for start,end in time:
    if (not q) or start<q[0]:
        answer+=1
    elif start>=q[0]:
        heapq.heappop(q)
    heapq.heappush(q,end)

print(answer)
