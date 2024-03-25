import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5+5)

def sol(x):
    visited[x]=1
    for to in graph[x]:
        if not visited[to]:
            dp[x]+=sol(to)
    return min(0,dp[x])
    

n,p=map(int,input().split())
p-=1
graph=[[] for i in range(n)]
A=tuple(map(int,input().split()))
B=tuple(map(int,input().split()))

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

dp=[A[i]-B[i] for i in range(n)]
visited=[0]*n

answer=sol(p)
print(-answer)

