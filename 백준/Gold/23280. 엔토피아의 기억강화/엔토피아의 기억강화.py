board=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
distance = [[float('inf')]*13 for i in range(13)]

n,a,b=map(int,input().split())

for i in range(4):
    for j in range(3):
        s=board[i][j]
        for k in range(4):
            for l in range(3):
                e=board[k][l]
                dist=abs(i-k)+abs(j-l)
                distance[s][e]=dist
                distance[e][s]=dist

number=list(map(int,input().split()))
start=number[0]
dp=[[[float('inf')]*13 for i in range(13)] for i in range(n)]

dp[0][start][3]=distance[1][start]+a
dp[0][1][start]=distance[start][3]+b

for i in range(1,n):
    target=number[i]
    for l in range(13):
        for r in range(13):
            if dp[i-1][l][r]==float('inf'): continue
            tempL= dp[i-1][l][r] + distance[l][target]+a
            dp[i][target][r]=min(dp[i][target][r],tempL)
            tempR = dp[i-1][l][r]+distance[r][target]+b
            dp[i][l][target]=min(dp[i][l][target],tempR)
answer=float('inf')

for i in range(13):
    for j in range(13):
        if i==number[-1] or j==number[-1]:
            answer=min(answer,dp[-1][i][j])
            
print(answer)