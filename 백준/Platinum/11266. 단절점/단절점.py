import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
def dfs(now,root):
    global unused
    unused+=1
    visited[now]=unused
    ret=unused
    count=0
    for to in graph[now]:
        if visited[to]:
            ret=min(ret,visited[to])
            continue
        count+=1
        
        prev = dfs(to,0)
        if not root and prev>=visited[now]:
            cut[now]=1
        ret=min(ret,prev)
    if root and count>=2:
        cut[now]=1
    return ret
n,m=map(int,input().split())

graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[0]*(n+1)
cut=[0]*(n+1)
unused=0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i,1)
count=0
answer=[]
for i in range(1,n+1):
    if cut[i]:
        answer.append(i)
        count+=1
print(count)
answer.sort()
print(*answer)
