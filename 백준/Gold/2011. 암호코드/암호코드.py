DIV=1000000

pw=[0]+list(map(int,input()))
n=len(pw)

dp=[0]*n
dp[0]=1
for i in range(1,n):
    if pw[i]:
        dp[i]=dp[i-1]
    if pw[i-1] and 1<=10*pw[i-1]+pw[i]<=26:dp[i]+=dp[i-2]
    dp[i]%=DIV
if pw[1]==0: print(0)
elif n==2:print(1)
else:print(dp[-1])

