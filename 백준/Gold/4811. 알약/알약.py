dp=[[0]*31 for i in range(31)]
dp[0]=[1]*31

for i in range(1,31):
    for j in range(30):
        dp[i][j]=dp[i-1][j+1]
        if j: dp[i][j]+=dp[i][j-1]

while True:
    n=int(input())
    if not n: break
    print(dp[n][0])