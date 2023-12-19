n,m=map(int,input().split())
size=set()
number=list(map(int,input().split()))
for i in range(m):
    size.add(number[i])
    for j in range(i+1,m):
        size.add(number[i]+number[j])

size=sorted(list(size))
dp=[float('inf')]*(n+1)
dp[0]=0
for i in range(1,n+1):
    for j in size:
        if j>i: break
        dp[i]=min(dp[i],dp[i-j]+1)
if dp[-1]==float('inf'):print(-1)
else:print(dp[-1])