tri=[1]
gap=1
gapgap=2
n=int(input())
while tri[-1]<n:
    gap+=gapgap
    gapgap+=1
    tri.append(tri[-1]+gap)
if tri[-1]>n:tri.pop()
m=len(tri)

dp=[i for i in range(n+1)]
for i in range(m):
    num=tri[i]
    for j in range(num,n+1):
        dp[j]=min(dp[j-num]+1,dp[j])
print(dp[-1])
