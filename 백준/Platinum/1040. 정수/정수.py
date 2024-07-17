def countBit(x):
    cnt=0
    while x:
        cnt+=x%2
        x//=2
    return cnt

def check(x):
    used=[0]*10
    while x:
        used[x%10]=1
        x//=10
    return sum(used)==K

n,K=map(int,input().split())
N=len(str(n))
dp = [[[float('inf')]*2 for i in range(1024)] for i in range(N+1)]
part=[n//(10**i) for i in range(N)]
part=part[::-1]
for i in range(10):
    if i>part[0]: dp[1][1<<i][1]=i
    else: dp[1][1<<i][0]=i
for i in range(1,N):
    target=part[i]
    for j in range(1024):
        for k in range(2):
            if dp[i][j][k]==float('inf'): continue
            now=dp[i][j][k]
            for k in range(10):
                nxt = now*10+k
                if nxt>target:
                    dp[i+1][j|(1<<k)][1] = min(dp[i+1][j|(1<<k)][1], nxt)
                elif nxt==target: dp[i+1][j|1<<k][0]=min(dp[i+1][j|1<<k][0], nxt)

answer=n if check(n) else float('inf')
for i in range(1024):
    if countBit(i)==K and dp[-1][i][1]!=float('inf'): answer=min(answer,dp[-1][i][1])

    
if answer==float('inf'):
    length = max(K, N+1)
    temp='1'
    temp+='0'*(length-K+1)
    temp+='23456789'[:K-2]
    print(temp)
    
else:print(answer)