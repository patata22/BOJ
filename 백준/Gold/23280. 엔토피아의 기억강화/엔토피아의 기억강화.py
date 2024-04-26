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
dp=[[[float('inf')]*13 for i in range(13)] for i in range(n+1)]
dp[0][1][3]=0

for i in range(1,n+1):
    target=number[i-1]
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
        answer=min(dp[-1][i][j],answer)
            
print(answer)
