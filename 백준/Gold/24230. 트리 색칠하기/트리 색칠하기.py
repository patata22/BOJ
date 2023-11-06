from collections import deque
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def makeTree():
    q=deque()
    q.append(1)
    depth[1]=0
    t=1
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            for to in graph[now]:
                if depth[to]<0:
                    depth[to]=t
                    q.append(to)
        t+=1

def fillColor(now,col):
    global answer
    c=col
    if goal[now]!=c:
        c=goal[now]
        answer+=1
    for to in graph[now]:
        if depth[to]>depth[now]:
            fillColor(to,c)
        
        
                    
n=int(input())
goal=[0]+list(map(int,input().split()))
depth=[-1]*(n+1)

graph=[[] for i in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
makeTree()
answer=0
fillColor(1,0)
print(answer)
        
