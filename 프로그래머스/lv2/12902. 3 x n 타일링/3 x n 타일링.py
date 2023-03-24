def solution(n):
    DIV=1000000007
    dp=[0]*(n+1)
    dp[0]=1
    dp[2]=3
    for i in range(4,n+1,2):
        dp[i]=((4*dp[i-2])%DIV-dp[i-4]%DIV)%DIV
    return dp[-1]