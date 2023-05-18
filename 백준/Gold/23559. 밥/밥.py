import sys,heapq
input=sys.stdin.readline

n,x=map(int,input().split())
x-=1000*n
q=[]
answer=0
for _ in range(n):
    a,b=map(int,input().split())
    heapq.heappush(q,b-a)
    answer+=b

for _ in range(x//4000):
    temp=heapq.heappop(q)
    if temp>0: break
    answer-=temp

print(answer)
