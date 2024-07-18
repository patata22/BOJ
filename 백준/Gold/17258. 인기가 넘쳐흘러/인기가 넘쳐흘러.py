n,m,K,T=map(int,input().split())

count=[0]*(n+2)
for _ in range(m):
    a,b=map(int,input().split())
    count[a]+=1
    count[b]-=1

for i in range(1,n+2):
    count[i]+=count[i-1]

dp=[[[-float('inf')]*(K+1) for i in range(K+1)] for i in range(n+1)]
dp[0][K][0]=0
answer=0

for i in range(n):
    nxt=count[i+1]
    if nxt>=T:
        for j in range(K+1):
            for k in range(K+1):
                dp[i+1][j][0] = max(dp[i+1][j][0],dp[i][j][k]+1)
    else:
        for j in range(K+1):
            for k in range(K+1):
                
                dp[i+1][j][k]=max(dp[i+1][j][k],dp[i][j][k])
                total=k+nxt
                if total>=T:
                    
                    dp[i+1][j][k] = max(dp[i+1][j][k],dp[i][j][k]+1)
                else:
                    need=T-total
                    if j>=need and k+need<=K:
                        dp[i+1][j-need][k+need]=max(dp[i+1][j-need][k+need],dp[i][j][k]+1)
                

answer=0
for i in range(1,n+1):
    for j in range(K+1):
        for k in range(K+1):
            answer=max(answer,dp[i][j][k])

print(answer)
