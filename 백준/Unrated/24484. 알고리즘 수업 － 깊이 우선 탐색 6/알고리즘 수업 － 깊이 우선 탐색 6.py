import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(x,depth):
    global total,count
    count+=1
    visited[x]=1
    total+=count*depth
    for to in graph[x]:
        if not visited[to]:
            
            dfs(to,depth+1)
    
n,m,r=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[0]*(n+1)
count=0
total=0
for i in range(1,n+1):
    graph[i].sort(reverse=True)

dfs(r,0)
print(total)
