
x=input()
n=len(x)

dp=[0]*n
dp[0]=1
if 10<=int(x[0]+x[1])<=34: dp[1]=1
for i in range(1,n):
    if x[i]!='0':dp[i]+=dp[i-1]
    if 10<=int(x[i-1]+x[i])<=34: dp[i]+=dp[i-2]
print(dp[-1])
    
