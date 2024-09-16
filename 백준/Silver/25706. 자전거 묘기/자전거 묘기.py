n=int(input())
number=tuple(map(int,input().split()))
dp=[1]*n
for i in range(n-2,-1,-1):
    jump=number[i]
    if i+1+jump<n:
        dp[i]+=dp[i+1+jump]

print(*dp)