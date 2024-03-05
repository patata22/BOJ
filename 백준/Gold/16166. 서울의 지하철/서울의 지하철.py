from collections import deque

def sol():
    q=deque()
    visited=[0]*n
    for x in starts:
        q.append(x)
        visited[x]=1
    t=0
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            if now in ends: return t
            for to in graph[now]:
                if not visited[to]:
                    visited[to]=1
                    q.append(to)
        t+=1
    return -1
        
n=int(input())
graph=[[] for i in range(n)]
stations=[list(map(int,input().split()))[1:] for i in range(n)]
starts=set()
s=0
ends=set()
e=int(input())
for i in range(n):
    a=stations[i]
    for j in range(n):
        b=stations[j]
        for x in a:
            if x==s:starts.add(i)
            if x==e: ends.add(i)
            if x in b:
                graph[i].append(j)
                
                
print(sol())
