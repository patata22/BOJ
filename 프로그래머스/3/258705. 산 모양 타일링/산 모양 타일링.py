DIV = 10007

def solution(n, tops):
    
    dp=[0]*(2*n+2)
    dp[0]=1
    dp[1]=1
    for i in range(2,2*n+2):
        if i%2==0:
            if tops[i//2-1]:
                dp[i]+=2*dp[i-1] 
                dp[i]+=dp[i-2]
                dp[i]%=DIV
            else:
                dp[i]+=dp[i-1] 
                dp[i]+=dp[i-2] 
        else:
            dp[i]+=(dp[i-1]+dp[i-2])%DIV
        
    return dp[-1]