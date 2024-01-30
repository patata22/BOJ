import sys
input=sys.stdin.readline

n,m,d=map(int,input().split())
board=[list(map(int,input().split())) for i in range(n)]
dp=[[-float('inf')]*m for i in range(n)]
dp[0]=[0]*m
for i in range(1,n):
    for j in range(m):
        for up in range(1,min(d,i)+1):
            left=max(0,j-d+up)
            right=min(m-1,j+d-up)
            for side in range(left,right+1):
                dp[i][j]=max(dp[i][j],dp[i-up][side]+board[i-up][side]*board[i][j])
print(max(dp[-1]))