from collections import deque
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def makeTree():
    q=deque()
    q.append(1)
    visited[1]=1
    while q:
        now=q.popleft()
        for to in graph[now]:
            if not visited[to]:
                visited[to]=1
                parent[to]=now
                q.append(to)
                
        

def sol(now):
    visited[now]=1
    count=0
    for to in graph[now]:
        if not visited[to]:
            count+=sol(to)
    if isIndoor[now]:
        global answer
        answer+=2*count
        return 1
    else:
        if parent[now]==-1 or (parent[now]!=-1 and isIndoor[parent[now]]):
            answer+=(count*(count-1))
        return count
    
    
n=int(input())
isIndoor=[0]+list(map(int,input().rstrip()))
graph=[[] for i in range(n+1)]
parent=[-1]*(n+1)
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[0]*(n+1)
makeTree()
visited=[0]*(n+1)
answer=0
sol(1)
print(answer)
