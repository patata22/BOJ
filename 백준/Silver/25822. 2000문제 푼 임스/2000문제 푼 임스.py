c=min(2,int(float(input())//0.99))
n=int(input())
number=list(map(int,input().split()))
dp=[[0]*(c+1) for i in range(n)]
answer=0
for i in range(n):
    if number[i]:
        for j in range(c+1):
            dp[i][j]=dp[i-1][j]+1
    else:
        for j in range(1,c+1):
            dp[i][j]=dp[i-1][j-1]+1

for i in range(n):
    for j in range(c+1):
        answer=max(answer,dp[i][j])
print(answer)
print(max(number))
