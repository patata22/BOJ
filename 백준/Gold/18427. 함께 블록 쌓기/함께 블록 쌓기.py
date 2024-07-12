DIV=10007

n,m,h=map(int,input().split())
blocks=[tuple(map(int,input().split())) for i in range(n)]

dp=[[0]*(h+1) for i in range(n+1)]
dp[0][0]=1
for i in range(1,n+1):
    block=blocks[i-1]
    for b in block:
        for j in range(b,h+1):
            dp[i][j]+=dp[i-1][j-b]
    for j in range(h+1):
        dp[i][j]+=dp[i-1][j]
        dp[i][j]%=DIV
    

print(dp[-1][h])
