distance=[[float('inf')]*5 for i in range(5)]
for i in range(5):
    distance[i][i]=1
for i in range(1,5):
    distance[0][i]=2
    distance[i][0]=2
for i in (1,2):
    distance[i][i+2]=4
    distance[i+2][i]=4
for i in (2,4):
    distance[1][i]=3
    distance[i][1]=3
    distance[3][i]=3
    distance[i][3]=3

number=list(map(int,input().split()))
n=len(number)
dp=[[[float('inf')]*5 for i in range(5)] for i in range(n)]
dp[0][0][0]=0
for i in range(1,n):
    target=number[i-1]
    for l in range(5):
        for r in range(5):
            temp=dp[i-1][l][r]+distance[l][target]
            dp[i][target][r]=min(dp[i][target][r],temp)

            temp=dp[i-1][l][r]+distance[r][target]
            dp[i][l][target]=min(dp[i][l][target],temp)
answer=float('inf')
for i in range(5):
    for j in range(5):
        answer=min(answer,dp[-1][i][j])
print(answer)
