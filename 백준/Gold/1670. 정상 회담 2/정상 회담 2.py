DIV=987654321

n=int(input())
dp=[0]*(n//2+1)
dp[0]=1

for i in range(1,len(dp)):
    result=0
    for j in range(i):
        result+=(dp[j]*dp[i-1-j])%DIV
    dp[i]=result%DIV

print(dp[-1])
   