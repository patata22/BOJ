from collections import deque
import sys
input=sys.stdin.readline


def calc(x,k):
    l=0
    r=1000
    total=2*x
    while l+1<r:
        mid=(l+r)//2
        if mid*(mid+1)*k>=total:r=mid
        else: l=mid
    return r

def sol():
    
    n,m,q,k=map(int,input().split())

    q=deque()
    visited=[-1]*n
    for x in map(int,input().split()):
        q.append(x-1)
        visited[x-1]=0
    t=1
    graph=[[] for i in range(n)]
    for _ in range(m):
        a,b=map(int,input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    while q:
        for _ in range(len(q)):
            now=q.popleft()
            for to in graph[now]:
                if visited[to]<0:
                    visited[to]=t
                    q.append(to)
        t+=1

    answer=[]
    for x in visited:
        if not x: answer.append(0)
        else:answer.append(calc(x,k))
    print(*answer)
        

sol()