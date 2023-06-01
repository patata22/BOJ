from collections import deque
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

from collections import deque

def sol(x):
    q=deque()
    q.append((x,0))
    visited=[0]*(n+1)
    maxdist=0
    maxpoint=0
    visited[x]=1
    while q:
        now,dist=q.popleft()
        if dist>maxdist:
            maxdist=dist
            maxpoint=now
        for to,d in graph[now]:
            if not visited[to]:
                visited[to]=1
                q.append((to,dist+d))
    return maxdist,maxpoint

n=int(input())
graph=[[] for i in range(n+1)]
for _ in range(n):
    temp=list(map(int,input().split()))
    a=temp[0]
    temp.pop()
    for i in range(1,len(temp),2):
        b=temp[i]
        c=temp[i+1]
        graph[a].append((b,c))


print(sol(sol(1)[1])[0])
