import sys
input=sys.stdin.readline

d,n=map(int,input().split())
temper = [int(input()) for i in range(d)]
cloth=[tuple(map(int,input().split())) for i in range(n)]
dp=[[0]*n for i in range(d)]

for i in range(n):
    a,b,c=cloth[i]
    if not a<=temper[0]<=b: dp[0][i]=-float('inf')

for i in range(1,d):
    for j in range(n):
        a,b,c=cloth[j]
        if a<=temper[i]<=b:
            for k in range(n):
                temp=dp[i-1][k]+abs(cloth[k][2]-c)
                dp[i][j]=max(dp[i][j],dp[i-1][k]+abs(cloth[k][2]-c))
        else:dp[i][j]=-float('inf')

print(max(dp[-1]))