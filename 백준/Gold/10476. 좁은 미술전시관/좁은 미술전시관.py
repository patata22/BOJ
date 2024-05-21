import sys
input=sys.stdin.readline

while True:
    n,k=map(int,input().split())
    if n==0: break

    left=[0]
    right=[0]

    for _ in range(n):
        l,r=map(int,input().split())
        left.append(l)
        right.append(r)
    #0 둘다 열림 1 왼쪽 열림 2 오른쪽 열림
    dp=[[[-float('inf')]*3 for i in range(k+1)] for i in range(n+1)]
    dp[0][0][0]=0
    for i in range(1,n+1):
        l,r=left[i],right[i]
        dp[i][0][0]=max(dp[i-1][0])+l+r
        for j in range(1,k+1):
            dp[i][j][0]=max(dp[i-1][j])+l+r
            dp[i][j][1]=max(dp[i-1][j-1][0],dp[i-1][j-1][1])+l
            dp[i][j][2]=max(dp[i-1][j-1][0],dp[i-1][j-1][2])+r
    print(max(dp[-1][-1]))
    



