def solution(sticker):
    n=len(sticker)
    if n==1: return sticker[0]
    dp=[[0]*2 for i in range(n)]
    dp[0][0]=sticker[0]
    
    for i in range(1,n):
        dp[i][0]= max(dp[i-1][0], dp[i-2][0]+sticker[i])
        dp[i][1]= max(dp[i-1][1], dp[i-2][1]+sticker[i])
                                
    return max(dp[-2][0],dp[-1][1])
        
