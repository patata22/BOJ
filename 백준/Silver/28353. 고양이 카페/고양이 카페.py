from collections import deque

n,k=map(int,input().split())

answer=0

q=deque(sorted(map(int,input().split())))

while len(q)>1:
    if q[0]+q[-1]<=k:
        answer+=1
        q.popleft()
        q.pop()
    else: q.pop()
print(answer)
