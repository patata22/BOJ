DIV=1000000007
n=int(input())
# n,mod3,last
dp=[[[0]*10 for i in range(3)] for i in range(n+1)]
dp[1][1][1]=1
dp[1][2][5]=1

for i in range(2,n+1):
    for j in range(3):
        for k in range(10):            
            for x in (1,5):
                dp[i][j][x]+=(dp[i-1][(j-x)%3][(k-x)%10])
            dp[i][j][k]%=DIV

print((dp[n][0][0]+dp[n][0][5])%DIV)
