n=int(input())
number='0'+input()

dp=[float('inf')]*(n+1)
dp[0]=0
for i in range(1,n+1):
    if number[i]!='0': dp[i]=dp[i-1]+1
    if number[i-1]!='0':
        dp[i]=min(dp[i],dp[i-2]+1)
    if i>=2 and number[i-2]!='0':
        temp=int(number[i-2:i+1])
        dp[i]=min(dp[i],dp[i-3]+1)
print(dp[-1])
        