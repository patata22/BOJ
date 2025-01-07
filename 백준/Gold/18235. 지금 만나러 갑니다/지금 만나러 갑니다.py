from collections import deque

dx=(-1,1)

def sol():
    q=deque()
    q.append((a,0))
    q.append((b,1))
    visited=[-1]*(n+1)
    visited[a]=0
    t=1
    while q:
        for _ in range(len(q)):
            x,isSecond=q.popleft()
            jump = 1<<(t-1)
            if not isSecond:
                for i in range(2):
                    nx=x+dx[i]*jump
                    if 0<nx<=n:
                        visited[nx]=t
                        q.append((nx,isSecond))
            else:
                for i in range(2):
                    nx=x+dx[i]*jump
                    if 0<nx<=n:
                        if visited[nx]==t: return t
                        q.append((nx,isSecond))
        t+=1
    return -1

n,a,b=map(int,input().split())
print(sol())
