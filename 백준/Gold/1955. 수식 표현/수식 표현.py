dp=[float('inf')]*10001
dp[0]=0
dp[1]=1
dp[2]=2
dp[3]=3
dp[4]=4
dp[5]=5
dp[6]=3
dp[7]=4
now=6
n=int(input())
for i in range(4,8):
   now*=i
   dp[now]=dp[i]

for i in range(8,10001):
   if dp[i]!=float('inf'): continue
   for j in range(1,i//2+1):
      dp[i]=min(dp[i],dp[i-j]+dp[j])

   temp=int(i**0.5)+1
   for j in range(1,temp):
      if i%j==0: dp[i]=min(dp[i],dp[i//j]+dp[j])

print(dp[n])