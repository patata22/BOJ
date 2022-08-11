from collections import deque

t=1

n=int(input())
q=deque([i for i in range(1,n+1)])
while len(q)>1:
    q.rotate(-(t**3-1))
    q.popleft()
    t+=1
print(q[0])
