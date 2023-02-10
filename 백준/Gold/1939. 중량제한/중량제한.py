from collections import deque

def sol(mid):
    q=deque()
    q.append(x)
    visited=[0]*(n+1)
    visited[x]=1
    while q:
        now=q.popleft()
        if now==y: return True
        for z,c in graph[now]:
            if not visited[z] and c>=mid:
                visited[z]=1
                q.append(z)
    return False
                
n,m=map(int,input().split())
r=0
graph=[[] for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    r=max(r,c)

x,y=map(int,input().split())
l=0

r+=1
while l+1<r:
    mid=(l+r)//2
    if sol(mid):
        l=mid
    else:r=mid
print(l)