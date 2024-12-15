from collections import deque
import sys
input=sys.stdin.readline


def start():
    q=deque()
    q.append(1)
    visited=[0]*(n+1)
    visited[1]=1
    while q:
        now=q.popleft()
        for to in graph[now]:
            if not visited[to]:
                visited[to]=1
                q.append(to)
    return visited

def end():
    q=deque()
    q.append(n)
    visited=[0]*(n+1)
    visited[n]=1
    while q:
        now=q.popleft()
        for to in graph_reverse[now]:
            if not visited[to]:
                visited[to]=1
                q.append(to)
    return visited
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
graph_reverse=[[] for i in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph_reverse[b].append(a)

visited1=start()
visited2=end()
answer=[]

for _ in range(int(input())):
    x=int(input())
    if visited1[x]*visited2[x]: answer.append("Defend the CTP")
    else: answer.append("Destroyed the CTP")

print(*answer, sep='\n')
    
