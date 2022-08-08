from collections import deque

def sol(mid):
    q=deque()
    q.append(s)
    visited=[0]*(n+1)
    visited[s]=1
    while q:
        now=q.popleft()
        if now==e: return True
        for b,c in graph[now]:
            if c>=mid and not visited[b]:
                
                visited[b]=1
                q.append(b)
    return False


n,m=map(int,input().split())

s,e=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


l=0
r=1000001
while l+1<r:
    mid=(l+r)//2
    if sol(mid):
        l=mid
    else: r= mid
print(l)
        
