n=int(input())
start=[0]+list(map(int,input()))
end=[0]+list(map(int,input()))

dp=[[float('inf')]*10 for i in range(n+1)]
dp[0][0]=0
before=[[0]*10 for i in range(n+1)]
for i in range(1,n+1):
    target=end[i]
    for j in range(10):
        now=(start[i]+j)%10
        for k in range(10): 
            leftMove=(k-j)%10 
            temp=(now+leftMove)%10
            rightMove=(temp-target)%10 
            if dp[i][k]>dp[i-1][j]+leftMove+rightMove:
                dp[i][k]=dp[i-1][j]+leftMove+rightMove
                before[i][k]=j

print(min(dp[-1]))
        
