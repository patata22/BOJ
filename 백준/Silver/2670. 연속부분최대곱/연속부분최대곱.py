n=int(input())
number=[float(input()) for i in range(n)]
dp=[0]*(n+1)
for i in range(n):
    dp[i]=max(dp[i-1]*number[i],number[i])
   
print('%.3f' %max(dp))

