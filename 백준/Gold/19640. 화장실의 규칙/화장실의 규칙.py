from collections import deque
import sys,heapq
input=sys.stdin.readline

n,m,k=map(int,input().split())
line=[deque() for i in range(m)]

for i in range(n):
   d,h=map(int,input().split())
   if i==k: line[i%m].append((-d,-h,i%m,True))
   else: line[i%m].append((-d,-h,i%m,False))

q=[]
for i in range(m):
   if line[i]:heapq.heappush(q,line[i].popleft())

answer=0
while q:
   d,h,l,flag=heapq.heappop(q)
   if flag:break
   answer+=1
   if line[l]: heapq.heappush(q,line[l].popleft())
   
print(answer)