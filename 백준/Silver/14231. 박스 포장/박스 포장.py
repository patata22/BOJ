n=int(input())
number=list(map(int,input().split()))
dp=[1]*n
for i in range(n):
    for j in range(i):
        if number[j]<number[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))