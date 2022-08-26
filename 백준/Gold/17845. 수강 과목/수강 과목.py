import sys
input=sys.stdin.readline

n,k=map(int,input().split())
time= [tuple(map(int,input().split())) for i in range(k)]

dp=[[0]*(n+1) for i in range(k)]
for i in range(k):
    v,w=time[i]
    for j in range(n+1):
        if j<w: dp[i][j]=dp[i-1][j]
        else: dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+v)
        
print(dp[-1][-1])