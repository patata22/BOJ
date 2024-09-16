n=int(input())
number=list(map(int,input().split()))
dp=[-float('inf')]*101
dp[number[0]]=0
for i in range(1,n):
    now=number[i]
    for j in range(1,101):
        dp[now]=max(dp[now],dp[j]+(now-j)*(now-j))
print(max(dp))

