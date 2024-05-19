import heapq

n,m,k=map(int,input().split())
work=[]
for _ in range(n):
    heapq.heappush(work,-int(input()))
happy=0
day=0
answer=[]
while -work[0]>k:
    day+=1
    sati=-heapq.heappop(work)
    happy= happy//2+sati
    answer.append(happy)
    heapq.heappush(work,-(sati-m))
print(day)
for x in answer:print(x)