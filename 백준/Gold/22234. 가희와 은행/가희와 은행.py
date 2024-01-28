from collections import deque
import sys,heapq
input=sys.stdin.readline

n,T,w=map(int,input().split())
q=deque()
for _ in range(n):
  q.append(tuple(map(int,input().split())))
wait=[]
for _ in range(int(input())):
  p,t,c = map(int,input().split())
  heapq.heappush(wait, (c, p, t))

answer=[]

now=0
while q and now<w:
  t=min(q[0][1],T)
  now+=t
  while wait and wait[0][0]<=now:
    c,p,tt=heapq.heappop(wait)
    q.append((p,tt))
  for _ in range(t):
      answer.append(q[0][0])
  if t==q[0][1]: q.popleft()
  else:
    p,tt=q.popleft()
    q.append((p,tt-t))

print(*answer[:w], sep='\n')
