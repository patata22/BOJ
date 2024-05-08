word=list(input())
target=list(input())
n,m=len(word),len(target)
dp=[[0]*m for i in range(n)]
for i in range(n):
    dp[i][0]+=dp[i-1][0]
    if word[i]==target[0]:
        dp[i][0]+=1

for i in range(n):
    x=word[i]
    for j in range(1,m):
        y=target[j]
        if x==y:
            dp[i][j]=min(dp[i-1][j-1],dp[i-1][j]+1)
        else:
            dp[i][j]=min(dp[i-1][j-1],dp[i-1][j])
print(dp[-1][-1])