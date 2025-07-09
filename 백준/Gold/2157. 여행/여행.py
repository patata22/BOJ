import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
graph=[[] for i in range(n+1)]

for _ in range(k):
    a,b,c=map(int,input().split())
    if a>b: continue
    graph[b].append((a,c))

dp=[[-float('inf')]*(m+1) for i in range(n+1)]
dp[1][1]=0
for now in range(2,n+1):
    for v in range(2,m+1):
        for prev,d in graph[now]:
            dp[now][v]=max(dp[now][v],dp[prev][v-1]+d)

print(max(dp[-1]))