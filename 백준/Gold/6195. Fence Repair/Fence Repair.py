import sys,heapq
input=sys.stdin.readline

q=[]
for _ in range(int(input())):heapq.heappush(q,int(input()))

answer=0
while len(q)>1:
    a,b=heapq.heappop(q),heapq.heappop(q)
    answer+=a+b
    heapq.heappush(q,a+b)

print(answer)