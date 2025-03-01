import sys
input=sys.stdin.readline

n,m=map(int,input().split())
drug=[tuple(map(int,input().split())) for i in range(m)]
dp=[[[-float('inf')]*51 for i in range(51)] for i in range(m+1)]
for i in range(m+1):
    dp[i][0][0]=0
for i in range(1,m+1):
    r,b,x = drug[i-1]
    for j in range(51):
        for k in range(51):
            if j<r or k<b: dp[i][j][k]=dp[i-1][j][k]
            else:dp[i][j][k]=max(dp[i-1][j][k],dp[i-1][j-r][k-b]+x)

answer=[]
for i in range(n):
    r,b=map(int,input().split())
    answer.append((i+1,max(0,dp[-1][r][b])))
answer.sort(key=lambda x: (x[1],x[0]))

for x in answer: print(*x)