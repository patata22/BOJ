from collections import deque

def sol():
    q=deque()
    q.append((1,0,0)) #now, record, count
    visited[1][0]=0
    while q:
        now, record, count=q.popleft()
        for to, w in graph[now]:
            if count<=w:
                if jewel[to]>=0:
                    temp=1<<jewel[to]
                    if jewel[to]>=0 and record&temp==0 and visited[to][record|temp]==-1:
                        visited[to][record|temp]=count+1
                        q.append((to, record|temp, count+1))
                if visited[to][record]==-1:
                    visited[to][record]=count
                    q.append((to,record,count))
    return max(visited[1])
n,m,k=map(int,input().split())

jewel=[-1]*(n+1)
for i in range(k):
    jewel[int(input())]=i
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
visited=[[-1]*(1<<k) for i in range(n+1)]

print(sol())
