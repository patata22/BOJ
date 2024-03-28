a=list(input())
b=list(input())
n=len(a)
m=len(b)
dp=[[0]*(m+1) for i in range(n+1)]
answer=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i-1]==b[j-1]:         
            dp[i][j]=dp[i-1][j-1]+1
            answer=max(answer,dp[i][j])
print(answer)
