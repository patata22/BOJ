from collections import deque

def solution(x, y, n):
    q=deque()
    q.append(y)
    visited=[0]*(y+1)
    visited[y]=1
    t=0
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            if now==x: return t
            if now>=n and not visited[now-n]:
                visited[now-n]=1
                q.append(now-n)
            if not now%2 and not visited[now//2]:
                visited[now//2]=1
                q.append(now//2)
            if not now%3 and not visited[now//3]:
                visited[now//3]=1
                q.append(now//3)
        t+=1
    return -1
