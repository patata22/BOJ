import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
orange=[int(input()) for i in range(n)]
dp=[k*i for i in range(n+1)]


for i in range(n+1):
    light,heavy = float('inf'),-float('inf')
    for j in range(1,m+1):
        if i+j>n: break
        light=min(light,orange[i+j-1])
        heavy=max(heavy,orange[i+j-1])

        dp[i+j]=min(dp[i+j],dp[i]+k+j*(heavy-light))

print(dp[-1])
