DIV= 1000000007

graph = ((1,2), (0,2,3), (0,1,3,5), (1,2,4,5), (3,5,6), (2,3,4,7), (4,7), (5,6))

d=int(input())

dp=[[0]*8 for i in range(d+1)]
dp[0][0]=1

for i in range(1,d+1):
    for j in range(8):
        for k in graph[j]:
            dp[i][j]+=dp[i-1][k]%DIV
        dp[i][j]%=DIV

print(dp[d][0])