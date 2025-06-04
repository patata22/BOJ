from collections import deque

MAX=4000000

def sol(x):
    q=deque()
    q.append(1)
    visited=set()
    visited.add(1)
    t=0
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            if now==x: return t
            if now*2<=MAX and now*2 not in visited:
                visited.add(now*2)
                q.append(now*2)
            if now>1 and now-1 not in visited:
                visited.add(now-1)
                q.append(now-1)
        t+=1
        
    return 'Wrong proof'

for tt in range(int(input())):
    print(sol(int(input())))
