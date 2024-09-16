n=int(input())
number=list(map(int,input().split()))
if n==1: print(0)
else:
    dp=[[0]*2 for i in range(n)]
    dp[0][1]=number[0]
    for i in range(1,n):
        dp[i][0]=dp[i-1][1]
        dp[i][1]=min(dp[i-1])+number[i]
    print(min(dp[-1]))

