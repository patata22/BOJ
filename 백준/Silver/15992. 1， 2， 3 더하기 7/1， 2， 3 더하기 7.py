DIV=1000000009

dp=[[0]*1001 for i in range(1001)]
dp[1][1]=1
dp[2][1]=1
dp[3][1]=1

for i in range(2,1001):
    for j in range(2,1001):
        for k in range(1,4):
            dp[i][j]+=dp[i-k][j-1]
        dp[i][j]%=DIV

for _ in range(int(input())):
    a,b=map(int,input().split())
    print(dp[a][b])
