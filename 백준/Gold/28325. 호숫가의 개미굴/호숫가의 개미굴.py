n=int(input())
number=list(map(int,input().split()))
answer=0

dp=[[0]*2 for i in range(n)]
dp[0][0]=number[0]
for i in range(1,n):
    dp[i][0]=max(dp[i-1])+number[i]
    dp[i][1]=dp[i-1][0]+1
    
answer=max(max(dp[-1]),answer)

dp=[[0]*2 for i in range(n)]
dp[0][0]=0
dp[0][1]=1
for i in range(1,n):
    dp[i][0]=max(dp[i-1])+number[i]
    dp[i][1]=dp[i-1][0]+1

answer=max(dp[-1][0],answer)
print(answer)
