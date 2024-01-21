import heapq

n,m=map(int,input().split())

number=sorted(list(map(int,input().split())))
q=[]
for _ in range(min(n,m)):
    heapq.heappush(q,number.pop())

while number:
    heapq.heappush(q,heapq.heappop(q)+number.pop())

print(max(q))
