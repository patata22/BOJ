from collections import deque
import sys
input=sys.stdin.readline

def sol(a,b):
    q=deque()
    q.append(a)
    visited=[0]*(n+1)
    visited[a]=1
    prev=[-1]*(n+1)
    while q:
        now=q.popleft()
        for to in graph[now]:
            if not visited[to]:
                prev[to]=now
                visited[to]=1
                q.append(to)

    now=b
    answer=[]
    while now!=-1:
        answer.append(reverse[now][0])
        now=prev[now]
    return ''.join(answer[::-1])
        
    

n,q=map(int,input().split())
graph=[[] for i in range(n+1)]
unused=0
trans={}
reverse={}
for _ in range(n):
    a,b=input().rstrip().split()
    if a not in trans:
        trans[a]=unused
        reverse[unused]=a
        unused+=1
    if b not in trans:
        trans[b]=unused
        reverse[unused]=b
        unused+=1
    a=trans[a]
    b=trans[b]
    graph[a].append(b)
    graph[b].append(a)

for _ in range(q):
    a,b=input().rstrip().split()
    print(sol(trans[a],trans[b]))