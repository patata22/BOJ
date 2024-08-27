DIV=1000000007

n=int(input())
dp = [[[0]*5 for i in range(10)] for i in range(n)]
for i in range(10): dp[0][i][0]=1

for i in range(1,n):
    for j in range(10):
        for k in (j-1,j+1):
            if not 0<=k<10: continue
            if k==j-1:
                dp[i][k][1]=(dp[i][k][1]+dp[i-1][j][-1]+dp[i-1][j][-2]+dp[i-1][j][0])%DIV    
                dp[i][k][2]=(dp[i][k][2]+dp[i-1][j][1])%DIV
            elif k==j+1:
                dp[i][k][-1]=(dp[i][k][-1]+dp[i-1][j][1]+dp[i-1][j][2]+dp[i-1][j][0])%DIV
                dp[i][k][-2]=(dp[i][k][-2]+dp[i-1][j][-1])%DIV
answer=0
for i in range(10):
    for j in range(5):
        answer+=dp[-1][i][j]
print(answer%DIV)