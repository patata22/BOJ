def solution(n, money):
    DIV=1000000007
    dp=[0]*(n+1)
    dp[0]=1
    for m in money:
        for now in range(1,n+1):        
            if now-m>=0:
                dp[now]+=dp[now-m]%DIV
        dp[now]%=DIV
    return dp[-1]