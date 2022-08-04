text1=list(input())
text2=list(input())
n=len(text1)
m=len(text2)
dp=[[0]*(m+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if text1[i-1]==text2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])
print(dp[-1][-1])

