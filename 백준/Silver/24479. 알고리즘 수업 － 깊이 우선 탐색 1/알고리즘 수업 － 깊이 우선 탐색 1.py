import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

def sol(x):
    global turn
    turn+=1
    visited[x]=turn
    for y in graph[x]:
        if not visited[y]:
            visited[y]=turn
            sol(y)
            


n,m,r=map(int,input().split())
graph=[[] for i in range(n+1)]
turn=0
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()
visited=[0]*(n+1)
sol(r)
for i in range(1,n+1):
    print(visited[i])
