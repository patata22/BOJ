n=int(input())
card=list(map(int,input().split()))
dp=[1]*n
for i in range(n):
    N=card[i]
    for j in range(i):
        if N>card[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
