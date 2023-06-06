DIV=1000000009
dp=[[[0]*4 for i in range(1001)] for i in range(1001)]
dp[0][0][0]=1
for i in range(1,1001):
    for k in range(1,4):
        if i-k>=0:
            for j in range(1,1001):
                dp[i][j][k]+=sum(dp[i-k][j-1])%DIV

for _ in range(int(input())):
    n,m=map(int,input().split())
    answer=0
    for i in range(1,m+1):
        answer+=sum(dp[n][i])
    print(answer%DIV)