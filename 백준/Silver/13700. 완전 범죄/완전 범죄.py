from collections import deque

def sol():
    q= deque()
    q.append(s)
    visited[s]=1
    t=0
    while q:
        for _ in range(len(q)):
            now = q.popleft()
            if now==d: return t
            for x in (-b, f):
                nnow = now+x
                if 0<nnow<=n and not visited[nnow]:
                    visited[nnow]=1
                    q.append(nnow)
        t+=1
    return 'BUG FOUND'

n,s,d,f,b,k = map(int,input().split())
board = [0]*(n+1)
visited = [0]*(n+1)
if k!=0:
    for x in map(int,input().split()): visited[x]=1

print(sol())
