import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())

graph=[[-float('inf')]*n for i in range(n)]
for _ in range(k):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    
    if a<b and graph[a][b]<c:
        graph[a][b]=c
dp=[[-float('inf')]*n for i in range(m)]
dp[0][0]=0
for k in range(1,m):
    for i in range(n):
        for j in range(i+1,n):
            if dp[k][i]:
                dp[k][j]=max(dp[k][j],dp[k-1][i]+graph[i][j])

answer=0
for i in range(m):
        if dp[i][n-1]>answer:
            answer=dp[i][n-1]
print(answer)
