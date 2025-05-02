from collections import deque
import sys
input=sys.stdin.readline

def sol(start,graph):
    q=deque()
    q.append(start)
    visited=[float('inf')]*(n+1)
    visited[start]=0
    t=1
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            for to in graph[now]:
                if visited[to]==float('inf'):
                    visited[to]=t
                    q.append(to)
        t+=1
    return visited


while True:
    n=int(input())
    if not n: break
    start,end=map(int,input().split())

    graph=[[] for i in range(n+1)]
    graph_reverse=[[] for i in range(n+1)]
    temp=[]
    for i in range(1,int(input())+1):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph_reverse[b].append(a)
        temp.append((i,a,b))
    dist1=sol(start,graph)
    dist2=sol(end,graph_reverse)
    dist=dist1[end]
    answer=0
    for idx,i,j in temp:
        if dist1[j]+dist2[i]+1<dist:
            dist=dist1[j]+dist2[i]+1
            answer=idx
        elif dist1[j]+dist2[i]+1==dist:
            answer=min(answer,idx)
    print(dist,answer)
    

