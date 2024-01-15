k,n=map(int,input().split())


dp=[[0]*128 for i in range(n+1)]
dp[0][k]=1

for t in range(1,n+1):
    for x in range(1,127):
        if x!=1: dp[t][x]+=dp[t-1][x-1]
        dp[t][x]+=dp[t-1][x+1]

print(sum(dp[-1]))
        
