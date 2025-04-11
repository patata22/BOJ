import sys
input=sys.stdin.readline

n,m=map(int,input().split())
number=[0]+[int(input()) for i in range(n)]

dp=[[-float('inf')]*2 for i in range(m+1)]
nxt=[[-float('inf')]*2 for i in range(m+1)]
dp[0][0]=0
for i in range(1,n+1):
    nxt[0][0]=max(dp[0][0],dp[1][1],dp[1][0])
    for j in range(1,m):
        nxt[j][0]=max(dp[j+1][1],dp[j+1][0])
    nxt[1][1]=dp[0][0]+number[i]
    for j in range(2,m+1):
        nxt[j][1]=dp[j-1][1]+number[i]
    dp=nxt
    nxt=[[-float('inf')]*2 for i in range(m+1)]

print(dp[0][0])