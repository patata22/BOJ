import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6+9)

def dfs(now,parent):
    global unused
    unused+=1
    visited[now]=unused
    ret=unused

    for to in graph[now]:
        if to==parent: continue
        if visited[to]:
            ret=min(ret,visited[to])
            continue
        prev = dfs(to,now)
        if prev>visited[now]:
            answer.append(sorted([now,to]))
        ret=min(ret,prev)
    return ret

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[0]*(n+1)
unused=0
answer=[]

dfs(1,-1)

answer.sort()
print(len(answer))
for x in answer:print(*x)
