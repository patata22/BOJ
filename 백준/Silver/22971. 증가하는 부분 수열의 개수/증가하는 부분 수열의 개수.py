DIV=998244353

n=int(input())
number=list(map(int,input().split()))
dp=[1]*n

for i in range(n):
    for j in range(i):
        if number[i]>number[j]:
            dp[i]+=dp[j]
    dp[i]%=DIV
print(*dp)