from collections import deque

def sol():
    q=deque()
    q.append(1)
    visited[1]=1
    t=0
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            if now==100: return t
            for i in range(1,7):
                if now+i<=100:
                    nxt=move[now+i]
                    if not visited[nxt]:
                        visited[nxt]=1
                        q.append(nxt)
        t+=1
        
n,m=map(int,input().split())
move=[i for i in range(101)]
visited=[0]*101

for _ in range(n+m):
    a,b=map(int,input().split())
    move[a]=b
print(sol())