import sys
input=sys.stdin.readline

m,n=map(int,input().split())
price=[tuple(map(int,input().split())) for i in range(n)]

dp=[[[float('inf')]*3 for i in range(m)] for i in range(n)]
for i in range(m): dp[0][i][0]=price[0][i]
minimum=min(price[0])

for i in range(1,n):
    nxtMin = float('inf')
    for j in range(m):
        temp = price[i][j]
        dp[i][j][0]=minimum+temp
        dp[i][j][1]= dp[i-1][j][0]+(temp*9)//10
        dp[i][j][2]= min(dp[i-1][j][1],dp[i-1][j][2])+(temp*7)//10
        
        nxtMin = min(nxtMin,min(dp[i][j]))
    minimum=nxtMin

answer=float('inf')

for i in range(m):
    answer=min(answer,min(dp[-1][i]))
print(answer)