for tt in range(int(input())):
    number=tuple(map(int,input().split()))
    n=len(number)
    dp=[[0]*2 for i in range(n)]
    dp[0][1]=number[0]
    for i in range(1,n):
        dp[i][0]=max(dp[i-1])
        dp[i][1]=dp[i-1][0]+number[i]
    print(max(dp[-1]))
                