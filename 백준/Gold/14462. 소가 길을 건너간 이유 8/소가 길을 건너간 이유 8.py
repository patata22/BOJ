import sys
input=sys.stdin.readline

n=int(input())
left=[0]
for _ in range(n):
    left.append(int(input()))
right=[0]
for _ in range(n):
    right.append(int(input()))

dp=[[0]*(n+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if -4<=left[i]-right[j]<=4: dp[i][j]=dp[i-1][j-1]+1
        else: dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])
