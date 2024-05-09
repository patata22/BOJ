DIV=10**9

n=int(input())

dp=[[0]*20 for i in range(n+1)]
dp[0][0]=1
for i in range(1,n+1):
    for j in range(20):
        temp=1<<j
        if temp<=i:
            for k in range(j+1):
                dp[i][j]+=dp[i-temp][k]
        else:break
        dp[i][j]%=DIV
print(sum(dp[-1])%DIV)
            
