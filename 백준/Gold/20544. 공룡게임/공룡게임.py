DIV=1000000007

n=int(input())

dp=[[[0]*3 for i in range(3)] for i in range(n)]

dp[0][0][0]=1
for i in range(1,n):
    dp[i][0][0]+=(dp[i-1][0][0]+dp[i-1][1][1]+dp[i-1][1][2]+dp[i-1][2][1]+dp[i-1][2][2])%DIV
    dp[i][1][1]+=dp[i-1][0][0]
    dp[i][2][1]+=dp[i-1][0][0]
    dp[i][1][2]+=(dp[i-1][1][1]+dp[i-1][2][1])%DIV
    dp[i][2][2]+=dp[i-1][1][1]

answer1=(sum(dp[-1][0])+sum(dp[-1][1])+sum(dp[-1][2]))%DIV


dp=[[[0]*3 for i in range(2)] for i in range(n)]
dp[0][0][0]=1
for i in range(1,n):
    dp[i][0][0]=(dp[i-1][0][0]+dp[i-1][1][1]+dp[i-1][1][2])%DIV
    dp[i][1][1]+=dp[i-1][0][0]
    dp[i][1][2]+=dp[i-1][1][1]

answer2=(sum(dp[-1][0])+sum(dp[-1][1]))%DIV
print((answer1-answer2)%DIV)
    