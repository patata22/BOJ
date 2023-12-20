for _ in range(int(input())):
    n=int(input())
    coins=tuple(map(int,input().split()))
    m=int(input())

    dp=[[0]*(m+1) for i in range(n)]
    for i in range(n):
        dp[i][0]=1
        coin=coins[i]
        for j in range(1,m+1):
            dp[i][j]+=dp[i-1][j]
            if j>=coin:dp[i][j]+=dp[i][j-coin]
    print(dp[-1][-1])
            
    
