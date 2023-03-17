def solution(n):
    if n<=2: return n
    DIV=1234567
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=(dp[i-1]+dp[i-2])%DIV
    return dp[-1]