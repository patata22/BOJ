def getScore(i,j):
    l=lose[j]
    if dp[i][j-1]%k==0: return l
    return min(dp[i][j-1]%k,l)

n=int(input())
win=[0]+list(map(int,input().split()))
m=int(input())
lose=[0]+list(map(int,input().split()))
k=int(input())
dp=[[0]*(m+1) for i in range(n+1)]
for i in range(1,n+1):
    dp[i][0]=dp[i-1][0]+win[i]
for j in range(1,m+1):
    dp[0][j]=dp[0][j-1]-getScore(0,j)
        
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j]=max(dp[i-1][j]+win[i],dp[i][j-1]-getScore(i,j))
print(dp[-1][-1])
